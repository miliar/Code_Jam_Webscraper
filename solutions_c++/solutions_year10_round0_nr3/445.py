#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define FS first
#define SD second

int Q[10000];
int W[10000];
int P[10000];

int main(){
	int T;scanf("%d",&T);
	FORE(test,1,T){
		LL ret = 0;
		int r,k,n;scanf("%d%d%d",&r,&k,&n);
		FOR(i,0,n) scanf("%d",&Q[i]);
		FOR(i,n,2*n) Q[i] = Q[i-n];
		FOR(i,0,n){
			int ile = 0,g = 0;
			while(g<n){
				if(ile+Q[i+g]>k) break;
				ile+=Q[i+g];
				g++;
			}
			P[i] = ile;
			W[i] = g;		
		}				
		int cur = 0;
		FOR(i,0,r){
			ret+=(LL)P[cur];
			cur = cur+W[cur];
			if(cur>=n) cur-=n;
		}
		printf("Case #%d: %lld\n",test,ret);
	}
}
