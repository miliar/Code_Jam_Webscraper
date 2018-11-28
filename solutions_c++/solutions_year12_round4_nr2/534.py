#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn = 10005;
struct node
{
	int x, y;
}a[maxn];
struct node1
{
	int i,r;
}r[maxn];
void dfs( int x1, int y1, int x2, int y2, int n )
{
	int x = x1;
	int y = y1;
	int xx, yy;
	int xxx,yyy;
	int t = 0;
		a[n-t].x = x;
		a[n-t].y = y;
		x = x1 + r[n-t].r*2;
		y = y1 + r[n-t].r*2;
		xx = x;
		yy = y;
		t++;
		while ( n - t >= 0 && x <= x2 )
		{
			a[r[n-t].i].x = x;
			a[r[n-t].i].y = y;
			x = x + r[n-t].r*2;
			t++;
		}
		while ( n - t >= 0 &&  y <= y2 )
		{
			a[r[n-t].i].x = xx;
			a[r[n-t].i].y = y;
			y = y + r[n-t].r*2;
			t++;
		}
		if ( n -t < 0 ) return;
		dfs( xx + r[n-t].r, yy + r[n-t].r, x2, y2, n - t);
}
bool cmp( node1 x, node1 y )
{
	return x.r < y.r;
}
int main()
{
	int cas, ca = 0;
	int w, l, n;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		scanf( "%d %d %d", &n, &w, &l );
		for ( int i = 0; i < n; i++ )
		{
			scanf( "%d", &r[i].r );
			r[i].i = i;
		}
		sort( r, r + n, cmp );
		dfs( 0, 0, w, l, n-1 );
		printf("Case #%d: ", ++ca );
		for ( int i = 0; i < n; i++ )
		{
			printf( "%d.0 %d.0", a[i].x, a[i].y );
			if ( i == n - 1 ) printf("\n");
			else printf(" ");
		}
	}
	return 0;
} 