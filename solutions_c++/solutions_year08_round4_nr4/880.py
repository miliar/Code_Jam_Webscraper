#include<cstdio>
#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

string s;
string res;
vector<int> v;
int k;

int calculate()
{
	int index = 0;
	int len = s.size();
	res = s;
	for( int j = 0; index < len; j += k )
		for( int i = 0; i < k; ++i )
			res[ index++ ] = s[ j + v[ i ] ];
	int ans = 1;
	//res = "aabcaabcaabc";
	for( int i = 1; i < res.size(); ++i )
		if( res[ i - 1 ] == res[ i ] );
		else ++ans;
	//if( res[ res.size() - 1 ] != res[ res.size() - 2 ] ) ++ans; 
	return ans;
}
int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin >> t;
	for( int test = 1; test <= t; ++test )
	{
		cin >> k >> s;
		v.resize( k );
		for( int i = 0; i < k; ++i )
			v[ i ] = i;
		int ans = 1 << 30;
		do{
			int a = calculate();
			if( a < ans ) 
				ans = a;
		}while( next_permutation( v.begin(), v.end() ) );
		printf( "Case #%d: %d\n", test, ans );
	}
	return 0;
}