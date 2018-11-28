#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define oo 50
#define inf 100000
int Test,Case;
int map[oo][oo];
char s[oo][oo];
int a[oo];
int x[oo],y[oo];
bool mx[oo],my[oo];
int lx[oo],ly[oo];
int N;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%s",s[i]+1);
	for (int i=1;i<=N;++i)
	{
		a[i]=0;
		for (int j=N;j>0;--j)
			if (s[i][j]=='1')
			{
				a[i]=j;
				break;
			}
	}
}

inline void Solve()
{
	int ans=0;
	
	for (int i=1;i<=N;++i)
	{
		for (int j=i;j<=N;++j)
			if (a[j]<=i)
			{
				ans+=abs(i-j);
				for (int k=j;k>i;--k)
					swap(a[k-1],a[k]);
				break;
			}
	}
	
	printf("%d\n",ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		
		Readin();
		Solve();
	}
	
	return 0;
}
