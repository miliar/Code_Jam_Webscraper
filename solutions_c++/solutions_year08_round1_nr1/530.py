#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<set>
#include<algorithm>
#include<queue>

using namespace std;

#define LL long long

bool cmp( int a, int b )
{
	return b < a;	
}
int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin >> t;
	for( int test = 1; test <= t; ++test )
	{
		int n;
		cin >> n;
		vector<LL> v1( n ), v2( n );
		for( int i = 0; i < n; ++i )
			cin >> v1[ i ];
		for( int i = 0; i < n; ++i )
			cin >> v2[ i ];
		sort( v1.begin(), v1.end() );
		sort( v2.begin(), v2.end(), cmp );
		LL res = 0 ;
		for( int i = 0; i < n; ++i )
			res += ( v1[ i ] * v2[ i ] );
		cout << "Case #" << test << ": " << res <<endl;


	}
	return 0;
}