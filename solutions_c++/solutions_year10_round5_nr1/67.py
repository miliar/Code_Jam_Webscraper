#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=101;
const __int64 maxm=1000000;
__int64 a[maxn],prime[maxm+1];
__int64 range,k;
__int64 primecnt;

void preprocess(){
	primecnt=0;
	for (__int64 i=2;i<=maxm;i++){
		primecnt++;
		prime[primecnt]=i;
		for (__int64 j=1;j<primecnt;j++){
			if (prime[j]*prime[j]>i){
				break;
			}
			if (i%prime[j]==0){
				primecnt--;
				break;
			}
		}
	}
	return;
}

__int64 powermod(__int64 a,__int64 b,__int64 mod){
	if (b==0){
		return 1;
	}
	if (b==1){
		return a%mod;
	}
	__int64 ans=powermod(a,b/2,mod);
	ans=ans*ans;
	ans%=mod;
	if (b%2==1){
		ans*=a;
		ans%=mod;		
	}
	return ans;
}

void init(){
	__int64 d;
	scanf("%I64d%I64d",&d,&k);
	range=1;
	for (__int64 i=1;i<=d;i++){
		range*=10;
	}
	for (__int64 i=1;i<=k;i++){
		scanf("%I64d",&a[i]);
	}
	return;
}

__int64 calc(__int64 p){
	__int64 ta[20],tb[20];
	for (__int64 i=1;i<=k-2;i++){
		ta[i]=(a[i+1]-a[i])%p;
		tb[i]=(a[i+2]-a[i+1])%p;
		if (ta[i]<0){
			ta[i]+=p;
		}
		if (tb[i]<0){
			tb[i]+=p;
		}
	}
	__int64 cura=(tb[1]*powermod(ta[1],p-2,p))%p;
	__int64 curb=(a[2]-a[1]*cura)%p;
	if (cura<0){
		cura+=p;
	}
	if (curb<0){
		curb+=p;
	}
	for (__int64 i=1;i<=k-2;i++){
		if ((ta[i]*cura)%p!=tb[i]){
			return -2;
		}
	}
	return (a[k]*cura+curb)%p;
}

void process(){
	__int64 ans=-2;
	for (__int64 i=1;i<=primecnt;i++){
		if (prime[i]>range){
			break;
		}
		__int64 cur=-3;
		for (__int64 j=1;j<=k;j++){
			if (prime[i]<=a[j]){
				cur=-2;
				break;
			}
		}
		if (cur==-3){
			for (__int64 j=1;j<k;j++){
				if (a[j]==a[k]){
					cur=a[j+1];
					break;
				}
			}
		}
		if (cur==-3){
			if (k<3){
				cur=-1;
			}
		}
		if (cur==-3){
			cur=calc(prime[i]);
		}
		if (cur==-2){
			continue;
		}
		if (cur==-1){
			ans=-1;
			break;
		}
		if (ans==-2){
			ans=cur;
			continue;
		}
		if (ans!=cur){
			ans=-1;
			break;
		}
	}
	if (ans==-1){
		puts("I don't know.");
	} else {
		printf("%I64d\n",ans);
	}
	return;
}

int main(){
	preprocess();
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: ",i);
		process();
	}
	return 0;
}
