#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<queue>
using namespace std;
#define Check(a) if(a)while(1)puts("kero");
 
bool kero(){
	int p,q,i,j;
	long long n;
	scanf("%lld%d%d",&n,&p,&q);
	if(q == 100 && p != 100)return 0;
	if(q == 0 && p != 0)return 0;
	if(n>1000) return 1;
	for(i=1;i<=n;i++){
		for(j=0;j<=i;j++){
			int jj = j*100;
			if(jj%i == 0 && jj/i == p)
				return 1;
		}
	}
	return 0;
}
int main(){
	int T,TC=1;
	scanf("%d",&T);
	while(T--){
		printf("Case #%d: %s\n",TC++,kero()?"Possible":"Broken");
	}
}
