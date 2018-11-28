#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int t[101][20];
int l, l2;

void debug() {
	for (int j = 0; j < l2; ++j) {
		for (int i = 0; i < l; ++i) {
			cout << t[i][j];
		}cout << endl;
	}cout << endl;
}

int cnt(string s1, string s2) {
	l = s1.length();
	l2 = s2.length();
	for (int i = 0; i < l; ++i) {
		t[i][0] = (s1[i] == s2[0]) ? 1 : 0;
	}
	for (int j = 1; j < l2; ++j) {
		for (int i = 0; i < l; ++i) {
			t[i][j] = 0;
			if (s1[i] == s2[j]) {
				for (int k = 0; k < i; ++k) {
					t[i][j] = (t[i][j] + t[k][j-1]) % 10000;
				}
			}
		}
	}
	int r = 0;
	for (int i = 0; i < l; ++i) {
		r += t[i][l2-1];
	}
	return r % 10000;
}

int main() {
	fstream fn;
	ofstream fn2;
	int N;
	char s[1001];
	//cout << "Result: " << cnt("aabbaa", "abbaa") << endl;
	
	fn.open ("input.txt");
	fn2.open ("C:\output.txt");
	fn >> N;
	fn.getline(s, 1000);
	for (int test = 0; test < N; ++test) {
		fn.getline(s, 1000);
		int c;
		c = cnt(s, "welcome to code jam");
		//cout << c;
		fn2.width(0);
		fn2.fill(' ');
		fn2 << left;
		fn2 << "Case #" << (test + 1) << ": " ;
		fn2.width(4);
		fn2.fill('0');
		fn2 << right;
		fn2 << c << endl;
	}
	fn.close();
	fn2.close();
	
	// system("pause");
	return 0;
}