#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

int main(){

	int n,i,m,k,t;
	int mask[32];
	mask[0]=1;
	for(i=1;i<28;i++)
		mask[i]=mask[i-1]*2;
	for(i=0;i<28;i++)
		mask[i]--;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		if((k&mask[n])==mask[n])
			printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}