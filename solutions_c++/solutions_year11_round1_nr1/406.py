/*
 TASK: A. FreeCell Statistics
 LANG: C++
*/
#include <iostream>
#include <cstdio>

using namespace std;

typedef long long lld;

int t,iii;
lld n,pd,pg,i;

int main()
{
	freopen("A-large-1.in.txt","r",stdin);
	freopen("A-large-1.out.txt","w",stdout);
	scanf("%d",&t);
	for(iii=1;iii<=t;iii++)
	{
		cin>>n;
		cin>>pd;
		cin>>pg;
		if(pg==100||pg==0)
		{
			if(pd==pg)
			{
				printf("Case #%d: Possible\n",iii);
			}
			else
			{
				printf("Case #%d: Broken\n",iii);
			}
		}
		else
		{
			for(i=1;i<=n;i++)
			{
				if((i*pd)%100==0)
				{
					break;
				}
			}
			if(i!=n+1)
			{
				printf("Case #%d: Possible\n",iii);
			}
			else
			{
				printf("Case #%d: Broken\n",iii);
			}
		}
	}
	return 0;
}