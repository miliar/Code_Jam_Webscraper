#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )

const int mn=20000;

int T,maxx,n;
int d[mn],l[mn],v[mn];

inline bool run()
{
	memset( v , 0 , sizeof v );
	v[1]=min( d[1] , l[1] );
	rp( i,2,n ) rp( j,1,i-1 )
	{
		if ( d[i]-d[j]<=min( v[j] , l[j] ) ) v[i]=max( v[i] , min( d[i]-d[j] , l[i] ) );
	} // 0 - 0
	rp( i,1,n ) if ( v[i] )
	{
		if ( d[i]-v[i]<=maxx && d[i]+v[i]>=maxx ) return 1;
	} // 0 - 0
	return 0;
} // 0 - 0

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("AL.txt","w",stdout);
	cin >> T; 
	rp( Test,1,T )
	{
		cin >> n;
		rp( i,1,n ) cin >> d[i] >> l[i] ;
		cin >> maxx;
		cout << "Case #" << Test << ": " ;
		bool ok=run();
		if ( ok ) cout << "YES" << endl; else cout << "NO" << endl;
	} // 0 - 0
} // 0 - 0