#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct node
{
	double x, y;
}L[101], U[101], t;
typedef struct node N;

double calc ( N a, N b, double p )
{
	return ( p - a.x ) * (b.y - a.y) / (b.x - a.x) + a.y;
}

double find ( int i, int j, double l, double r, double pl, double s )
{
	double x, t, p = l;
	
	while ( l < r - 1e-7 )
	{
		x = ( l + r ) * 0.5;
		t = ( calc(U[j-1],U[j],x) - calc(L[i-1],L[i],x) + pl ) *
			( x - p ) * 0.5;
		if ( t < s + 1e-7 )
			l = x;
		else r = x;
	}
	return l;
}

int main ( )
{
	freopen ( "i.in", "r", stdin );
	freopen ( "o.out", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d:\n", o );
		
		int w, l, u, g;
		scanf ( "%d%d%d%d", &w, &l, &u, &g );
		
		int i;
		for ( i = 1; i <= l; ++i )
			scanf ( "%lf%lf", &L[i].x, &L[i].y );
		for ( i = 1; i <= u; ++i )
			scanf ( "%lf%lf", &U[i].x, &U[i].y );
		
		int j;
		double s = 0, p = 0, pl = U[1].y - L[1].y, te;
		for ( i = 2, j = 2; i <= l && j <= u; )
		{
			te = pl;
			if ( L[i].x < U[j].x )
				s += ((pl = calc(U[j-1],U[j],L[i].x)-L[i].y) +te) *
					(L[i].x-p) * 0.5, p = L[i].x, ++i;
			else s += ((pl = U[j].y-calc(L[i-1],L[i],U[j].x)) +te) *
					(U[j].x-p) * 0.5, p = U[j].x, ++j;
		}
		
		int k = 0;
		s /= g;
		p = 0, pl = U[1].y - L[1].y;
		double ts = 0, tt;
		for ( i = 2, j = 2; i <= l && j <= u; )
		{
			te = pl;
			if ( L[i].x < U[j].x )
			{
				tt = ((pl = calc(U[j-1],U[j],L[i].x)-L[i].y) +te) *
					(L[i].x-p) * 0.5;
				if ( ts + tt > s - 1e-7 )
				{
					printf ( "%.6lf\n",p=find(i,j,p,L[i].x,te,s-ts));
					pl = calc ( U[j-1], U[j], p ) - 
						 calc ( L[i-1], L[i], p );
					ts = 0;
					++k;
					if ( k == g - 1 ) break;
				}
				else
				{
					ts += tt;
					p = L[i].x; ++i;
				}
			}
			else
			{
				tt = ((pl = U[j].y-calc(L[i-1],L[i],U[j].x)) +te) *
					(U[j].x-p) * 0.5;
				if ( ts + tt > s - 1e-7 )
				{
					printf ( "%.6lf\n",p=find(i,j,p,U[j].x,te,s-ts));
					pl = calc ( U[j-1], U[j], p ) - 
						 calc ( L[i-1], L[i], p );
					ts = 0;
					++k;
					if ( k == g - 1 ) break;
				}
				else
				{
					ts += tt;
					p = U[j].x; ++j;
				}
			}
		}
	}
	return 0;
}
