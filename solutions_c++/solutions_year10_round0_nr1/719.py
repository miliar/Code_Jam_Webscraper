#include <iostream>

using namespace std;

void solve( int __r )
{
    long long n, k, t; cin >> n >> k;
    
    t = 1 << n;
    
    cout << "Case #" << __r << ": ";
    
    if( k % t == t - 1 ) cout << "ON";
    else cout << "OFF";

    cout << endl;
}

int main( void )
{
    int __t; cin >> __t;
    for( int i = 1; i <= __t; ++i )
	solve( i );
}
