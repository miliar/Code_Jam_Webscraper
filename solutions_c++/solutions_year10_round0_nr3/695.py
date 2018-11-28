#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
using namespace std;
#define MAXN 4000
#define DBG(x) cerr << #x <<" = " << x << endl
typedef long long ll;
ll g[MAXN];
ll R,k;
int n;
int next[MAXN];
int p[MAXN];
ll col[MAXN];

ll solve(){
	ll S=0;
	ll res=0LL,resc;
	int j=-1,i,t,s,sc;
	for(i=0;i<n;i++){
		if(i>0) S-=g[i-1];
		while(j+1<i+n&&(S+g[j+1]<=k)) j++,S+=g[j];
		next[i]=(j+1)%n;
		col[i]=S;
	}
	//for(i=0;i<n;i++) cerr << next[i] <<" ";
	//cerr << endl;
	t=0;
	memset(p,-1,sizeof p);
	while(1){
		if(p[t]==-1){
			p[t]=0;
		}else{
			sc=t;
			break;
		}
		t=next[t];
	}
	//DBG(sc);
	//predperiod
	t=0;
	while(R&&t!=sc){
		res+=col[t];
		t=next[t];
		R--;
	}
	s=-1,t=sc;
	int dl=0;
	resc=0;
	while(R&&(t!=sc||s==-1)){
		s=t;
		dl++;
		res+=col[t];
		resc+=col[t];
		t=next[t];
		R--;
	}
	res=res+resc*(R/dl);
	R=R%dl;
	while(R){
		res+=col[t];
		t=next[t];
		R--;
	}
	return res;
}

int main(){
	assert(freopen("C-large.in","rt",stdin)==stdin);
	assert(freopen("C-large.out","wt",stdout)==stdout);
	int T,Case,i;
	ll res;
	assert(scanf("%d",&T)==1);
	for(Case=1;Case<=T;Case++){
		assert(scanf("%lld%lld%d",&R,&k,&n)==3);
		for(i=0;i<n;i++) assert(scanf("%lld",&g[i])==1),g[i+n]=g[i];
		res=solve();
		printf("Case #%d: %lld\n",Case,res);
	}
	return 0;
}
