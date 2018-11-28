#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;
int p2[33];
int aa[33];
void init(){
	int i;
	p2[1]=1;
	for(i=2;i<=30;i++)
		p2[i]=p2[i-1]*2;
	aa[1]=1;
	for(i=2;i<=30;i++)
		aa[i]=aa[i-1]+p2[i];
}

int main(){
	
	init();
	int i,T,cas,n,k,f,tt;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){
		f=0;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cas);
		tt=aa[n];
		if(k<tt){
			printf("OFF\n");
			continue;
		}
		k+=1;
		if(k%(tt+1)==0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}


