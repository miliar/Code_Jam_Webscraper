#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main() {
	fstream fn;
	ofstream fn2;
	fn.open ("C:\input.txt");
	fn2.open ("C:\output.txt");
	
	char s[101];
	int N;
	fn >> N;
	fn.getline(s, 1000);

	for (int test = 0; test < N; ++test) {
		int l;
		vector <char> v;
		map <char, int> m;
		long long R = 0;
		fn.getline(s, 100);
		fn2 << "Case #" << (test + 1) << ": ";
		l = strlen(s);
		for (int i = 0; i < l; ++i) {
			bool f = false;
			for (int j = 0; j < v.size(); ++j) {
				if (v[j] == s[i]) {
					f = true;
					break;
				}
			}
			if (!f) {
				v.push_back(s[i]);
			}
		}
		int O = v.size();
		if (O == 1) {
			O = 2;
			for (int i = 0; i < l; ++i) {
				R = R * O + 1;
			}
			cout << R << endl;
			fn2 << R << endl;
			continue;
		}
		int tmp = v[0];
		v[0] = v[1];
		v[1] = tmp;
		for (int i = 0; i < v.size(); ++i) {
			m[v[i]] = i;
		}
		for (int i = 0; i < l; ++i) {
			R = R * O + m[s[i]];
		}
		cout << R << endl;
		fn2 << R << endl;
	}
	fn.close();
	fn2.close();
	
	system("pause");
	return 0;
}