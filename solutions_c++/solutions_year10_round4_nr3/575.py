#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

const int MAXN = 105;

int _t, res, n;
bool in[MAXN][MAXN];

void output(int k = 7) {
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < k; j++) {
			cout << in[i][j];
		}
		cout << endl;
	}
	cout << endl << endl;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &_t);
	for (int cas = 1; cas <= _t; cas++) {
		memset(in, 0, sizeof(in));
		scanf("%d", &n);
		for (int z = 0, a, b, c, d; z < n; z++) {
			scanf("%d%d%d%d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++)
				for (int j = b; j <= d; j++)
					in[i][j] = true;
		}
		res = 0;
		bool flag = true;
		while (flag) {
			//output();
			flag = false;
			for (int i = MAXN - 1; i >= 0; i--) {
				for (int j = MAXN - 1; j >= 0; j--) {
					if (i == 0 || j == 0) {
						in[i][j] = false;
						continue;
					}
					if (in[i - 1][j] == true && in[i][j - 1] == true) {
						in[i][j] = true;
						flag = true;
					} else if (in[i - 1][j] == false && in[i][j - 1] == false) {
						in[i][j] = false;
					}
					if (in[i][j] == true) flag = true;
				}
			}
			res++;
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}