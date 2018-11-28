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

int P[100000];
int M[100000];
int D[2100][20];

int go(int v,int k){
	if(k<0) return INF;
	if(D[v][k]!=-1) return D[v][k];
	int ret = go(v*2,k)+go(v*2+1,k);
	int a = go(v*2,k+1)+go(v*2+1,k+1)+P[v];
	if(a<ret) ret = a;
	if(ret>INF) ret = INF;
//	printf("%d %d %d\n",v,k,ret);
	return D[v][k] = ret;
}
int main(){
	int T;
	scanf("%d",&T);
	FORE(test,1,T){
		int p;scanf("%d",&p);
		int n = 1<<p;
		for(int i = n-1;i>=0;i--) scanf("%d",&M[i]);
		FOR(i,0,2100) FOR(j,0,20) D[i][j] = -1;
		FOR(i,0,n){
			int v = n+i;
			M[i] = p-M[i];
			FOR(j,0,M[i]) D[v][j] = INF;
			FORE(j,M[i],p) D[v][j] = 0;
		}
		int v = n-1;
		while(true){
			scanf("%d",&P[v]);
			v--;
			if(v==0) break;
		}
		int ret = go(1,0);
		printf("Case #%d: %d\n",test,ret);
	}
}
