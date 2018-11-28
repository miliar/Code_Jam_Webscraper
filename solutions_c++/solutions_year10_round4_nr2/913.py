#include <queue>
#include <sstream>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <cmath>
using namespace std;

const int M = 4096;
const double eps=1e-9;
const int DIR[2][2]={{0,-1},{-1,0}}; //R,D,L,U
const int DIRX[8][2]={{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};

int getlower(int n, int k) {
	int step = 1u << k;
	for (int i = 0; i <= M; i += step) {
		if (n <= i - 1)
			return i - step;
	}
}
int getupper(int n, int k) {
	int step = 1u << k;
	for (int i = 0; i <= M; i += step) {
		if (n <= i - 1)
			return i;
	}
}
int main() {
	int T, P, x;
	cin >> T;
	for (int kase = 0; kase < T; ++kase) {
		cin >> P;
		int team[M];
		int val[M];
		memset(val, 0, sizeof(val));
		int n = 1u << P;
		for (int i = 0; i < n; ++i) {
			cin >> team[i];
			team[i] = P - team[i];
		}
		for (int i = 0; i < P; ++i)
			for (int j = 0; j < 1u << (P-i-1); ++j)
				cin >> x;
		int ret = 0;
		for (int i = P; i > 0; --i) {
			for (int j = 0; j < n; ++j) {
				if (team[j] > 0) {
					ret ++;
					int st = getlower(j, i);
					int ed = getupper(j, i);
					//printf("%d,%d - %d, %d\n", i, j, st, ed);
					for (int k = st; k < ed; ++k)
						if (team[k] > 0) team[k] --;
					j = ed - 1;
				}
			}
			/*	
			for (int j = 0; j < n; ++j)
				printf("%d ", team[j]);
			printf("\n");
			*/
		}
		cout << "Case #" << kase + 1 << ": " << ret << endl;
	}
	return 0;
}



