#include<sstream>
using namespace std;
int aa(int a)
{
	return a>0?a:-a;
}
int main()
{
	int n,ans,d,tt,t,i,o,b,to,tb;
	char s[1001];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		o=b=1;ans=to=tb=0;
		for(i=0;i<n;i++)
		{
			scanf("%s %d",s,&d);
			if(s[0]=='O')
			{
				if(ans-to>=aa(o-d))
				{
					ans++;to=ans;
				}
				else
				{
					ans=aa(o-d)+1+to;
					to=ans;
				}
				o=d;
			}
			else
			{
				if(ans-tb>=aa(b-d))
				{
					ans++;tb=ans;
				}
				else
				{
					ans=aa(b-d)+1+tb;
					tb=ans;
				}
				b=d;
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}