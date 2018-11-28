#include <stdio.h>

int N,K;
int a[10];

int solve()
{
	int tmp=K;
	int ret=0;
	int i;
	for(i=1;i<=N;i++){
		ret=K%2;
		if(ret==0)return 0;
		K/=2;
	}
	return ret;
}

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("a.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i);
		if(solve())printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}