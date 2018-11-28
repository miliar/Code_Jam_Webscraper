#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back
const int INF = 100000;
int n, m;
int C[16384], G[16384], B[16384];
int res[16384][2];
void doit(int x) {
	res[x][0] = res[x][1] = INF;
	if (x < m) {
		//interior
		int left = x*2 + 1;
		int right = left + 1;
		doit(left);
		doit(right);
		FOR(l,0,2) {
			FOR(r,0,2) {
				int v1 = res[left][l];
				int v2 = res[right][r];
				int p = l | r;
				int q = l & r;
				int orv = v1 + v2 + (G[x]==0 ? 0 : (C[x] ? 1 : INF));
				int andv = v1 + v2 + (G[x]==1 ? 0 : (C[x] ? 1 : INF));
				/*
				if (x == 1) {
					printf("l, r, v1, v2, p, q, orv, andv\n%d %d %d %d %d %d %d\n",l,r,v1,v2,p,q,orv,andv);
				}
				*/
				res[x][p] = min(res[x][p], orv);
				res[x][q] = min(res[x][q], andv);
			}
		}
	} else {
		//left
		res[x][B[x]] = 0;
	}
}
int main() {
	freopen("A.in","r",stdin);
	int e = 0 , T;
	scanf("%d",&T);
	int v;
	while(T--) {
		scanf("%d%d",&n,&v);
		m = (n-1)/2;
		int cnt = 0;
		FOR(i,0,m) {
			scanf("%d%d",&G[i],&C[i]);
			cnt+= C[i];
		}
		FOR(i,m,n) 
			scanf("%d",&B[i]);
			
		doit(0);
		/*
		FOR(i,0,n) {
			printf("%d: %6d, %6d\n",i,res[i][0],res[i][1]);
		}
		*/
		int ans = res[0][v];
		if (ans > cnt)
			printf("Case #%d: IMPOSSIBLE\n",++e);
		else
			printf("Case #%d: %d\n",++e,ans);
	}
	return 0;
}