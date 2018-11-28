#include <stdio.h>

#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
template<typename T> inline bool checkmin(T &a, const T &b) {
	return a > b ? a = b, 1 : 0;
}
template<typename T> inline bool checkmax(T &a, const T &b) {
	return a < b ? a = b, 1 : 0;
}
typedef long long lint;

const int MAXN = 2000;
int T, n, d, val[MAXN], dd[MAXN], ans;
bool flag;

int main() {
	freopen("c.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d", &n);
		ans = 0;
		flag = true;
		for (int i = 0; i < n - 1; i++) {
			scanf("%d", val + i);
			val[i]--;
			for (int j = 0; j < i; j++)
				if (val[j] > i && val[j] < val[i]) {
					flag = false;
					break;
				}
		}
		if (!flag) {
			printf("Impossible");
		} else {
			int k;
			dd[n - 1] = 10000000;
			dd[n - 2] = 7000000;
			double tmp;
			for (int i = n - 3; i >= 0; i--) {
				if (val[i] == i + 1) {
					tmp = double(dd[val[i + 1]] - dd[i + 1]) / (val[i + 1] - (i
							+ 1)) * (val[i + 1] - i);
					dd[i] = dd[val[i + 1]] - (int(tmp) + 10);
				} else {
					for (int j = i + 1; j < n - 1; j++)
						if (val[i] == val[j]) {
							k = j;
							break;
						}
					tmp = double(dd[val[i]] - dd[k]) / (val[i] - k) * (val[i]
							- i);
					dd[i] = dd[val[i]] - (int(tmp) - 10);
				}
			}
			tmp = 0;
			for (int i = 0; i < n; i++)
				if (dd[i] < 0 && tmp > dd[i])
					tmp = dd[i];
			for (int i = 0; i < n; i++)
				dd[i] += -int(tmp) + 10;
			for (int i = 0; i < n; i++)
				cout << dd[i] << ' ';
		}
		puts("");
	}
	return 0;
}

