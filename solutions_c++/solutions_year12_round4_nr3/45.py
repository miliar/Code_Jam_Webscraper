#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=2001;
const int oo=1000000000;
int p[maxn],cnt[maxn],v[maxn],cur[maxn];
int f[maxn][maxn];
int n;
bool flag;

void init(){
	scanf("%d",&n);
	for (int i=1;i<n;i++){
		scanf("%d",&p[i]);
		cur[i]=1;
	}
	memset(f,0,sizeof(f));
	memset(cnt,0,sizeof(cnt));
	memset(v,0xff,sizeof(v));
	cur[n]=1;
	v[0]=v[n+1]=oo;
	flag=false;
	return;
}

int det(int p,int li,int lh,int ri,int rh){
	return (int(((double)rh)-((double)(rh-lh))*((double)(ri-p))/((double)(ri-li))))-1;	
}

void dp(int st,int en,int li,int lh,int ri,int rh){
	if (flag){
		return;
	}
	if (st>en){
		return;
	}
	if (cnt[en]==0){
		v[en]=max(v[en],0);
		dp(st,en-1,li,lh,ri,rh);
		return;
	}
	if (cnt[en]<cur[en]){
		dp(st,en-1,li,lh,ri,rh);
		return;
	}
	int now=f[en][cur[en]];
	cur[en]++;
	if ((st>now)||(en<now)){
		flag=true;
		return;
	}
	if (v[en]<0){
		v[en]=det(en,li,lh,ri,rh);
	}
	if (v[now]<0){
		v[now]=det(now,li,lh,ri,rh);
	}
	dp(st,now,now,v[now],en,v[en]);
	dp(now,en,now,v[now],en,v[en]);
	return;
}

void process(){
	for (int i=1;i<n;i++){
		if (p[i]<=i){
			puts(" Impossible");
			return;
		}
		cnt[p[i]]++;
		f[p[i]][cnt[p[i]]]=i;
	}
	dp(1,n,0,oo,n+1,oo);
	if (flag){
		puts(" Impossible");
		return;		
	}
	for (int i=1;i<=n;i++){
		printf(" %d",v[i]);
	}
	puts("");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d:",i);
		process();
	}
	return 0;
}
