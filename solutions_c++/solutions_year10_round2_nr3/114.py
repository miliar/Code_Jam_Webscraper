#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=501;
const __int64 modo=100003;
__int64 c[maxn][maxn];
__int64 f[maxn][maxn];
__int64 ans[maxn];

void preprocess(){
	memset(c,0,sizeof(c));
	c[0][0]=1;
	for (__int64 i=1;i<maxn;i++){
		c[i][0]=1;
		for (__int64 j=1;j<maxn;j++){
			c[i][j]=c[i-1][j-1]+c[i-1][j];
			c[i][j]%=modo;
		}
	}
	return;
}

void dp(){
	memset(f,0,sizeof(f));
	for (__int64 i=2;i<maxn;i++){
		f[i][1]=1;
		for (__int64 j=2;j<i;j++){
			for (__int64 k=1;k<j;k++){//f[i][j]==>f[j][k]
				__int64 rem=i-j-1;
				__int64 need=j-k-1;
				if (rem<need){
					continue;
				}
				__int64 delta=f[j][k]*c[rem][need];
				delta%=modo;
				f[i][j]+=delta;
				f[i][j]%=modo;
			}
		}
	}
	memset(ans,0,sizeof(ans));
	for (__int64 i=2;i<maxn;i++){
		for (__int64 j=1;j<i;j++){
			ans[i]+=f[i][j];
			ans[i]%=modo;
		}
	}
	return;
}

int main(){
	preprocess();
	dp();
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 k=1;k<=cse;k++){
		__int64 t;
		scanf("%I64d",&t);
		printf("Case #%I64d: %I64d\n",k,ans[t]);
	}
	return 0;
}
