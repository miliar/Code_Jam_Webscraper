#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;

using namespace std;

int n, D;
pair<int, int> F[10009];
int d[10009];

priority_queue<pair<int, int> > Q;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 1;  I <= T; ++I) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", &F[i].first, &F[i].second);
		}
		//sort(F, F + n);
		scanf("%d", &D);
		bool flag = false;
		MEM(d, -1);
		d[0] = F[0].first;
		Q.push(make_pair(0, d[0]));
		F[n] = make_pair(D, 1000000001);
		while (!Q.empty()) {
			int v = Q.top().first;
			int td = Q.top().second;
			Q.pop();
			if (td == d[v]) {
				for (int i = 0; i <= n; ++i) {
					if (abs(F[v].first - F[i].first) <= d[v]) {
						if (min(F[i].second, abs(F[v].first - F[i].first)) > d[i]) {
							d[i] = min(F[i].second, abs(F[v].first - F[i].first));
							Q.push(make_pair(i, d[i]));
						}
					}
				}
			}
		}



		if (d[n] >= 0)
			printf("Case #%d: YES\n", I);
		else
			printf("Case #%d: NO\n", I);
	}
	return 0;
}