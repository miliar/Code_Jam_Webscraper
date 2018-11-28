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
const __int64 maxn=1000001;
__int64 n,nprime;
__int64 p[maxn];
bool isprime[maxn];

void preprocess(){
	memset(isprime,false,sizeof(isprime));
	for (__int64 i=2;i<=1000;i++){
		if (isprime[i]){
			continue;
		}
		for (__int64 j=i*i;j<maxn;j+=i){
			isprime[j]=true;
		}
	}
	nprime=0;
	for (__int64 i=2;i<maxn;i++){
		if (isprime[i]){
			continue;
		}
		p[nprime]=i;
		nprime++;
	}
	return;
}

void init(){
	scanf("%I64d",&n);
	return;
}

__int64 count(__int64 k,__int64 p){
	__int64 cnt=0;
	while (1){
		if (k<p){
			break;
		}
		k/=p;
		cnt++;
	}
	return cnt;
}

__int64 calc(__int64 n){
	__int64 ans=0;
	for (__int64 i=0;i<nprime;i++){
		__int64 cnt=count(n,p[i]);
		ans+=cnt-1;
		if (cnt<=1){
			break;
		}
	}
	return ans+1;
}
	
int main(){
	preprocess();
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,calc(n));
	}
	return 0;
}
