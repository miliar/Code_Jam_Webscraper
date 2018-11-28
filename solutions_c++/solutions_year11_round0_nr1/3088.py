#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector <char> turn;
vector <int> OG;
vector <int> BG;

int main() {
	freopen( "A-large.out", "w", stdout );
	int TC;
	cin >> TC;

	for( int TCC=1; TCC<=TC; TCC++ ) {
		turn.clear();
		OG.clear();
		BG.clear();
		int N;
		cin >> N;

		for( int i=0; i<N; i++ ) {
			char C;
			int WG;
			cin >> C >> WG;
			if( C == 'O' ) {
				turn.push_back( C );
				OG.push_back( WG );
			}
			if( C == 'B' ) {
				turn.push_back( C );
				BG.push_back( WG );
			}
		}

		int O = 1;
		int B = 1;
		int ret = 0;
		int TP = 0;
		int OP = 0;
		int BP = 0;

		bool OC = false;
		bool BC = false;

		while( TP < (int)turn.size() ) {
			if( turn[TP] == 'O' ) {
				if( O == OG[OP] ) {
					OP++;
					TP++;
				}
				else {
					if( O > OG[OP] ) O--;
					else O++;
				}
				if( B > BG[BP] ) B--;
				else if( B < BG[BP] ) B++;
			}
			else if( turn[TP] == 'B' ) {
				if( B == BG[BP] ) {
					BP++;
					TP++;
				}
				else {
					if( B > BG[BP] ) B--;
					else B++;
				}
				if( O > OG[OP] ) O--;
				else if( O < OG[OP] ) O++;
			}

			ret++;
		}
		cout << "Case #" << TCC << ": " << ret << endl;
	}
}
