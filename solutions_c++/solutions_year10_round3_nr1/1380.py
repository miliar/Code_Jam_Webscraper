#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

const double eps = 1e-8;


inline int sgn( double x )
{ return x < -eps ? -1 : x > eps; }


struct xv {
    double x, y; xv() { }
};

double crs( xv p0, xv p1, xv p2 )
{ return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y); }

double dot( xv p0, xv p1, xv p2 )
{ return (p1.x-p0.x)*(p2.x-p0.x)+(p1.y-p0.y)*(p2.y-p0.y); }

int pt_sg( xv pt, xv p1, xv p2 )
{ return sgn(crs(pt,p1,p2))==0 && sgn(dot(pt,p1,p2))<=0; }

int lns_int( xv p1, xv p2, xv p3, xv p4, xv &cp )
{
    double u = crs( p1,p2,p3 ), v = crs( p2,p1,p4 );
    if( sgn( u + v ) )
    {
	cp.x = ( p3.x*v + p4.x*u ) / ( v + u );
	cp.y = ( p3.y*v + p4.y*u ) / ( v + u );
	return 1;
    }
    return 0;
}


int sgs_int( xv p1, xv p2, xv p3, xv p4, xv &cp )
{
    return lns_int( p1,p2,p3,p4,cp )
	&& pt_sg( cp,p1,p2 ) && pt_sg( cp,p3,p4 );
}


const int maxn = 2000;

xv a[ maxn ], b[ maxn ], tp;

void solve( int __r )
{
    cout << "Case #" << __r << ": ";
    int n;  cin >> n;
    for( int i = 0; i < n; ++i )
    {
	a[i].x =   0;  cin >> a[i].y;
	b[i].x = 100;  cin >> b[i].y;
    }

    int cnt = 0;
    for( int i = 0; i < n-1; ++i )
	for( int j = i+1; j < n; ++j )
	    cnt += sgs_int( a[i],b[i],a[j],b[j], tp );

    cout << cnt << endl;
}

int main( void )
{
    int __t; cin >> __t;
    for( int i = 1; i <= __t; ++i )
	solve( i );
    return 0;
}





