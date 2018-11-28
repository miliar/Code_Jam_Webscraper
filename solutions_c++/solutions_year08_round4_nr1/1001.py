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
#define pii pair<int, int>

int m, v;

int val[100];
pii g[100];
int mask;
int G;

int calc(int n) {
	if(n > G) return val[n];
	else if(g[n].first == 1) {
		if(mask&(1<<(n-1))) return calc(2*n) || calc(2*n + 1);
		else return calc(2*n) && calc(2*n + 1);
	} else {
		if(mask&(1<<(n-1))) return calc(2*n) && calc(2*n + 1);
		else return calc(2*n) || calc(2*n + 1);
	}
}

bool check(int k) {
	for(int i=0; i<G; i++) if((k&(1<<i)) && g[i+1].second == 0) return false;
	return true;
}

int main(void)
{
	int i, j, k;
	
	int casos;
	
	scanf("%d", &casos);
	for(int h=0; h<casos; h++) {
		scanf("%d %d", &m, &v);
		
		G = (m-1)/2;
// 		printf("%d\n", G);
		
		for(i=1; i<=G; i++) {
			scanf("%d %d", &j, &k);
			g[i] = make_pair(j, k);
		}
		for(i=G+1; i<=m; i++) {
			scanf("%d", &val[i]);
		}
		
		int res = 1000000000;
		
		for(k=0; k<(1<<G); k++) {
			if(check(k)) {
				mask = k;
				if(calc(1) == v) res = min(res, __builtin_popcount(k));
			}
		}
		
		printf("Case #%d: ", h+1);
		if(res == 1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	
	return 0;
}
