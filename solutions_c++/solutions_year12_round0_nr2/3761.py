#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,s,p,num;
		int count=0;
		scanf("%d%d%d",&n,&s,&p);
		int min=3*p-4;
		int max=3*p-2;
		if(p==0)
		{
			min=0;
			max=0;
		}
		else if(p==1)
		{
			min=2;
			max=1;
		}
		while(n--)
		{
			scanf("%d",&num);
			if(num>=max)count++;
			else if(s && num>=min)
			{
				count++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
