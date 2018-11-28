#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)
#define MOD 10007

int N,H,W,R,d[100][100];
bool rc[100][100];

int main()
{
	freopen("D.in","r",stdin);freopen("D.out","w",stdout);
	scanf("%d",&N);
	REP(C,N)
	{
		memset(rc,0,sizeof(rc));
		scanf("%d%d%d",&H,&W,&R);
		while(R--)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			x--;y--;
			rc[x][y]=1;
		}
		memset(d,0,sizeof(d));
		d[0][0]=1;
		REP(i,H)REP(j,W)if(!rc[i][j])
		{
			if(i+1<H&&j+2<W)
			{
				d[i+1][j+2]+=d[i][j];
				if(d[i+1][j+2]>=MOD)d[i+1][j+2]-=MOD;
			}
			if(i+2<H&&j+1<W)
			{
				d[i+2][j+1]+=d[i][j];
				if(d[i+2][j+1]>=MOD)d[i+2][j+1]-=MOD;
			}
		}
		printf("Case #%d: %d\n",C+1,d[H-1][W-1]);
	}
	return 0;
}
