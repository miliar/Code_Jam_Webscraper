#include <cstdio>
#include <algorithm>
#include <vector>
#define MOD 10007

using namespace std;

vector < pair <int,int> > rocks;
int W, H;
int memo[128][128];

int broj_nacina( int x, int y ){
	if( x == 0 && y == 0 ) return 1;
	if( x < 0 || y < 0 ) return 0;

	int &sol = memo[x][y];
	if( sol != -1 ) return sol;

	return sol = (broj_nacina(x-1,y-2)+broj_nacina(x-2,y-1))%MOD;
}

int main(){
	int tp, r;
	scanf( "%d", &tp );
	memset( memo, -1, sizeof memo );

	for( int tt = 1; tt <= tp; ++tt ){
		int sol = 0;
		scanf( "%d%d", &W, &H );
		scanf( "%d", &r );
		rocks.resize(r);
		for( int i = 0; i < r; ++i ) scanf( "%d%d", &rocks[i].first, &rocks[i].second );
		sort( rocks.begin(), rocks.end() );

		for( int mask = 0; mask < (1<<r); ++mask ){
			int sx = 1, sy = 1, bc = 0, t = 1;

			for( int i = 0; i < r; ++i ){
				if( (mask & (1<<i)) != 0 ){
					t = (t*broj_nacina( rocks[i].first-sx, rocks[i].second-sy ))%MOD;
					sx = rocks[i].first; sy = rocks[i].second;
					++bc;
				}
			}
			t = (t*broj_nacina( W-sx, H-sy ))%MOD;
			if( bc % 2 == 0 ) sol = (sol+t)%MOD;
			else sol = (sol-t+MOD)%MOD;	
		}

		printf( "Case #%d: %d\n", tt, sol );
	}
	

	return 0;
}
