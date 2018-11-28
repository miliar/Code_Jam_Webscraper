#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
typedef long long ll;
int main()
{
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	int _,cas=0;
	scanf("%d",&_);
	while(_--)
	{
		ll n;
		int pd,pg;
		scanf("%lld%d%d",&n,&pd,&pg);
		bool flag=true;
		if(pd!=0&&pg==0) flag=false;
		if(pd!=100&&pg==100) flag=false;
		if(n<100&&flag)
		{
			bool found=false;
			for(int i=1;i<=n&&!found;i++)
			{
				for(int j=0;j<=i&&!found;j++)
				{
					if(j*100==i*pd) found=true;
				}
			}
			if(!found) flag=false;
		}
		printf("Case #%d: ",++cas);
		if(flag) puts("Possible");
		else puts("Broken");
	}
    return 0;
}
