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

typedef long long i64;
int N, M;
char dat[12][12];
int ans;
int prev[1024];
int next[1024];
int num[1024];
int valid[12][1024];
int main() {
	freopen("C.in","r",stdin);
	int e = 0, T ;

	scanf("%d",&T);
	while(T--) {ans = 0;
		scanf("%d%d",&N,&M);
		FOR(i,0,N)scanf("%s",dat[i]);
		SET(prev, 0);	
		int ltd = 1<<N;
		SET(num,0);
		FOR(i,0,ltd) {
			FOR(j,0,N)
				if(i&(1<<j))
					num[i]++;
		}
		SET(valid,0);
		FOR(i,0,M) {
			FOR(j,0,ltd) {
				valid[i][j]= true;
				FOR(k,0,N) {
					if ((j&(1<<k))!=0 && dat[k][i]!='.') {
						valid[i][j]=false;
						break;
					}
				}
			}
		}
		FOR(i,0,M) {
			SET(next, 0);
			FOR(j,0,ltd) {
				if (i && !valid[i-1][j]) continue;
				FOR(k,0,ltd) {
					if((j&k)!=0 || ((j>>1)&k)!=0 || (j&(k>>1))!=0)continue;
					if (!valid[i][k])continue;
					next[k] = max(next[k], prev[j] + num[k]);
				}
			}
			memcpy(prev, next, sizeof next);
		}
		ans = 0;
		FOR(i,0,ltd)
			ans=max(ans, next[i]);
		printf("Case #%d: %d\n",++e, ans);
	}

	return 0;
}


