#include <cstdio>
#include <algorithm>
#include <climits>
using namespace std;
const int maxn=110;
const int mx[4]={0,-1,1,0};
const int my[4]={-1,0,0,1};
int h,w;
int m[maxn][maxn];
pair<int,int> f[maxn][maxn];
char c[maxn][maxn];
void init()
{
	scanf("%d%d",&h,&w);
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
		{
			scanf("%d",&m[i][j]);
			f[i][j]=make_pair(i,j);
		}
}
pair<int,int> find(pair<int,int> a)
{
	if(f[a.first][a.second]==a) return a;
	return f[a.first][a.second]=find(f[a.first][a.second]);
}
void combine(pair<int,int> a,pair<int,int> b)
{
	pair<int,int> r=find(f[a.first][a.second]),p=find(f[b.first][b.second]);
	f[r.first][r.second]=p;
}
void solve()
{
	memset(c,0,sizeof(c));
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
		{
			int d=-1,l=INT_MAX;
			for(int k=0;k<4;k++)
			{
				int x=j+mx[k],y=i+my[k];
				if(x<0||x>=w||y<0||y>=h) continue;
				if(l>m[y][x]&&m[y][x]<m[i][j])
				{
					l=m[y][x];
					d=k;
				}
			}
			if(d>=0)
			{
				combine(make_pair(i,j),make_pair(i+my[d],j+mx[d]));
			}
		}
	char u='a';
	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)
		{
			pair<int,int> r=find(make_pair(i,j));
			if(c[r.first][r.second])
			{
				c[i][j]=c[r.first][r.second];
			}
			else
			{
				c[i][j]=c[r.first][r.second]=u++;
			}
			putchar(c[i][j]);
			//printf("%1d,%1d ",r.first,r.second);
			if(j==w-1) putchar('\n'); else putchar(' ');
		}
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
