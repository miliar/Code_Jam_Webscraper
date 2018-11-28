#include<stdio.h>
#include<algorithm>
using namespace std;
int data[10000];
char at[10000];
int ans=-99999999,in;
void perm(int lvl)
{
	if(lvl==in)
	{
		int n,a=0,b=0,sa=0,sb=0,oka=0,okb=0;
		for(n=0;n<in;n++)
		{
			if(at[n]==0)
			{
				oka=1;
				a^=data[n];
				sa+=data[n];
			}
			else
			{
				okb=1;
				b^=data[n];
				sb+=data[n];
			}
		}
		//printf("%d %d\n",a,b);
		if(a==b&&oka&&okb)
			ans=max(ans,max(sa,sb));
		return;
	}
	at[lvl]=0;
	perm(lvl+1);
	at[lvl]=1;
	perm(lvl+1);
}
void process()
{
	int n;
	ans=-99999999;
	scanf("%d",&in);
	for(n=0;n<in;n++)
		scanf("%d",&data[n]);
	perm(0);
	if(ans<0)
		printf("NO\n");
	else
		printf("%d\n",ans);
}
int main()
{
	int ix,n;
	scanf("%d",&ix);
	for(n=0;n<ix;n++)
	{
		printf("Case #%d: ",n+1);
		process();
	}
}
