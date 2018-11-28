#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn=600;
int p[maxn][maxn];
int left[maxn][maxn],up[maxn][maxn];
int opt[maxn][maxn];
int n,m,test;
int res[maxn*maxn];

int main()
{
	//freopen("input.txt","r",stdin);

	scanf("%d",&test);
	for (int t=1;t<=test;t++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
		{
			char st[maxn];
			scanf("%s",st);
			for (int j=0;j<m/4;j++)
			{
				int xxx;
				if (st[j]>='0' && st[j]<='9') xxx=st[j]-'0';
				else xxx=st[j]-'A'+10;
				for (int k=0;k<4;k++)
					p[i][j*4+4-k]=((xxx&(1<<k))>0)+1;
			}
		}
		
		int tot=n*m;
		for (int i=1;i<=tot;i++) res[i]=0;
		while (tot)
		{
			int best=0,rr,cc;

			for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
			{
				up[i][j]=left[i][j]=1;
				if (p[i][j-1]+p[i][j]==3) left[i][j]=left[i][j-1]+1;
				if (p[i-1][j]+p[i][j]==3) up[i][j]=up[i-1][j]+1;
				opt[i][j]=0;
				if (p[i][j]<3)
				{
					opt[i][j]=1;
					if (p[i-1][j-1]==p[i][j])
						opt[i][j]=min(opt[i-1][j-1]+1,min(left[i][j],up[i][j]));
					if (opt[i][j]>best || (opt[i][j]==best && i<rr) || (opt[i][j]==best && i==rr && j<cc))
					{
						best=opt[i][j];rr=i;cc=j;
					}
				}
			}
			//printf("%d %d %d\n",best,rr,cc);
			tot-=best*best;
			res[best]++;
			for (int i=0;i<best;i++)
			for (int j=0;j<best;j++)
				p[rr-i][cc-j]=3;
		}
		printf("Case #%d: ",t);
		int cnt=0;
		for (int i=1;i<=n*m;i++) cnt+=res[i]>0;
		printf("%d\n",cnt);
		for (int i=n*m;i;i--)
		if (res[i]) printf("%d %d\n",i,res[i]);
	}
}
