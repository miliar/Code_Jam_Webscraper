#include <iostream>
using namespace std;

double d, p[210];
int n, cn, ci, v[210];
int i;
double tmp, st, ed, ans;

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );

	scanf( "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		scanf( "%d %lf", &n, &d );
		for ( i = 0; i < n; i++ ) scanf( "%lf %d", &p[i], &v[i] );
		ans = 0;
		ed = p[0];
		for ( i = 0; i < n; i++ )
		{
			if ( p[i] < ed ) st = ed;
			else st = p[i];
			ed = st + d*(v[i]-1);
			tmp = (ed-p[i])/2.0;
			if ( tmp > ans ) ans = tmp;
			ed = ed+d;
		}
		printf( "Case #%d: %.2lf\n", ci, ans );
	}
}