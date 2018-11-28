#include<stdio.h>
#include<string.h>

int p[2][4000];
int t,na,nb;
int x,y;

int main()
{
	freopen("output.txt","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		memset(p,0,sizeof(p));
		scanf("%d",&t);
		scanf("%d%d",&na,&nb);
		for(int i=0;i<na;i++)
		{
			scanf("%d:%d",&x,&y);
			p[0][x*60+y]++;
			scanf("%d:%d",&x,&y);
			p[1][x*60+y+t]--;
		}
		for(int i=0;i<nb;i++)
		{
			scanf("%d:%d",&x,&y);
			p[1][x*60+y]++;
			scanf("%d:%d",&x,&y);
			p[0][x*60+y+t]--;
		}
		int ansa = 0, tmp = 0;
		for(int i=0;i<3600;i++)
		{
			tmp -= p[0][i];
			if(tmp<0)
			{
				ansa -= tmp;
				tmp=0;
			}
		}
		int ansb = 0; tmp = 0;
		for(int i=0;i<3600;i++)
		{
			tmp -= p[1][i];
			if(tmp<0)
			{
				ansb -= tmp;
				tmp=0;
			}
		}
		printf("Case #%d: %d %d\n",test,ansa,ansb);
	}
	return 0;
}
