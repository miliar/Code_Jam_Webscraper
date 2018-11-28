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

string s, ss;
int k;
int p[16];

int main(){
	int tn;
	int cn = 1;
	cin >> tn;
	while(tn--){
		cin >> k;
		cin >> s;
		REP( i, k ) p[i] = i;
		int l = SZ(s);
		int sol = 234234234;
		do{
			ss = "";
			REP( i, l/k ){
				int b = i * k;
				REP( j, k )
					ss += s[b+p[j]];		
			}
			//REP( i, k ) cout << p[i] << " ";
			//cout << endl;
		//	cout << ss << endl;
			char bef = '\0';
			int out = 0;
			REP( i, l ){
				if( ss[i] == bef ) continue;
				out++;
				bef = ss[i];
			}
			sol = min( sol, out );
		}while( next_permutation( p, p+k ) );
		printf("Case #%d: %d\n", cn++, sol);
	}

}
