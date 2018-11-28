#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int sou[105];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	int n,s,p;
	int i;
	int ans;
	int cs=1;
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		int mid=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&sou[i]);
			if(sou[i]%3==0)
			{
				int a=sou[i]/3;
				if(a>=p)
					ans++;
				else if(a+1>=p&&a!=0)
					mid++;
			}
			else if(sou[i]%3==1)
			{
				int a=sou[i]/3+1;
				if(a>=p)
					ans++;
			}
			else if(sou[i]%3==2)
			{
				int a=sou[i]/3+1;
				if(a>=p)
					ans++;
				else if(a+1>=p)
					mid++;
			}
		}
		if(mid>=s)
			ans+=s;
		else
			ans+=mid;
		printf("Case #%d: %d\n",cs++,ans);
	}
	return 0;
}