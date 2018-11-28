#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )
#define dp(i,l,r) for ( int i=(int)(l); i>=(int)(r); --i )

const int mn=2000;

typedef long long LL;

int T,n,m;
LL W,L;
LL x[mn],y[mn];
int r[mn];
int sa[mn],R[mn];

inline bool cmp( const int &a , const int &b )
{
	return r[a]>r[b] ;
} // 0 - 0

inline bool dis( LL x, LL y, LL r)
{
    x *= x; y *= y; r *= r;
    x += y;
    return x >= r;
}

inline bool check(int x2, int y2, int id)
{
    if (x2 > W || y2 > L) return 0;
    rp( i,1,id-1 )
    {
        int xx = x[i], yy = y[i];
        if (!dis(xx - x2, yy - y2, r[i] + r[id])) return 0;
    }
    return 1;
}

inline bool ok(int a, int b)
{
    int xx, yy;
    xx = x[a]; yy = y[a];
    if (check(xx + r[a] + r[b], yy, b))
    {
        x[b] = xx + r[a] + r[b];
        y[b] = yy;
        return 1;
    }
    if (check(xx, yy + r[a] + r[b], b))
    {
        x[b] = xx;
        y[b] = yy + r[a] + r[b];
        return 1;
    }
    return 0;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("BL.txt","w",stdout);
	cin >> T ;
	rp( Test,1,T )
	{
		cin >> n >> W >> L ;
		memset( x , 0 , sizeof x ); 
		memset( y , 0 , sizeof y );
		rp( i,1,n ) cin >> r[i] ;
		rp( i,1,n ) sa[i]=i;  
		sort( sa+1 , sa+1+n , cmp );
		rp( i,1,n ) R[i]=r[i];
		rp( i,1,n ) r[i]=R[sa[i]];
		rp( i,1,n ) R[sa[i]]=i;
		x[1]=0 , y[1]=0;
		rp( i,2,n ) 
		{
			rp( j,1,i-1 ) if ( ok( j,i ) ) break;
		} // 0 - 0
		cout << "Case #" << Test << ":" ;
		rp( i,1,n )
		{        
			cout << " " << x[R[i]] << " " << y[R[i]] ;
		}
		cout << endl;
	} // 0 - 0 
} // 0 - 0