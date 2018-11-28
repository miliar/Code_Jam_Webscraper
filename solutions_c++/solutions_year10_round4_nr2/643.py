#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int func2() {
}

int func(int P, vector< vector<int> > input) {
	vector<int> a(1<<P, 0);
	int r = 0;
	for (int j = 1; j <= P; ++ j) {
		for (int k = 0; k < (1<<(P-j)); ++ k) {
			bool f = true;
			for (int l = 0; l < (1<<P); ++ l) {
				if ((l>>j) == k) {
					if (a[l]+1 > input[0][l]) {
						f = false;
						break;
					}
				}
			}
			if (!f) {
				r += input[j][k];
			} else {
				for (int l = 0; l < (1<<P); ++ l) {
					if ((l>>j) == k) ++ a[l];
				}
			}
		}
	}
	return r;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++ i) {
		int P;
		cin >> P;
		vector< vector<int> > input(P+1);
		for (int j = 0; j <= P; ++ j) {
			input[j] = vector<int>(1<<(P-j));
			for (int k = 0; k < (1<<(P-j)); ++ k) {
				cin >> input[j][k];
			}
		}
		cout << "Case #" << i << ": " << func(P, input) << endl;
	}
}
