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
int S[1000][1000];
int L[1000];
int C[1000][1000];

int lim[1000];
int k,K;


bool wpisz(int x,int y){
	//if(x+2*K>2*k) return false;
	FOR(i,0,2*k-1) FOR(j,0,lim[i]) C[i][j] = -1;
	FOR(i,0,2*K-1){
		if(i+x>=2*k-1) return false;
		FOR(j,0,L[i]){
			if(j+y<0 || j+y>=lim[i+x]) return false;
			C[x+i][j+y] = S[i][j];
		}
		if(L[i+1]>L[i] && lim[x+i+1]<lim[x+i]) y--;
		else if(L[i+1]<L[i] && lim[x+i+1]>lim[x+i]) y++;
	} 
	return true;
}

bool check(int a,int b){
	if(a==-1 || b==-1 || a==b) return false;
	return true;
}
bool sprawdz(){
	bool ok = false;
	int A = k-2, B = k;
	while(A>=0 && B<2*k-1){
		FOR(j,0,lim[A]) ok |= check(C[A][j],C[B][j]);
		
		A--;B++;
	}
	FOR(i,0,2*k-1){
		int A = 0, B = lim[i]-1;
		while(A<B){
			ok|= check(C[i][A],C[i][B]);
			A++;B--;
		}
	}
	return !ok;
}

int main(){
	int T;scanf("%d",&T);
	FORE(test,1,T){
//		int k;
		FOR(i,0,1000) FOR(j,0,1000) S[i][j] = -1;
		scanf("%d",&k);	
		K = k;
		for(int i = 1;i<=k;i++){
			L[i-1] = i;
			for(int j = 0;j<i;j++) scanf("%d",&S[i-1][j]);
		}
		int w = k;
		for(int i = k-1;i>=1;i--){
			L[w] = i;
			for(int j = 0;j<i;j++) scanf("%d",&S[w][j]);
			w++;
		}
		int ret = -1;
		int W = 0;
		while(true){
			for(int i = 1;i<=k;i++) lim[i-1] = i;
			int w = k;
			for(int i = k-1;i>=1;i--) lim[w++] = i;
			for(int x=0;x<2*k-1;x++){
				for(int y = 0;y<lim[x];y++){
					if(wpisz(x,y)){
					//	printf("%d %d\n",x,y);
						if(sprawdz()) ret = W;
					}
				}
			}
			if(ret!=-1) break;
			W+=2*k+1;
			k++;
		//	break;
		}
		printf("Case #%d: %d\n",test,ret);fflush(stdout);	
	}
}
