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

int n,k,p;
int mem[5000][1000];
int modu = 30031;

int go(int km,int mask){
	if(mem[km][mask]!=-1) return mem[km][mask];
	if((mask&1)==0){
		return 0;
		mem[km][mask]=go(km+1,(mask>>1));
		return mem[km][mask];
	}
	if(km+k-1==n){
	//printf("%d ",mask);
		return 1;
	}
	mem[km][mask]=0;
	
	FORE(i,1,p){
		if(km+i>n) break;
		if( ((mask>>i)&1)==0 ){
			mem[km][mask]=(mem[km][mask]+go(km+1,(mask+(1<<i))>>1))%modu;
		}
	}

	return mem[km][mask];
}
int main(){
	int T;
	scanf("%d",&T);
	FORE(tt,1,T){
		scanf("%d%d%d",&n,&k,&p);
		int mask = 0;
		FOR(i,0,k) mask+=(1<<i);
		FOR(i,0,5000) FOR(j,0,1000) mem[i][j]=-1;
		printf("Case #%d: %d\n",tt,go(1,mask));				
	}
}
