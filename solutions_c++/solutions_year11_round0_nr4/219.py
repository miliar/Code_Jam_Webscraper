#include <cstdio>
#include <cstring>
#define oo 1005
int a[oo];
bool mk[oo];
int N;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	int ans= 0;
	memset(mk,0,sizeof mk);
	for (int i=1;i<=N;++i)
		if (!mk[i])
		{
			int cnt=0,u=a[i];
			while (!mk[u])
			{
				mk[u]=true;
				u=a[u];
				++cnt;
			}
			
			if (cnt>1) ans+=cnt;
		}
	
	printf("%d.0000\n",ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
