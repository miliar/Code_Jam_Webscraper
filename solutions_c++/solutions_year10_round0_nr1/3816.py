#include<stdio.h>
int a[31];
void mid()
{
	int y=1;
	for(int x=0;x<=30;x++)
	{
		y=2*y;
		a[x]=y;
	}
}
void main()
{
	int t,k[10000],n[10000];
	scanf("%d",&t);
	mid();
	for(int x=0;x<t;x++)
	{
		scanf("%d %d",&n[x],&k[x]);
		if(k[x]==0){printf("Case #%d: OFF\n",x+1);continue;}
		if(((k[x]+1)%(a[n[x]-1]))==0){printf("Case #%d: ON\n",x+1);}
		else {printf("Case #%d: OFF\n",x+1);}
	}
}
	