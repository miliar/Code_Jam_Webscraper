#include<cstdio>
#include<queue>
using namespace std;
typedef pair<int,int> pii;
typedef pair< int , pii > piii;

priority_queue< piii > S;
int h,n,m;
int U[110][110], L[110][110];
int ans[110][110];
bool vst[110][110];

inline int ab(int x){ if( x > 0 ) return x; return -x; }

void f()
{
	scanf("%d%d%d",&h,&n,&m);
	for(int c=1;c<=n;c++) for(int d=1;d<=m;d++) scanf("%d",&U[c][d]);
	for(int c=1;c<=n;c++) for(int d=1;d<=m;d++) scanf("%d",&L[c][d]);
	for(int c=0;c<110;c++) for(int d=0;d<110;d++) ans[c][d] = -10000000;
	for(int c=0;c<110;c++) for(int d=0;d<110;d++) vst[c][d] = false;
	ans[1][1] = h;
	S.push( piii( 0 , pii(1,1) ) );
	while( !S.empty() )
	{
		int x = S.top().second.first, y = S.top().second.second;
		S.pop();
		if( vst[x][y] ) continue;
		vst[x][y] = true;
		for(int c=-1;c<=1;c++) for(int d=-1;d<=1;d++) if( ab(c) != ab(d) )
		{
			int p = x+c, q = y+d;
			if( p < 1 or p > n or q < 1 or q > m ) continue;
			if( min( U[x][y] , U[p][q] ) - max( L[x][y] , L[p][q] ) < 50 ) continue;
			int r = ans[x][y];
			r = min( r , U[p][q] - 50 );
			if( r == h );
			else if( r - L[x][y] < 20 ) r -= 100;
			else r -= 10;
			ans[p][q] = max( ans[p][q] , r );
			S.push( piii( ans[p][q] , pii(p,q) ) );
		}
	}
	//for(int c=1;c<=n;c++) { for(int d=1;d<=m;d++) printf("%d ",ans[n][m]); printf("\n"); }
	ans[n][m] = h - ans[n][m];
	printf("%d.%d\n",ans[n][m]/10,ans[n][m]%10);
}

int main()
{
	freopen("22.in","r",stdin);
	freopen("22.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		f();
	}
}
