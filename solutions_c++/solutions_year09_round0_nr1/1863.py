#include <iostream>
using namespace std;

char	Dict[6000][20];
char	Req[5000];
bool	mark[6000];
int		p,m,n,Ans;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d%d%d",&p,&m,&n);
	for (int i=1;i<=m;i++)
		scanf("%s",Dict[i]);
	for (int i=1;i<=n;i++)
	{
		for (int j=1;j<=m;j++)	mark[j]=1;
		scanf("%s",Req);
		int h=0;	int t=strlen(Req)-1;
		int step=-1;
		while (h<=t)
		{
			step++;
			if (Req[h]=='(')
			{
				int k;
				for (k=h+1;k<=t;k++)
					if (Req[k]==')')	break;
				for (int l=1;l<=m;l++)
					if (mark[l])
					{
						mark[l]=0;
						for (int j=h+1;j<=k-1;j++)
							if (Req[j]==Dict[l][step])	mark[l]=1;
					}
				h=k+1;
			}
			else
			{
				for (int j=1;j<=m;j++)
					if (Req[h]!=Dict[j][step])	mark[j]=0;
				h++;
			}
		}
		Ans=0;
		for (int j=1;j<=m;j++)
			if (mark[j])	Ans++;
		printf("Case #%d: %d\n",i,Ans);
	}
}
