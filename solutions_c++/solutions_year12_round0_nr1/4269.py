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

const string SAMPLE_INPUT = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

const string SAMPLE_OUTPUT = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

map<char,char> M;

int main() {
  	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);
	
	assert(SAMPLE_INPUT.size() == SAMPLE_OUTPUT.size());

	for (char c = 'a'; c <= 'z'; ++c)
		M[c] = c;

	M['a'] = 'y';
	M['o'] = 'e';
	M['z'] = 'q';
	M['q'] = 'z';


	for (int i = 0; i < SAMPLE_INPUT.size(); ++i)
		M[SAMPLE_INPUT[i]] = SAMPLE_OUTPUT[i];

	/*map<char,int> L, R;

	FORE(it,M) {
		L[it->ST]++;
		R[it->ND]++;
		cout << it->ST << " " << it->ND << endl;
	}

	for (char c = 'a'; c <= 'z'; ++c)
		cout << c << " " << L[c] << " " << R[c] << endl;*/



	int T;

	cin >> T;

	string line;
	getline(cin,line);

	REP(q,T) {

		cout << "Case #" << q + 1 << ":";

		getline(cin,line);

		stringstream ss(line);
		string s;

		while (ss >> s) {
			FORE(it,s)
				*it = M[*it];
			cout << " " << s;
		}
		
		cout << endl;
	}

  	return 0;
}	
