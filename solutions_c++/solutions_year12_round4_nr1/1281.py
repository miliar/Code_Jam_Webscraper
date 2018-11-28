 //if you want,you can

#include<stdio.h>

int pos[20000];
int len[20000];
int len2[20000];
int d;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,n;
	scanf("%d",&t);

	for(int tt=0;tt<t;tt++)
	{
		scanf("%d",&n);

		for(int i=0;i<n;i++)
		{
			scanf("%d %d",&pos[i],&len[i]);
		}

		scanf("%d",&d);

		int next=1;
		len2[0]=pos[0];
		int flag=0;
		for(int i=0;i<n;i++)
		{
			if(i>=next)
			{
				break;
			}
			int reach=pos[i]+len2[i];
			if(reach>=d)
			{
				flag=1;
				break;
			}
			while(1)
			{
				if(next==n || pos[next]>reach)
				{
					break;
				}

				len2[next]=pos[next]-pos[i];
				if(len2[next]>len[next])
				{
					len2[next]=len[next];
				}

				next++;
			}
		}

		if(flag)
		{
			printf("Case #%d: YES\n",tt+1);
		}
		else
		{
			printf("Case #%d: NO\n",tt+1);
		}
	}
}
