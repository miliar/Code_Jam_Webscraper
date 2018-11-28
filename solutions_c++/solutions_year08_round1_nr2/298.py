#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>

int main(void)
{
	int i, j, k;
	int c, n, m;
	vector<int> a[100];
	int sat[100];
	
	scanf("%d", &c);
	for(k=1; k<= c; k++) {
		scanf("%d", &n);
		scanf("%d", &m);
		
		for(i=0; i<m; i++) {
			a[i].clear();
			int t, q, r;
			scanf("%d", &t);
			for(j=0; j<t; j++) {
				scanf("%d %d", &q, &r);
				if(r == 0) a[i].PB(-q);
				else a[i].PB(q);
			}
		}
		
// 		int res = 1000000000;
		int f = 0;
		int rmask = 0;
		
		for(int mask = 0; mask < (1<<n); mask++) {
			memset(sat, 0, sizeof(sat));
			int cant = 0;
			for(i=0; i<n; i++) {
				for(j=0; j<m; j++) {
					if(sat[j]) continue;
					for(int q=0; q<a[j].size(); q++) {
						if(abs(a[j][q]) == i+1 && (((mask&(1<<i)) && a[j][q] > 0) || (!(mask&(1<<i)) && a[j][q] < 0))) {
							if(!sat[j]) sat[j] = 1, cant++;
							break;
						}
					}
				}
			}
			
			if(cant == m) {
				if(!f || __builtin_popcount(rmask) > __builtin_popcount(mask)) rmask = mask;
				f = 1;
			}
		}
		
		printf("Case #%d: ", k);
		if(!f) printf("IMPOSSIBLE\n");
		else {
			if(rmask&(1<<0)) printf("1");
			else printf("0");
			
			for(i=1; i<n; i++) {
				if(rmask&(1<<i)) printf(" 1");
				else printf(" 0");
			}
			printf("\n");
		}
	}
	
	return 0;
}
