#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef double LD;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

int main() {
  ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);
	
	int Q;
	
	cin >> Q;
	
	REP(q,Q) {
	
		map<pair<char,char>, char> M;
		
		//M[MP('A','A')] = 'B';
	
		map<pair<char,char>, int> O;
		
		int C;
		
		cin >> C;
		
		REP(i,C) {
			string s;
			cin >> s;
			assert(s.size() == 3);
			//cout << s[2] << endl;
			M[MP(s[0],s[1])] = s[2];
			M[MP(s[1],s[0])] = s[2];
		}
		
		int D;
		
		cin >> D;
		
		REP(i,D) {
			string s;
			cin >> s; //cout << s << endl;
			O[MP(s[0],s[1])] = 1;
			O[MP(s[1],s[0])] = 1;
		}
		
		//cout << O[MP('F', 'Q')] << endl;
	
		int n;
	
		cin >> n;
	
		string s;
	
		cin >> s;
		
		//cout << s << endl;
	
		vector<char> res;
	
		REP(i,n) {//cout << res.size() << " ";
			if (res.size() && M[MP(s[i], res.back())]) {
				char c = M[MP(res.back(), s[i])]; 
				res.pop_back();
				res.PB(c);
			}
			else {
				res.PB(s[i]);
				FORE(it,res)
					if (O[MP(*it, s[i])]) {
						res.clear();
						break;
					}
			}
		}	
		
		cout << "Case #" << q + 1 << ": [";
		
		if (res.size())
			cout << res[0];
			
		FOR(i,1,res.size() - 1)
			cout << ", " << res[i];
			
		cout << "]\n";
		
		
	}
	

  return 0;
}
