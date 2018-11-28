#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=1025;
const __int64 maxl=21;
const __int64 oo=1000000;
__int64 f[maxl][maxn][maxn],v[maxl][maxn][maxn];
__int64 cost[maxn][maxn];
__int64 m[maxn];
__int64 n,curcase;

void init(){
	scanf("%I64d",&n);
	for (__int64 i=0;i<(1<<n);i++){
		scanf("%I64d",&m[i]);
		m[i]=n-m[i];
	}
	for (__int64 i=0;i<n;i++){
		for (__int64 j=0;j<(1<<n-i-1);j++){
			scanf("%I64d",&cost[j<<(i+1)][((j+1)<<(i+1))-1]);
		}
	}
	return;
}

__int64 search(__int64 ans,__int64 l,__int64 r){
	__int64 mid=(l+r)>>1;
	if (l==r){
		if (ans<m[r]){
			return oo;
		} else {
			return 0;
		}
	}
	if (v[ans][l][r]==curcase){
		return f[ans][l][r];
	} else {
		v[ans][l][r]=curcase;
		f[ans][l][r]=min(cost[l][r]+search(ans+1,l,mid)+search(ans+1,mid+1,r),search(ans,l,mid)+search(ans,mid+1,r));
		return f[ans][l][r];
	}
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	memset(v,0xff,sizeof(v));
	for (__int64 k=1;k<=cse;k++){
		init();
		curcase=k;
		printf("Case #%I64d: %I64d\n",k,search(0,0,(1<<n)-1));
	}
	return 0;
}
