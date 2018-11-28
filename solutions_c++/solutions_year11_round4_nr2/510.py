#include <iostream>

using namespace std;

char a[1000][1000];
long long w[1000][1000];
long long s[1000][1000];
long long sy[1000][1000];
long long sx[1000][1000];

int n,m,d;

int doing()
{
	scanf("%d %d %d\n",&n,&m,&d);
	for (int i=0;i<n;i++)
		gets(a[i]);
	memset(s,0,sizeof(s));
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			w[i][j]=(a[i-1][j-1]-'0')+d;
			s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+w[i][j];
			sy[i][j]=sy[i-1][j]+sy[i][j-1]-sy[i-1][j-1]+w[i][j]*(long long)j;
			sx[i][j]=sx[i-1][j]+sx[i][j-1]-sx[i-1][j-1]+w[i][j]*(long long)i;
		}
	int ans=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			for (int k=1;i-k>0 && i+k<=n && j-k>0 && j+k<=m;k++)
			{
				if ((sy[i+k][j+k]-sy[i+k][j-k-1]-sy[i-k-1][j+k]+sy[i-k-1][j-k-1]
				-w[i+k][j+k]*(j+k)-w[i-k][j+k]*(j+k)-w[i-k][j-k]*(j-k)-w[i+k][j-k]*(j-k)
				==(long long)j*(s[i+k][j+k]-s[i+k][j-k-1]-s[i-k-1][j+k]+s[i-k-1][j-k-1]-w[i+k][j+k]-w[i-k][j+k]-w[i+k][j-k]-w[i-k][j-k]))
					&&(sx[i+k][j+k]-sx[i+k][j-k-1]-sx[i-k-1][j+k]+sx[i-k-1][j-k-1]
				-w[i+k][j+k]*(i+k)-w[i-k][j+k]*(i-k)-w[i-k][j-k]*(i-k)-w[i+k][j-k]*(i+k)
				==(long long)i*(s[i+k][j+k]-s[i+k][j-k-1]-s[i-k-1][j+k]+s[i-k-1][j-k-1]-w[i+k][j+k]-w[i-k][j+k]-w[i+k][j-k]-w[i-k][j-k])))
					
					{
						ans=max(ans,k*2+1);	
					}
			}
				for (int k=1;i-k>0 && i+k+1<=n && j-k>0 && j+k+1<=m;k++)
			{
				if (2*(sy[i+k+1][j+k+1]-sy[i+k+1][j-k-1]-sy[i-k-1][j+k+1]+sy[i-k-1][j-k-1]
				-w[i+k+1][j+k+1]*(j+k+1)-w[i-k][j+k+1]*(j+k+1)-w[i-k][j-k]*(j-k)-w[i+k+1][j-k]*(j-k))
				==(long long)(2*j+1)*(s[i+k+1][j+k+1]-s[i+k+1][j-k-1]-s[i-k-1][j+k+1]+s[i-k-1][j-k-1]-w[i+k+1][j+k+1]-w[i-k][j+k+1]-w[i+k+1][j-k]-w[i-k][j-k])
					&&2*(sx[i+k+1][j+k+1]-sx[i+k+1][j-k-1]-sx[i-k-1][j+k+1]+sx[i-k-1][j-k-1]
				-w[i+k+1][j+k+1]*(i+k+1)-w[i-k][j+k+1]*(i-k)-w[i-k][j-k]*(i-k)-w[i+k+1][j-k]*(i+k+1))
				==(long long)(2*i+1)*(s[i+k+1][j+k+1]-s[i+k+1][j-k-1]-s[i-k-1][j+k+1]+s[i-k-1][j-k-1]-w[i+k+1][j+k+1]-w[i-k][j+k+1]-w[i+k+1][j-k]-w[i-k][j-k]))
					
					{
					//	cout << i << ' ' << j << endl; 
						ans=max(ans,k*2+2);	
					}
			}
		}
	if (ans!=0)
	cout << ans << endl;
	else
		cout <<"IMPOSSIBLE" << endl;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
