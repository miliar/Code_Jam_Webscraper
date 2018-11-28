#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
#define MAX 700

typedef pair<long long, long long> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

char trans[MAX][MAX];
char oposed[MAX];
int main(){
	int test , tcase = 1 ;
	cin >> test;
	while(test--){
		cout << "Case #" << tcase++ << ": ";
		memset( trans , -1 , sizeof(trans) );
		memset( oposed , -1 , sizeof(oposed) );
		int C , D , N;
		cin >> C;
		REP( i , C ){
			char a , b , c;
			cin >> a >> b >> c;
			trans[a][b] = c;
			trans[b][a] = c;
		}
		cin >> D;
		REP( i , D ){
			char a , b;
			cin >> a >> b;
			oposed[a] = b;
			oposed[b] = a;
		}
		cin >> N;
		string L;
		cin >> L;
		vector< char > ans;
		REP( i , L.size() ){
			ans.pb(L[i]);
			while( ans.size() >=  2 ){
				char last = ans.back();
				char alast = ans[ans.size()-2];
				if( trans[alast][last] != -1 ){
					ans.pop_back();
					ans.pop_back();
					ans.pb(trans[alast][last]);
					continue;
				}
				int flag = 0;
				REP( i , ans.size()-1 ){
					if( oposed[ans.back()] == ans[i] ){
						flag = 1;
						ans.clear();
						break;
					}
				}
				if( flag == 0 ) break;
			}
		}
		cout << "[";
		int j = ans.size() -1;
		REP( i , ans.size() ){
			if( i != 0 ) cout << ", ";
			cout << ans[i];
		}
		cout << "]" << endl;
	}
	return 0;
}

