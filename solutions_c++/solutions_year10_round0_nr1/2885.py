#include<stdio.h>
int main(){
	int tt;
	int t,N,K;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tt);
	for (t=1;t<=tt;t++){
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",t);
		if ((K&((1<<N)-1))==((1<<N)-1)) printf("ON\n");
		else printf("OFF\n");
	}
}
	
