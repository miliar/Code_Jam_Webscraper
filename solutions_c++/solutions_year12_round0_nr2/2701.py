#include <cstdlib>
#include <cstring>
#include <cstdio>

int n,id,t[110],s,p,T,ans;
int i;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for (id=1;id<=T;id++)
	{
		ans=0;
		scanf("%d%d%d",&n,&s,&p);
		for (i=0;i<n;i++)
		{
			scanf("%d",&t[i]);
			if (t[i]==0)
			{
				if (p==0)ans++;
			}
			else if (t[i]==1)
			{
				if (p<=1)ans++;
			}
			else if (t[i]>=29)
			{
				ans++;
			}
			else
			{
				if (t[i]%3==0)
				{
					if(t[i]/3>=p)ans++;
					else if (t[i]/3+1>=p && s>0)
					{
						s--;ans++;
					}
				}
				else if (t[i]%3==1)
				{
					if(t[i]/3+1>=p)ans++;
				}
				else
				{
					if (t[i]/3+1>=p)ans++;
					else if (t[i]/3+2>=p && s>0)
					{
						s--;ans++;
					}
				}
			}
		}
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}