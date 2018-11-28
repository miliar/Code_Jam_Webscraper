#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> kreceA, dolaziB, kreceB, dolaziA;

int main(){
	int tt, T;
	scanf( "%d", &tt );

	for( int tp = 1; tp <= tt; ++tp ){
		int na, nb;
		scanf( "%d", &T );
		scanf( "%d%d", &na, &nb );

		kreceA.clear(); dolaziB.clear(); kreceB.clear(); dolaziA.clear();

		for( int i = 0; i < na; ++i ){
			int aa, bb, cc, dd;
			scanf( "%d:%d %d:%d", &aa, &bb, &cc, &dd );

			kreceA.push_back( aa*60+bb );
			dolaziB.push_back( cc*60+dd+T );
		}
		for( int i = 0; i < nb; ++i ){
			int aa, bb, cc, dd;
			scanf( "%d:%d %d:%d", &aa, &bb, &cc, &dd );

			kreceB.push_back( aa*60+bb );
			dolaziA.push_back( cc*60+dd+T );
		}

		sort( kreceA.begin(), kreceA.end() );
		sort( dolaziA.begin(), dolaziA.end() );

		int solA = na, solB = nb;

		for( int k = 0, d = 0; k < kreceA.size() && d < dolaziA.size(); ++k ){
			if( kreceA[k] >= dolaziA[d] ){
				++d; --solA;
			}
		}
		sort( kreceB.begin(), kreceB.end() );
		sort( dolaziB.begin(), dolaziB.end() );
		for( int k = 0, d = 0; k < kreceB.size() && d < dolaziB.size(); ++k ){
			if( kreceB[k] >= dolaziB[d] ){
				++d; --solB;
			}
		}


		printf( "Case #%d: %d %d\n", tp, solA, solB );
	}

	return 0;
}
