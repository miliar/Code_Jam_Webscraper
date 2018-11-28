#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
typedef long long lld;
using namespace std;
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME))
#define MAX 0x7f7f7f7f
using namespace std;


int main()
{
	freopen("B-small-attempt0(2).in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		int c;
		int l,p;
		scanf("%d%d%d",&l,&p,&c);
		int ca=0;
		int ll=l;
		while(ll<p)
		{
			ll*=c;
			ca++;
		}
		int ans=0;
		if(ca==0)
			ans=0;
		else
		{
			int h=0;
			long long tt=1;
			if(ca==1)
				h=0;
			else
			{
			for(h=1;((h<=10000)&&(tt<ca));h++)
			{
				tt*=2;
				if(tt>=ca)
					break;
			}
	
		}
			ans=h;
		}
		printf("Case #%d: %d\n",i,ans);
	}

return 0;
}
