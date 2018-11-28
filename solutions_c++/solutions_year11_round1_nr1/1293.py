#include<cstdlib>
#include<stdio.h>
#include<vector>

using namespace std;


int nwd(int a, int b)
{
	int tmp;
	while(b!=0)
	{
		tmp=b;
		b=a%b;
		a=tmp;
	}
	return a;
}

int main()
{
	int t,n,pd,pg;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		scanf("%d%d%d",&n,&pd,&pg);
		if(pg==0)
		{
			if(pd==0)
				printf("Case #%d: Possible\n",i+1);
			else printf("Case #%d: Broken\n",i+1);
		}
		else if(pg==100)
		{
			if(pd==100)
				printf("Case #%d: Possible\n",i+1);
			else printf("Case #%d: Broken\n",i+1);
		}
		else if(100<=n*nwd(100,pd))
			printf("Case #%d: Possible\n",i+1);
		else printf("Case #%d: Broken\n",i+1);	
	}
	return 0;
}
