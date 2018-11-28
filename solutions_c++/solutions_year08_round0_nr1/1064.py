#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>

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

map< string, int > m;

int main(){
	int tn, s, q;
	int cn = 1;
	cin >> tn;
	while(tn--){
		m.clear();
		cin >> s;
		string tmp;
		getline(cin, tmp);
		REP( i, s ) getline( cin, tmp );

		cin >> q;
		getline(cin, tmp);
		int k = 0;
		int out = 0;
		REP( i, q ){
			getline( cin, tmp );
			if( m[tmp] == 0 ){
				if( ++k == s ) m.clear(), out++, k = 1;
				m[tmp] = 1;
			}
		}
		cout << "Case #" << cn++ << ": " << out << endl;
	}
}

