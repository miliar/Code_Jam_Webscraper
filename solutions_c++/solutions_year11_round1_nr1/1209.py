#include<iostream>
#include<cstdio>

using namespace std;

bool func(long long n,int pd, int pg)
{
	
	if(pg==0 && pd==0)
		return 1;
	if(pg==0)
		return 0;
	
	if(pg==100 && pd==100)
		return 1;
	if(pg==100 && pd!=100)
		return 0;
		
	if(pd==0 && pg!=0)
		return 1;

	if(pd==100 && pg!=0)
		return 1;	
		
	int k=1;
	
	while((100*k)%pd!=0 && (100*k)/pd <= n)
		k++;

	if((100*k)%pd==0 && (100*k)/pd<=n)
	{
		//if( ((100*k)/pd-k)*100/(100-pg) >=(100*k/pd) )
		return 1;
	}	
	return 0;
}

int main()
{
	int t,pd,pg;
	long long n;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		cin>>n;
		scanf("%d%d",&pd,&pg);
		if(func(n,pd,pg))
			printf("Case #%d: Possible\n",k);
		else
			printf("Case #%d: Broken\n",k);
	}
}
