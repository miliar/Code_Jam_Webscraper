#include <iostream>
using namespace std;


int num[10010];
int p,q;
bool vist[110];

int res;

inline void dfs(int step,int now)
{
	if (step==q)
	{
		if (now<res)
		{
			res=now;
		}
		return;
	}

	int i,j;

	for (i=0;i<q;++i)
	{
		if (!vist[num[i]])
		{
			vist[num[i]]=true;


			int ct=0;
			for (j=num[i]+1;j<=p;++j)
			{
				if (vist[j])
				{
					break;
				}
				else
				{
					++ct;
				}
			}

			for (j=num[i]-1;j>=1;--j)
			{
				if (vist[j])
				{
					break;
				}
				else
				{
					++ct;
				}
			}
			dfs(step+1,now+ct);

			vist[num[i]]=false;
		}
	}

}

int main()
{
	int T;
	int bb=1;

	freopen("C.in","r",stdin);
	freopen("C.txt","w",stdout);
	scanf("%d",&T);

	while (T--)
	{
		
		scanf("%d%d",&p,&q);

		int i;

		for (i=0;i<q;++i)
		{
			scanf("%d",&num[i]);
		}

		memset(vist,0,sizeof(vist));


		res=INT_MAX;
		dfs(0,0);

		printf("Case #%d: ",bb++);
		printf("%d\n",res);
	}
	return 0;
}