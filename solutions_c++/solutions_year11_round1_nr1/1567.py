#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,pd,pg,nd,ng,ca=0,x,flag;
	scanf("%d",&t);
	while(t--)
	{
		++ca;
		scanf("%d%d%d",&n,&pd,&pg);
		flag=0;
		if(pd==0)    
		{
			x=0;
			if(pg<100)
			{
				printf("Case #%d: Possible\n",ca);
				continue;
			}
			else
			{
				printf("Case #%d: Broken\n",ca);
			}
		}
		else
		{
			flag=0;
			for(x=1;x<=n;x++)
			{
				if((x*100)%pd==0)
				{
					nd=(x*100)/pd;
					if(nd>n) continue;
					if(pd<100&&pg==100) continue;
					if(pd>0&&pg==0) continue;
					flag=1;
				}
			}
			if(flag==1)
				printf("Case #%d: Possible\n",ca);
			else
				printf("Case #%d: Broken\n",ca);
		}
	}
	return 0;
}
