#include<iostream>
#include<cstring>
using namespace std;
int weishu(int k)
{
	int wws=0;
	while(k>0)
	{
		k/=10;
		wws++;
	}
	return wws;
}
int main()
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	int t,j,a,i,b;
	int dq,ans,dq1;
	bool hash[1001];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		memset(hash,0,sizeof(hash));
		scanf("%d%d",&a,&b);
		ans=0;
		for(i=a;i<=b;i++)
		{
			int ws=weishu(i);
			dq=0;dq1=0;
			if(ws==2)
			{
				if(hash[i]==0&&i%10!=0)
				{
					dq=(i%10)*10+i/10;
					if(hash[dq]==0&&dq!=i&&dq>=a&&dq<=b)
					{
					//	printf("%d\n",dq);
						ans++; hash[dq]=1;hash[i]=1;
					}
				}
			}
			else if(ws==3)
			{
				if(hash[i]==0&&i%10!=0)
				{
					dq=(i%10)*100+(i/10)%10+(i/100)*10;
					bool flag=0;
					if(hash[dq]!=1&&dq!=i&&dq>=a&&dq<=b)
					{
					//	printf("%d\n",i);
						ans++; hash[dq]=1; hash[i]=1;flag=1;
					}
					if(flag&&dq%10!=0)
					{
						dq1=(dq%10)*100+(dq/10)%10+(dq/100)*10;
						if(hash[dq1]!=1&&dq1!=i&&dq1>=a&&dq1<=b)
						{	
					 		hash[dq1]=1;ans+=2;
						}
					}
				}
				else if(hash[i]==0&&(i/10)%10!=0)
				{
					dq=((i/10)%10)*100+i/100;
					if(hash[dq]!=1&&dq!=i&&dq>=a&&dq<=b)
					{
					//	printf("%d\n",dq);
						ans++; hash[dq]=1; hash[i]=1;
					}
				}
			}
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}
