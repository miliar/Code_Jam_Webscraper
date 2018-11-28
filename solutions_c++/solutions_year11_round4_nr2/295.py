// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#define N 510
using namespace std;
typedef long long LL;
int n,m,d,w[N][N];
void input() {
	scanf("%d%d%d",&n,&m,&d);
	for ( int i=1; i<=n; i++ )
		for ( int j=1; j<=m; j++ )
			scanf("%1d",&w[i][j]);
	for ( int i=1; i<=n; i++ )
		for ( int j=1; j<=m; j++ )
			w[i][j]+=d;
}
LL s[N][N];
void build() {
	memset(s,0,sizeof(s));
	for ( int i=1; i<=n; i++ )
		for ( int j=1; j<=m; j++ )
			s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+w[i][j];
}
LL get( int x1, int y1, int x2, int y2 ) {
	if ( x1>x2 || y1>y2 ) return 0;
	return s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1];
}
int cal( int x1, int y1, int x2, int y2, int tmt ) {
	int ret=0;
	LL Ls=0,Rs=0,Us=0,Ds=0,dis=1;
	while ( x1>=1 && x2<=n && y1>=1 && y2<=m ) {
		Ls+=dis*get(x1+1,y1,x2-1,y1);
		Rs+=dis*get(x1+1,y2,x2-1,y2);
		Us+=dis*get(x1,y1+1,x1,y2-1);
		Ds+=dis*get(x2,y1+1,x2,y2-1);	
		if ( Ls==Rs && Us==Ds ) ret=(x2-x1+1);
		Ls+=dis*(w[x1][y1]+w[x2][y1]);
		Rs+=dis*(w[x1][y2]+w[x2][y2]);
		Us+=dis*(w[x1][y1]+w[x1][y2]);
		Ds+=dis*(w[x2][y1]+w[x2][y2]);
		dis+=tmt;
		x1--; x2++;
		y1--; y2++;
	}
	return ret;
}
void solve() {
	static int cas=0;
	int ans=0,i,j;
	for ( i=1; i<=n; i++ )
		for ( j=1; j<=m; j++ ) {
			ans=max(ans,cal(i,j,i+1,j+1,2));
			ans=max(ans,cal(i,j,i+2,j+2,1));
		}
	if ( ans<3 ) printf("Case #%d: IMPOSSIBLE\n",++cas);
	else printf("Case #%d: %d\n",++cas,ans);
}
const double eps=1e-9;
bool eq( double a, double b ) { return fabs(a-b)<eps; }
bool chk( int x, int y, int L ) {
	double s1=0,s2=0,cx=x+(L-1)/2.0,cy=y+(L-1)/2.0;
	//printf("==========%g,%g\n",cx,cy);
	for ( int i=x; i<x+L; i++ )
		for ( int j=y; j<y+L; j++ ) {
			if ( (i==x||i==x+L-1) && (j==y||j==y+L-1) ) continue;
			s1+=(i-cx)*w[i][j];
			s2+=(j-cy)*w[i][j];
		}
	return eq(s1,0) && eq(s2,0);
}
void slow_solve() {
	static int cas=0;
	int ans=0;
	for ( int i=1; i<=n; i++ )
		for ( int j=1; j<=m; j++ )
			for ( int k=ans; i+k-1<=n && j+k-1<=m; k++ )
				if ( chk(i,j,k) ) {
					ans=k;
					//printf("%d,%d: %d\n",i,j,k);
				}
	if ( ans<3 ) printf("Case #%d: IMPOSSIBLE\n",++cas);
	else printf("Case #%d: %d\n",++cas,ans);
}
int main()
{
	int t;
	scanf("%d",&t);
	while ( t-- ) {
		input();
		build();
		//solve();
		slow_solve();
	}
	return 0;
}
