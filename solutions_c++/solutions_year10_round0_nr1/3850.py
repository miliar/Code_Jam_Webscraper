//gnu c++ codeblocks
#include<iostream>
#include<algorithm>
#include<cmath>
#include<stdio.h>
using namespace std;

int main(){
	long long i,j,l,n,m,k,t,cas=0;
	freopen("1.txt","r",stdin);
	//freopen("out_small.txt","w",stdout);
	freopen("out_large.txt","w",stdout);
	scanf("%lld",&t);
	while(t--){
		scanf("%lld %lld",&n,&k);
		i=1<<n;
		l=i-1;
		if(k<l || k==0){printf("Case #%lld: OFF\n",++cas);continue;}
		j=k%i;
		if(j==l)printf("Case #%lld: ON\n",++cas);
		else printf("Case #%lld: OFF\n",++cas);
	}
	return 0;
}