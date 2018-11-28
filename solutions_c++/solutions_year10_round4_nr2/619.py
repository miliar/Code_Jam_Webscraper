#include<iostream>
#include<string>

using namespace std;
const int maxp=10;
bool buy[1<<maxp];
int m[1<<maxp];
int k;
int main()
{
	freopen("out.txt","w",stdout);
	int t,p;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		memset(buy,0,sizeof(buy));
		scanf("%d",&p);
		int num=1<<p;
		for (int j=0;j<num;j++)
		{
			scanf("%d",&m[j]);
		}
		for (int j=p-1;j>=0;j--)
		{
			for (int l=0;l<(1<<j);l++)
				scanf("%d",&k);
		}
		for (int j=0;j<num;j++)
		{
			int l=j+num;
//			int cnt=p-m[j];
			for (int ii=p;ii>m[j];ii--)
			{
				int fa=(l>>ii);
				buy[fa]=1;
			}
			
		}
		int result=0;
		for (int ii=0;ii<num;ii++)
			if (buy[ii]) result++;
		printf("Case #%d: %d\n",i,result);
	}
	return 0;
}