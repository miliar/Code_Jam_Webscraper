#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
__int64 n;

void init(){
	scanf("%I64d",&n);
	return;
}

__int64 gcd(__int64 x,__int64 y){
	if (y==0){
		return x;
	} else {
		return gcd(y,x%y);
	}
}

__int64 process(){
	__int64 last,cur;
	scanf("%I64d%I64d",&last,&cur);
	__int64 dif=abs(last-cur);
	last=cur;
	for (__int64 i=3;i<=n;i++){
		__int64 k;
		scanf("%I64d",&k);
		dif=gcd(dif,abs(last-k));
		last=k;
	}
	__int64 ans=last%dif;
	ans=dif-ans;
	ans%=dif;
	return ans;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,process());
	}
	return 0;
}
