#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (105)
using namespace std;

int test,n,a[maxn][maxn],c[maxn][maxn];

inline void Print()
{
	for (int i=1;i<=6;i++,puts(""))
			for (int j=1;j<=6;j++) printf("%d",a[i][j]);
	puts("");
}
inline bool Check()
{
	memcpy(c,a,sizeof(a));
	for (int i=1;i<=100;i++)
		for (int j=1;j<=100;j++)
		{
			int A=a[i-1][j],B=a[i][j-1];
			if (A && B && !a[i][j]) c[i][j]=1;
			if (!A && !B && a[i][j]) c[i][j]=0;
		}
	memcpy(a,c,sizeof(c));
	for (int i=1;i<=100;i++)
		for (int j=1;j<=100;j++) if (a[i][j]) return true;
	return false;
}
int main()
{
//	freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		printf("Case #%d: ",cnt);
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		for (int T=1;T<=n;T++)
		{
			int X1,X2,Y1,Y2;
			scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
			for (int j=X1;j<=X2;j++)
				for (int i=Y1;i<=Y2;i++) ++a[i][j];
		}
		int ans=1;
		for (;Check();++ans);
		printf("%d\n",ans);
	}
	return 0;
}
