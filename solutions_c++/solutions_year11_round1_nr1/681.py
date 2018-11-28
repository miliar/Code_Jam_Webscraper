#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

string solve()
{
	__int64 n;
	int pd, pg;
	cin >> n >> pd >> pg;
	if( 100 == pg && 100 != pd ) return "Broken";
	if( 0 == pg && 0 != pd ) return "Broken";
	if( n >= 100 ) return "Possible";
	if( n >= 50 && (0 == pd%2) ) return "Possible";
	if( n >= 25 && (0 == pd%4) ) return "Possible";
	if( n >= 20 && (0 == pd%5) ) return "Possible";
	if( n >= 10 && (0 == pd%10) ) return "Possible";
	for( int d = 1; d <= n; ++d )
		if( 0 == (d * pd)%100 )
			return "Possible";
	return "Broken";
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	cin >> tests;
	for( int x = 1; x <= tests; ++x )
	{
		cout << "Case #" << x << ": " << solve() << endl;
	}
	return 0;
}