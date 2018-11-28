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
#define MAX 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 

LL kat[3][3];

LL go(int a,int ile){
	int a0 = a/3;
	int a1 = a%3;
	if(ile==1) return kat[a0][a1];
	else if(ile==2) return kat[a0][a1]*(kat[a0][a1]-1ll)/2;
	else return kat[a0][a1]*(kat[a0][a1]-1ll)*(kat[a0][a1]-2ll)/6;

}

LL countt(int a,int b,int c){
	int a0 = a/3;
	int a1 = a%3;
	int b0 = b/3;
	int b1 = b%3;
	int c0 = c/3;
	int c1 = c%3;
	if((a0+b0+c0)%3!=0) return 0;
	if((a1+b1+c1)%3!=0) return 0;
	LL ret;
	if(a==b && b==c) return go(a,3);
	else if(a==b) return go(a,2)*go(c,1);
	else if(b==c) return go(a,1)*go(b,2);
	else return go(a,1)*go(b,1)*go(c,1);
}

int main(){
	int T;
	scanf("%d",&T);
	FORE(t,1,T){
		LL n,a,b,c,d,x,y,m;
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&a,&b,&c,&d,&x,&y,&m);
		FOR(i,0,3) FOR(j,0,3) kat[i][j]=0;
		kat[x%3][y%3]++;
		FORE(i,1,n-1){
			x = (a*x+b)%m;
			y = (c*y+d)%m;
			kat[x%3][y%3]++;
		}
		LL ret = 0;
		for(int i=0;i<9;i++) for(int j=i;j<9;j++) for(int z=j;z<9;z++) ret += countt(i,j,z);
	
		printf("Case #%d: %lld\n",t,ret);
	}


}
