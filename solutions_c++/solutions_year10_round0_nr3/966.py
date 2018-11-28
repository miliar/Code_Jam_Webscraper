#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=1001;
__int64 r,k,n;
__int64 g[maxn];
__int64 f[maxn],cap[maxn];

void init(){
	scanf("%I64d%I64d%I64d",&r,&k,&n);
	for (__int64 i=1;i<=n;i++){
		scanf("%I64d",&g[i]);		
	}
	return;
}

__int64 calc(){
	memset(f,0,sizeof(f));
	__int64 ans=0;
	__int64 st=1;
	for (__int64 i=1;i<=r;i++){
		if (f[st]==0){
			f[st]=i;
			__int64 sum=g[st];
			__int64 cur=st+1;
			cur=((cur-1)%n)+1;
			while (1){
				if (sum+g[cur]>k){
					break;
				}
				if (cur==st){
					break;
				}
				sum+=g[cur];
				cur++;
				cur=((cur-1)%n)+1;
			}
			cap[i]=sum;
			ans+=sum;
			st=cur;
			continue;
		}
		__int64 sum=0;
		for (__int64 j=f[st];j<i;j++){
			sum+=cap[j];
		}
		ans+=sum*((r-i+1)/(i-f[st]));
		for (__int64 j=f[st];j<f[st]+((r-i+1)%(i-f[st]));j++){
			ans+=cap[j];
		}
		return ans;
	}
	return ans;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,calc());
	}
	return 0;
}
