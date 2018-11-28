#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn=100;
char s[maxn][maxn];
int n,k;
void init()
{
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++) scanf("%s",s[i]);
}
void solve()
{
	for(int i=0;i<n;i++)
	{
		for(int j=n-1;j>=0;j--)
		{
			if(s[i][j]!='.') continue;
			int z;
			for(z=j;z>=0&&s[i][z]=='.';z--);
			if(z>=0&&j!=z) swap(s[i][j],s[i][z]);
		}
		//printf("  %s\n",s[i]);
	}
	const int mx[4]={1,0,1,1},my[4]={0,1,1,-1};
	bool r=false,b=false;
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			for(int d=0;d<4;d++)
			{
				int rc=0,bc=0;
				for(int z=0;z<k;z++)
				{
					int y=i+my[d]*z,x=j+mx[d]*z;
					if(y>=n||x>=n||x<0||y<0) break;
					if(s[y][x]=='R') rc++;
					else if(s[y][x]=='B') bc++;
					else break;
				}
				if(rc>=k) {r=true;/*printf("R %d,%d,%d,%d\n",i,j,d,rc);*/}
				if(bc>=k) {b=true;/*printf("B %d,%d,%d,%d\n",i,j,d,rc);*/}
			}
			//printf("%d,%d: %d,%d\n",i,j,r,b);
		}
	if(r&&b) puts("Both");
	else if(r&&!b) puts("Red");
	else if(!r&&b) puts("Blue");
	else puts("Neither");
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
