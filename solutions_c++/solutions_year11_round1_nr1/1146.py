#include<cstdio>
int main()
{
	int X;
	scanf("%d",&X);
	int kase=1;
	while(X--)
	{
		long long int n,pd,pg;
		scanf("%lld%lld%lld",&n,&pd,&pg);
		int g,d,t1,t2;
		bool flag=false;
		for(d=1;d<=n;d++)
		{
			if((pd*d)%100!=0)continue;
			for(g=d;g<=d+1000000;g++)
			{
				if((pg*g)%100!=0)continue;
				t1=pd*d/100;
				t2=pg*g/100;
				if(t2>=t1 && g-t2>=d-t1)
				{
					flag=1;
					break;
				}
				
			}
			if(flag)break;
			break;
		}

		if(!flag)printf("Case #%d: Broken\n",kase);
		else printf("Case #%d: Possible\n",kase);
		kase++;

	}
}
