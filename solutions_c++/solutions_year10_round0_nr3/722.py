#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

void solve( int __r )
{
    cout << "Case #" << __r << ": ";
    
    int r, k, n;  cin >> r >> k >> n;
    vector<int> que, it;
    for( int i = 0; i < n; ++i )
    {
	int x;  cin >> x;
	que.push_back( x );
    }
    
    it = que;

    vector<vector<int> > vi;
    vector<long long>    vr, vg;
    long long g = 0, Tg, Tt;

    vi.push_back( it );
    vr.push_back(  r );
    vg.push_back(  0 );
    
    while( r-- )
    {
	int i, p;
	for( i = 0, p = 0; i < n; ++i )
	{
	    if( p + it[i] > k ) break;
	    p += it[i];
	}
	if( i < n )rotate( it.begin(),it.begin()+i,it.end() );
	
	g += p;

	for( i = 0; i < vi.size( ); ++i )
	    if( vi[i] == it )
	    {
		Tg = g - vg[i];
		Tt = vr[i] - r; 
		break;
	    }


	if( i == vi.size( ) )  //failure
	{
	    vi.push_back( it );
	    vr.push_back(  r );
	    vg.push_back(  g );
	}
	else                      //hit
	{
	    break;
	}
    }

    if( r == -1 )
    {
	cout << g << endl;
	return;
    }

    long long rounds = r / Tt;

    g += rounds * Tg;
    r -= rounds * Tt;

    while( r-- )
    {
	int i, p;
	for( i = 0, p = 0; i < n; ++i )
	{
	    if( p + it[i] > k ) break;
	    p += it[i];
	}
	if( i < n )rotate( it.begin(),it.begin()+i,it.end() );
	g += p;
    }

    cout << g << endl;
}

int main( void )
{
    int __t;  cin >> __t;
    for( int i = 1; i <= __t; ++i )
	solve( i );
    return 0;
}

