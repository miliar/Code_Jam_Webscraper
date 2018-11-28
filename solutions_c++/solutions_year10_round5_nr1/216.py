#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long llong;

#define BIT(X,B) (((X)>>(B))&1)
#define SET(X,B) ((X)|(1<<(B)))
#define CLR(X,B) ((X)&(~(1<<(B))))
#define REV(X,B) ((X)^(1<<(B)))

const int MaxP=1000000,MaxD=6;
int pr[MaxP/2],npr;
bool np[MaxP];
int lmt[MaxD+1];
int inv(int a,int p){
	llong r=1,t=a%p;
	for(int b=p-2;b;b>>=1){
		if(b&1) r=r*t%p;
		t=t*t%p;
	}
	return int(r);
}
inline int mod(int a,int m){
	return (a%m+m)%m;
}
pair<int,int> solve(int x[],int n,int p){
	if(n==1) return make_pair(2,0);
	if(n==2){
		if(x[0]==x[1]) return make_pair(1,x[0]);
		else return make_pair(2,0);
	}
	
	int d1=mod(x[1]-x[0],p),d2=mod(x[2]-x[1],p);
	int A,B;
	if(d1==0){
		if(d2!=0) return make_pair(0,0);
		else A=1,B=0;
	}
	else{
		A=d2*inv(d1,p)%p;
		B=mod(x[1]-A*x[0],p);
	}
	for(int i=1;i<n;++i)
		if((A*x[i-1]+B-x[i])%p!=0) return make_pair(0,0);
	return make_pair(1,(A*x[n-1]+B)%p);
}
int main(){
	for(int i=2;i<MaxP;++i){
		if(!np[i]) pr[npr++]=i;
		for(int j=0;j<npr&&pr[j]<=(MaxP-1)/i;++j){
			np[i*pr[j]]=true;
			if(i%pr[j]==0) break;
		}
	}
	lmt[0]=1;
	for(int i=1;i<=MaxD;++i) lmt[i]=lmt[i-1]*10;
	
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int D,K,x[10];
		scanf("%d %d",&D,&K);
		int mm=0;
		for(int i=0;i<K;++i){
			scanf("%d",x+i);
			if(x[i]>mm) mm=x[i];
		}
		pair<int,int> ans(0,0);
		for(int i=0;i<npr&&pr[i]<=lmt[D];++i){
			if(pr[i]<=mm) continue;
			pair<int,int> res=solve(x,K,pr[i]);
			if(res.first>0){
				if(ans.first==0||res.first>1) ans=res;
				else if(ans.second!=res.second) ++ans.first;
			}
			if(ans.first>1) break;
		}
		if(ans.first!=1) printf("Case #%d: I don't know.\n",cas);
		else printf("Case #%d: %d\n",cas,ans.second);
	}
	return 0;
}
