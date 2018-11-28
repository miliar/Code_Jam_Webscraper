#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))

#define all(a) a.begin(),a.end()
#define pb push_back

#define i64 long long
#define pi (2.0*acos(0.0))
#define eps (1e-9)

typedef pair< int , int >  pii;
int eg[ 10 ][ 10 ], n;

bool okay( int mask )
{
	if( mask == 15 )
		mask = mask;
	vector <int> now, ready;
	int i, j;
	for(i = 0; i < n ; i ++ )
		if( ( 1 << i ) & mask )
			now.push_back( i );
	sort( now.begin(), now.end() );
	if( now.size() < 3 ) 
		return false;
	now.push_back( now[ 0 ] );
	for(i = 0; i < now.size() - 1; i ++ ) 
		if( eg[ now[ i ] ][ now[ i + 1 ] ] == 0 )
			return false;
	for(i = 0; i < now.size() - 1; i ++ )
		for(j = i + 2; j < now.size() - 1; j ++ )
		{
			if( i == 0 && j ==  now.size() - 2 ) continue;
			if( eg[ now[ i ] ][ now[ j ] ] ) return false;
		}
	return true;
}
int col[ 10 ];
vector<int> st;
bool chk(int lm)
{
	int i, j;
	for(i = 0; i < st.size(); i ++ )
	{
		int now = 0;
		for(j = 0; j < n ; j ++ )
			if( (1 << j ) & st[ i ] )
				now |= ( 1 << col[ j ] );
		if( now != ( 1 << lm ) - 1 ) return false;
	}
	return true;

}
bool succ( int node, int lm )
{
	if( node == n ){
		if ( chk(lm) ) return true;
		return false;
	}
	int i;
	for(i = 0; i < lm ; i ++ )
	{
		col[ node ] = i;
		if( succ( node + 1, lm ) )
			return true;
	}
	return false;
}
int main(){
	freopen("aa.txt","r",stdin);
	freopen("C-large.ans","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{		
		printf("Case #%d: ", cs ++);

		CLR( eg );
		int m, i, k;
		cin >> n >> m;
		
		vector <int> U;
		for(i = 0; i < n - 1 ; i ++ ) eg[ i ][ i + 1 ] = eg[ i + 1 ][ i ] = 1;
		eg[ 0 ][ n - 1 ] = eg[ n - 1 ][ 0 ] = 1;
		for(i = 0; i < m ; i ++ )
		{
			cin >> k;
			k --;
			U.push_back( k );
		}
		for(i = 0; i < m ; i ++ )
		{
			cin >> k;
			k --;
			eg[ U[ i ] ][ k ] = eg[ k ][ U[ i ] ] = 1;
		}
		st.clear();
		int done = 0;
		for(i = 1; i < ( 1 << n ); i ++ )
				if ( okay ( i ) )				
					st.push_back( i );
		int lm = 1;
		while( succ( 0, lm ) ) 
			lm ++;
		succ( 0, lm - 1 );
		cout << lm - 1 << endl;
		cout << col[ 0 ] + 1;
		for(i = 1; i < n; i ++ )
			cout <<" "<<col[ i ] + 1;
		cout << endl;
	}

	return 0;
}