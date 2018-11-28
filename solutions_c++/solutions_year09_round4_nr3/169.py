#include <stdio.h>
#include <memory.h>
const int maxn=210;
int n,k;
int a[maxn][maxn];
bool g[maxn][maxn];
bool v[maxn];
int match[maxn];

bool dfs(int k)
{
	v[k]=true;
	for (int i=0;i<n;i++)
    {
		if (!g[k][i]) continue;
		if (match[i]==-1||!v[match[i]]&&dfs(match[i]))
		{
				match[i]=k;
				return true;
        }
	}
	return false;
}


bool check(int x,int y)
{
	for (int i=0;i<k;i++)
		if (a[x][i]<=a[y][i]) return false;
	return true;
}


int main(){
    freopen("c2.in","r",stdin);
    freopen("c2.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int t0=1;t0<=tests;t0++)
    {
    	scanf("%d%d",&n,&k);
    	for (int i=0;i<n;i++)
    		for (int j=0;j<k;j++)
    			scanf("%d",&a[i][j]);    			
    	for (int i=0;i<n;i++)
    		for (int j=0;j<n;j++)
    			g[i][j]=check(i,j);
    		
    	int ans=n;
    	memset(match,-1,sizeof(match));
    	for (int i=0;i<n;i++)
        {
    		memset(v,0,sizeof(v));
    		if (dfs(i)) ans--;    		
    	}
    	
		printf("Case #%d: %d\n",t0,ans);
	}

}

