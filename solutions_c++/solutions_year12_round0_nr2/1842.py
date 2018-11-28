#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )

int n,s,p,t;
int test;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("BL.txt","w",stdout);
	cin >> test ;
	rp( T,1,test )
	{
		cin >> n >> s >> p ;  p*=3;
		int ans=0;
		rp( i,1,n ) 
		{
			cin >> t ;
			if ( t==0 ) { if ( p==0 ) ++ans; continue; }
			if ( t+2>=p ) { ++ans; continue; }
			if ( s==0 ) continue;
			if ( t+4>=p ) { ++ans; --s; continue; }
		} // 0 - 0
		cout << "Case #" << T << ": " << ans << endl;
	} // 0 - 0
} // 0 - 0