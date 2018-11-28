#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
#define INF 987654321
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

int n,m;
int mp[110][110],tmp[110][110];

int over()
{
	int i,j;
	for(i=0;i<101;i++)
	{
		for(j=0;j<101;j++)
		{
			if(mp[i][j]) return 0;
		}
	}
	return 1;
}

void change()
{
	int i,j;
	for(i=0;i<=100;i++) for(j=0;j<=100;j++) tmp[i][j]=mp[i][j];
	for(i=100;i>=0;i--)
	{
		for(j=100;j>=0;j--) if(mp[i][j] == 0)
		{
			int cnt = 0;
			int tx=i-1,ty=j;
			if(tx>=0 && ty>=0 && mp[tx][ty]==1) cnt++;
			tx=i,ty=j-1;
			if(tx>=0 && ty>=0 && mp[tx][ty]==1) cnt++;
			if(cnt == 2)
			{
				tmp[i][j] = 1;
			}
		}
	}
	for(i=100;i>=0;i--)
	{
		for(j=100;j>=0;j--) if(mp[i][j] == 1)
		{
			int cnt = 0;
			int tx=i-1,ty=j;
			if((tx>=0 && ty>=0 && mp[tx][ty]==0) || (tx<0 || ty<0)) cnt++;
			tx=i,ty=j-1;
			if((tx>=0 && ty>=0 && mp[tx][ty]==0) || (tx<0 || ty<0)) cnt++;
			if(cnt == 2)
			{
				tmp[i][j] = 0;
			}
		}
	}

	for(i=0;i<=100;i++) for(j=0;j<=100;j++) mp[i][j]=tmp[i][j];
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	int cs,cn=1,i,j,k;
	int x1,y1,x2,y2;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d",&n);
		memset(mp,0,sizeof(mp));
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			x1--;y1--;x2--;y2--;
			for(j=min(x1,x2);j<=max(x1,x2);j++)
			{
				for(k=min(y1,y2);k<=max(y1,y2);k++) mp[j][k] = 1;
			}
		}
		int ans = 0;
		while(!over())
		{
			ans++;
			change();
		}
		printf("Case #%d: %d\n",cn++,ans);
	}
	return 0;
}

