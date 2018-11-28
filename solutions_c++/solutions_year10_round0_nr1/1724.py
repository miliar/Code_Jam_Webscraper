#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,j;
	int case_cnt=0;
	int T,n,k;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",++case_cnt);
		if(  k!=0&&k%(1<<n)==(1<<n)-1)
			puts("ON");
		else
			puts("OFF");
	}
}