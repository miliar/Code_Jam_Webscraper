/*
Author  :kabir.iut06
Compiler: GNU C++ Code Blocks
problem : A
Contest : 2010 Google CodeJam qualification Round*/

#include<stdio.h>
typedef long long LL;
LL n,num,b,t,k,txt;
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%lld",&t);
	while(t--){
		scanf("%lld%lld",&n,&k);
		num=1;
		b=num=(num<<n)-1;
		if(k>num){
			num=num+1;
			num=k%num;
		}
		else num=k;
		if(num!=b)printf("Case #%lld: OFF\n",++txt);
		else printf("Case #%lld: ON\n",++txt);
	}
	return 0;
}