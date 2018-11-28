#include <iostream>
using namespace std;

int t,c,i,j,k,m,n,p,q;
long long f[3111][50];
bool b[3111][50];
int a[3111];

void dfs(int n, int k)
{
	if (b[n][k]) return;
	
	if (n>=(1<<p) && n<(1 << (p+1)))
	{
		b[n][k]=true;
		if (k>=a[n]) f[n][k]=0; else f[n][k]=1 << 27;
		return;
	}
	
	if (f[n][k]==-1)
	{
	dfs(n*2,k);
	dfs(n*2+1,k);
	dfs(n*2,k+1);
	dfs(n*2+1,k+1);
	
	f[n][k]=min(f[n*2][k]+f[n*2+1][k], f[n*2][k+1]+f[n*2+1][k+1]+a[n]);
	}
	b[n][k]=true;		
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (c=1; c<=t; c++)
	{
		scanf("%d",&p);
		for (i=(1 << (p+1))-1; i>=1; i--)
		{
			scanf("%d",&a[i]);
			if (i>=(1<<p) && i<(1 << (p+1))) a[i]=p-a[i];
		}
		memset(b,false,sizeof(b));
		memset(f,-1,sizeof(f));
		dfs(1,0);
		cout << "Case #" << c << ": " << f[1][0] << endl;
	}
	
//	system("pause");
	return 0;
}
