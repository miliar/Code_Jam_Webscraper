#include<iostream>
#include<map>
#include<queue>
using namespace std;
int a[1000];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int ca=1;ca<=zu;ca++)
	{
		printf("Case #%d: ",ca);
		int m;
		scanf("%d",&m);
		for(int i=0;i<m;i++)
		{
			char ccc[100];
			scanf("%s",ccc);
			int j;
			for(j=m-1;j>0;j--)
			{
				if(ccc[j]=='1')
				{
					break;
				}
			}
			a[i]=j;
		}
		int x=0;
		while(1)
		{
			bool f=1;
			for(int i=0;i<m;i++)
			{
				if(a[i]>i)
				{
					f=0;break;
				}
			}
			if(f)break;
			for(int i=0;i<m;i++)
			{
				if(a[i]>i)
				{
					for(int j=i+1;j<m;j++)
					{
						if(a[j]<=i)
						{
							for(int k=j;k>i;k--)
							{
								swap(a[k],a[k-1]);
								x++;
							}
							break;
						}
					}
				}
			}
		}
		printf("%d\n",x);
	}
}