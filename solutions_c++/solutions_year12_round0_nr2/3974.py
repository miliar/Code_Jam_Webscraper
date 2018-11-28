#include<iostream>
#include<cstring>
#include<string>
using namespace std;
int times,n,s,p,num,all,total;
bool use1,use2;
void check(int x)
{
	if (p==0)
	{
		use1=use2=1;return ;
	}
	if (p==1)
	{
		if (x>=1) use1=use2=1;
		else use1=use2=0;
		return ;
	}
	if (x<(p*3-4))
	{
		use1=use2=0;
	}else
	{
		if (x>=p*3-2)
		{
			use1=use2=1;
		}else
		{
			use1=0;
			use2=1;
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		all=total=0;
		scanf("%d%d%d",&n,&s,&p);
		for (int a=0;a<n;++a)
		{
			scanf("%d",&num);
			check(num); 
			if (use2==1)
			{
				if (use1==1)
				{
					all++;
				}else
				{
					total++;
				}
			}
		}
		all+=min(total,s);
		printf("Case #%d: %d\n",z,all);
	}
}
