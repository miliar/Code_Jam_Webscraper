#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)


int main(){

	int tn, n;
	freopen("out", "w", stdout);
	freopen("largein", "r", stdin);

	cin >> tn;

	int cn = 1;
	while( tn-- ){
		printf("Case #%d:\n", cn++);
		cin >> n;
		int kaa, kab, uaa, uab;
		int kba, kbb, uba, ubb;

		VPII NB;

		kba = kaa = 234234234;
		kbb = kab = -1;

		uaa = uba = 0;
		uab = ubb = 234234234;
		
		REP( i, n ){
			string s;
			int a, b;
			cin >> a >> b >> s;

			if( s == "BIRD" ){
				kaa = min( a, kaa );
				kba = min( b, kba );
				kab = max( a, kab );
				kbb = max( b, kbb );
			}
			else{ cin >> s; NB.PB( MP( a, b ) ); }
		}
		REP( i, SZ(NB) ){
			int a, b;
			a = NB[i].ST;
			b = NB[i].ND;
			if( kaa <= a && a <= kab ){
				if( b < kba ) uba = max( uba, b );
				else if( kbb < b ) ubb = min( ubb, b );
			}
			else if( kba <= b && b <= kbb ){
				if( a < kaa ) uaa = max( uaa, a );
				else if( a > kab ) uab = min( uab, a );
			}
		}
		//cout << kaa << " " << kab << " " << uaa << " " << uab << endl;
		//cout << kba << " " << kbb << " " << uba << " " << ubb << endl;
		cin >> n;
		while( n-- ){
			int a, b;
			cin >> a >> b;
			if( kaa <= a && a <= kab &&
				kba <= b && b <= kbb ){
				printf("BIRD\n");
			}
			else if( uaa < a && a < uab && uba < b && b < ubb ){


				REP( i, SZ(NB) ){
					int aa, bb;
					aa = NB[i].ST;
					bb = NB[i].ND;

					if( aa < kaa && aa < a ) continue;
					if( aa > kab && aa > a ) continue;
					if( bb < kba && bb < b ) continue;
					if( bb > kbb && bb > b ) continue;

					printf("NOT BIRD\n");
					goto next;

				}
				printf("UNKNOWN\n");

			}
			else printf("NOT BIRD\n");
next:;
		}

	}

		

}