#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <cstdio>

using namespace std;
typedef long long int ll;

void print_case(ll num, ll ris) {
	cout << "Case #" << num << ": " << ris << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N, S, p, max_nor, max_sur, tot_nor = 0, tot_sur = 0;
		cin >> N; cin >> S; cin >> p;
		max_nor = 3 * p - 2;
		max_sur = 3 * p - 4;
		for (int j = 0; j < N; j++) {
			int f;
			cin >> f;
			if (f >= max_nor) {
				tot_nor++;
			} else if (f >= max_sur && max_sur >= 0) {
				tot_sur++;
			}
		}
		tot_sur = (tot_sur < S ? tot_sur : S);
		print_case(i, tot_nor + tot_sur);
	}
}
