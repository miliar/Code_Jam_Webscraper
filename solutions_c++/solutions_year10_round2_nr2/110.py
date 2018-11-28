#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=51;
__int64 n,k,b,t;
__int64 x[maxn],v[maxn];
bool ok[maxn];

void init(){
	scanf("%I64d%I64d%I64d%I64d",&n,&k,&b,&t);
	for (__int64 i=1;i<=n;i++){
		scanf("%I64d",&x[i]);
	}
	for (__int64 i=1;i<=n;i++){
		scanf("%I64d",&v[i]);
	}
	return;
}

void preprocess(){
	for (__int64 i=1;i<=n;i++){
		if ((x[i]+v[i]*t)>=b){
			ok[i]=true;
		} else {
			ok[i]=false;
		}
	}
	return;
}

void getans(){
	__int64 ans=0;
	__int64 cur=0;
	__int64 need=k;
	for (__int64 i=n;i>=1;i--){
		if (need==0){
			break;
		}
		if (ok[i]){
			ans+=cur;
			need--;
		} else {
			cur++;
		}
	}
	if (need>0){
		puts("IMPOSSIBLE");
	} else {
		printf("%I64d\n",ans);
	}
	return;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 k=1;k<=cse;k++){
		init();
		preprocess();
		printf("Case #%I64d: ",k);
		getans();
	}
	return 0;
}
