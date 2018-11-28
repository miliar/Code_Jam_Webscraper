#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T,cs;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		int n,i,j;
		char s[1005][5];
		int p[1005];
		int ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",s[i],&p[i]);
		}
		int a,b,ta,tb;
		a=b=1;
		ta=tb=0;
		for(i=0;i<n;i++)
		{
			if(s[i][0]=='O')
			{
				ta=max(ta+abs(p[i]-a)+1,tb+1);
				a=p[i];
			}
			else
			{
				tb=max(tb+abs(p[i]-b)+1,ta+1);
				b=p[i];
			}
		}
		ans=max(ta,tb);
		printf("Case #%d: %d\n",cs,ans);
	}
}