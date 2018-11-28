#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

int harms[100];
int main() {
	ifstream cin("C-small.in");
	ofstream cout("C-small.out");
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int N, L, H;
		cin >> N >> L >> H;
		for (int i = 0; i < N; i++)
			cin >> harms[i];
		int res = -1;
		for (int i = L; i <= H; i++) {
			bool valid = true;
			for (int t = 0; t < N; t++) {
				if (harms[t]%i != 0 && i%harms[t] != 0)
					valid = false;
			}
			if (valid) {
				res = i;
				break;
			}
		}
		cout << "Case #" << cc << ": ";
		if (res > -1)
			cout << res;
		else
			cout << "NO";
		cout << endl;
	}
	return 0;
}