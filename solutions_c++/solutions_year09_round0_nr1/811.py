#include<iostream>
#include<cstdio>
#include<cmath>
#include<complex>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<sstream>
#include<utility>

using namespace std;
using namespace __gnu_cxx;

typedef long long _ll;
typedef double _db;
typedef unsigned int _ui;
typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;
typedef vector<string> _vs;
typedef istringstream _is;
typedef ostringstream _os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS = (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();i++)
#define PRINT(v) for(int (i)=0;(i)<(int)(a).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

bool patt[15][26];

int main(){
	ios::sync_with_stdio(0);
	int L,D,N;
	cin >> L >> D >> N;
	_vs dict(D,"");
	REP(i,D) cin >> dict[i];
	REP(i,N){
		string s;
		cin >> s;
		REP(j,15) REP(k,26) patt[j][k] = false;
		int pos = 0;
		REP(j,L){
			if(s[pos] != '('){
				patt[j][s[pos] - 'a'] = true;
				pos++;
			}
			else{
				pos++;
				while(s[pos] != ')')
					patt[j][s[pos++] - 'a'] = true;
				pos++;
			}
		}

		int cnt = D;
		REP(j,D)
			REP(k,L)
				if(!patt[k][dict[j][k] - 'a']){
					cnt--;
					break;
				}
		cout << "Case #" << i+1 << ": " << cnt << "\n";
	}
	return 0;
}

