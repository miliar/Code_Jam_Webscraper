#include <stdio.h>
#include <algorithm>

using namespace std;

#define NMAX 100002
#define INF 0x3f3f3f3f

int din[NMAX][2];
int ST[NMAX],CH[NMAX];

void solve()
{
	int i,j,k,x,y,n,v;
	
	memset(din,0,sizeof(din));
	scanf("%d %d",&n,&v);

	for (i=1;i<=(n-1)/2;i++)
	{
		scanf("%d %d",&x,&y);
		ST[i]=x;CH[i]=y;
	}

	for (i=(n+1)/2;i<=n;i++)
	{
		scanf("%d",&x);
		din[i][x]=0;
		din[i][!x]=INF;
	}

	for (i=(n-1)/2;i;i--)
	{
	//0 pe nodul i

	din[i][0]=INF;
	if (ST[i]==0) din[i][0]=min(din[i][0], din[i*2][0]+din[i*2+1][0] );
	if (ST[i]==1) din[i][0]=min(din[i][0], min( din[i*2][0]+din[i*2+1][0], min( din[i*2][1]+din[i*2+1][0], din[i*2][0]+din[i*2+1][1]) ) );

	if (CH[i]) 
		if (ST[i]==0) din[i][0]=min(din[i][0], min( din[i*2][0]+din[i*2+1][0], min( din[i*2][1]+din[i*2+1][0], din[i*2][0]+din[i*2+1][1]) ) +1 );
			else  din[i][0]=min(din[i][0], din[i*2][0]+din[i*2+1][0]+1 );
	//1 pe nodul i
 
 	din[i][1]=INF;
	if (ST[i]==0) din[i][1]=min(din[i][1], min( din[i*2][1]+din[i*2+1][1], min( din[i*2][0]+din[i*2+1][1], din[i*2][1]+din[i*2+1][0] ) ) );
	if (ST[i]==1) din[i][1]=min(din[i][1], din[i*2][1]+din[i*2+1][1]);

	if (CH[i]) 
		if (ST[i]==0) din[i][1]=min(din[i][1], din[i*2][1]+din[i*2+1][1]+1 );
			else  din[i][1]=min(din[i][1], min( din[i*2][1]+din[i*2+1][1], min( din[i*2][0]+din[i*2+1][1], din[i*2][1]+din[i*2+1][0] ) )+1 );
	}
        
	if (din[1][v]==INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",din[1][v]);
}

int main()
{
	freopen("tree.in","r",stdin);
	freopen("tree.out","w",stdout);

	int T,i;
	
	for (scanf("%d",&T),i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
