#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

const int mn = 3;
int D,I,M,n;
int inp[mn];

int go(VI & r){
	int ret=INF;
	assert(r.sz<=3);
	if(r.sz==3){
		REP(v,256){
			VI d1,d2;
			d1.pb(r[0]);d1.pb(v);
			d2.pb(v);d2.pb(r[2]);
			ret<?=abs(r[1]-v)+go(d1)+go(d2);	
		}
		return ret;
	}	
	else{
		if(r.sz<=1)	return 0;
		int r0=r[0],r1=r[1];
		if(abs(r0-r1)<=M)	return 0;
		ret=abs(r0-r1)-M;
		if(r0>r1)	swap(r0,r1);
		if(M){
			FOR(z,r0,r1-M){
				ret<?=z-r0+(r1-z-1)/M*I;
			}
		}
		return ret;	
	}
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		D=GI,I=GI,M=GI,n=GI;
		REP(i,n)	inp[i]=GI;
		printf("Case #%d: ",kase);
		if(n<=1){printf("0\n");continue;}
		int ans=INF;
		FOR(mask,0,(1<<n)){
			VI r;
			int cand=0;
			REP(i,n){
				if(mask&(1<<i))	r.pb(inp[i]);
				else	cand+=D;
			}
			ans<?=go(r)+cand;
		}
		printf("%d\n",ans);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
