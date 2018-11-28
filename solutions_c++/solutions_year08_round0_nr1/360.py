#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const int MAXS=105;

bool tg[MAXS];
string A[MAXS];
int s,q;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++)
	{
		int i,j;
		char str[MAXS];
		scanf("%d",&s);
		getchar();
		for(i=0;i<s;i++)
		{
			gets(str);
			A[i]=str;
		}
		scanf("%d",&q);
		getchar();
		int cnt=0,ans=0;
		memset(tg,0,sizeof(tg));
		for(i=0;i<q;i++)
		{
			gets(str);
			for(j=0;j<s;j++)
			{
				if(A[j].compare(str)==0)
				{
					if(!tg[j])
					{
						tg[j]=1;
						cnt++;
						if(cnt==s)
						{
							memset(tg,0,sizeof(tg));
							cnt=1;
							tg[j]=1;
							ans++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",ic,ans);
	}
	return 0;
}
