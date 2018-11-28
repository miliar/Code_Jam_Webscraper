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
#define MOD 100003

LL D[505][505];

LL C[505][505];
LL goc(int i,int j){
	if(i<j) return 0;
	if(C[i][j]!=-1) return C[i][j];
	if(j==0){
		C[i][j]=1;
		return C[i][j];
	}
	C[i][j]=(goc(i-1,j)+goc(i-1,j-1))%MOD;
	return C[i][j];
}

int go(int n,int k){
	if(D[n][k]!=-1) return D[n][k];
	if(k==1) return D[n][k] = 1;
	LL ret = 0;
	FORE(i,1,k-1) ret+=(LL)go(k,i)*goc(n-k-1,k-i-1);
	return D[n][k] = ret%MOD;
}

int main(){
	FORE(i,0,500) FORE(j,0,500) D[i][j] = C[i][j] = -1;
	int T;scanf("%d",&T);

	FORE(test,1,T){
		int n;scanf("%d",&n);
		LL ret = 0;
		FOR(i,1,n){
			ret+=go(n,i);
			
		}
		printf("Case #%d: %lld\n",test,ret%MOD);
	}
}
