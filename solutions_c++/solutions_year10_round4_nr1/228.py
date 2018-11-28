#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define maxn 505
#define inf 1000000000

char s[maxn];
int a[maxn][maxn],n;

inline bool ok(int a,int b)
{
	return a<0 || b<0 || a==b;
}

inline int dist(int a,int b,int x,int y)
{
	return abs(a-x)+abs(b-y);
}

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d",&n);
		gets(s);
		for (int i=1;i<2*n;++i)
		{
			memset(s,0,sizeof(s));
			gets(s);
			for (int j=1;j<2*n;++j)
			if (s[j-1]>='0' && s[j-1]<='9')
				a[i][j]=s[j-1]-'0';
			else a[i][j]=-1;
		}
		
		int ans=inf;
		for (int i=1;i<2*n;++i)
			for (int j=1;j<2*n;++j)
			{
				bool fl=true;
				for (int x=1;x<2*n && fl;++x)
				{
					int left=j-1,right=j+1;
					while (left>0 && right<2*n && ok(a[x][left],a[x][right]))
						--left,++right;
					if (left>0 && right<2*n) fl=false;
				}
				for (int y=1;y<2*n && fl;++y)
				{
					int left=i-1,right=i+1;
					while (left>0 && right<2*n && ok(a[left][y],a[right][y]))
						--left,++right;
					if (left>0 && right<2*n) fl=false;
				}
				
				if (fl)
				{
					int d1=max(dist(1,n,i,j)+1,dist(2*n-1,n,i,j)+1);
					int d2=max(dist(n,1,i,j)+1,dist(n,2*n-1,i,j)+1);
					ans=min(ans, max( d1,d2 ) );
				}
			}
		
		printf("Case #%d: %d\n",test,ans*ans-n*n);
	}
	return 0;
}
