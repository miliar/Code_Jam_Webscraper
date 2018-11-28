#include <cstdio>
#include <vector>

using namespace std;

vector < vector < pair<int,int> > > customers;
vector <int> jedan;
vector <int> sol;
int n, m;

void load(){
	scanf( "%d%d", &n, &m );

	customers.resize(m);
	jedan.resize(m);
	sol.resize(n);

	for( int i = 0; i < m; ++i ){
		int t;
		scanf( "%d", &t );
		customers[i].resize(t);
		jedan[i] = -1;

		for( int k = 0; k < t; ++k ){
			scanf( "%d%d", &customers[i][k].first, &customers[i][k].second );
			if( customers[i][k].second == 1 ) jedan[i] = customers[i][k].first;
		}
	}
}

bool nepase( const vector < pair<int,int> > &kupac ){
	for( int i = 0; i < kupac.size(); ++i ){
		if( sol[kupac[i].first-1] == kupac[i].second ) return false;
	}
	return true;
}

void solve(){
	fill( sol.begin(), sol.end(), 0 );
	bool promjena;

	do{
		promjena = false;
		for( int i = 0; i < customers.size(); ++i ){
			if( nepase( customers[i] ) ){
				if( jedan[i] == -1 ) {
					sol[0] = -1;
					return;
				}
				sol[ jedan[i]-1 ] = 1;

				promjena = true;
				continue;
			}
		}
	}while( promjena );
}

int main(){
	int tp;
	scanf( "%d", &tp );

	for( int tt = 1; tt <= tp; ++tt ){
		load();
		solve();
		if( sol[0] == -1 ) printf( "Case #%d: IMPOSSIBLE\n", tt );
		else {
			printf( "Case #%d: ", tt );
			for( int i = 0; i < n; ++i ){
				printf( "%d ", sol[i] );
			}
			printf( "\n" );
		}
	}

	return 0;
}
