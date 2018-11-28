#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;
int INF = 100000000;
vector<bool> ch;
vector<int> val;
int v;

bool Read(){
	int n;
	scanf("%d%d", &n, &v );
	val.assign( n+1, 0 );
	int isch;
	ch.clear();
	ch.push_back( false );
	for(int i = 1; i <= (n-1)/2; ++i){
		scanf("%d%d", &val[i], &isch );
		if( isch == 1 )ch.push_back( true ); else ch.push_back( false );
	}
	for(int i = (n-1)/2 + 1; i <= n; ++i){
		scanf( "%d", &val[i] );
	}
	return true;
}


int rec( int k, int t ){
	if( k > (val.size() - 1) / 2 ){
		if( val[k] == t ) return 0;
		return INF;
	}
	int res = INF;
	int l1, l0, r1, r0;
	l1 = rec( 2*k, 1 );
	l0 = rec( 2*k, 0 );
	r0 = rec( 2*k + 1, 0 );
	r1 = rec( 2*k + 1, 1 );

		if( val[k] == 1 ){
			if( t == 0 ){
				res = min( res, l0 + r0 );
				res = min( res, l0 + r1 );
				res = min( res, l1 + r0 );
			}
			if( t == 1 ){
				res = min( res, l1 + r1 );
			}
		}
		if( val[k] == 0 ){
			if( t == 0 ){
				res = min( res, l0 + r0 );
			}
			if( t == 1 ){
				res = min( res, l0 + r1 );
				res = min( res, l1 + r0 );
				res = min( res, l1 + r1 );
			}
			
		}
	if( ch[k] ){
		if( val[k] == 0 ){
			if( t == 0 ){
				res = min( res, l0 + r0 + 1 );
				res = min( res, l0 + r1 + 1);
				res = min( res, l1 + r0 + 1);
			}
			if( t == 1 ){
				res = min( res, l1 + r1 + 1);
			}
		}
		if( val[k] == 1 ){
			if( t == 0 ){
				res = min( res, l0 + r0 + 1 );
			}
			if( t == 1 ){
				res = min( res, l0 + r1 + 1);
				res = min( res, l1 + r0 + 1);
				res = min( res, l1 + r1 + 1);
			}
		}
	}
	return res;
}

int Solve(){
	return rec( 1, v );
}

void Write( int num, int ans ){
	if( ans != INF )
	printf( "Case #%d: %d\n", num, ans ); else
	printf( "Case #%d: IMPOSSIBLE\n", num );
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	scanf( "%d", &n );
	for(int i = 0; i < n; ++i){
		Read();
		Write( i+1, Solve() );
	}

	return 0;
}