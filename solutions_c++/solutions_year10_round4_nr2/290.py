//Arash Rouhani
#define _GLIBCXX_DEBUG
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>
#include <set>
#include <queue>
#include <stack>
#include <bitset>

using namespace std;

typedef long long LL;
typedef pair < int, int > II;
typedef pair < int, II > I_II;
typedef vector < LL > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < VII > VVII;
typedef vector < VVI > VVVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC > VVC;
typedef stringstream SS;
typedef set < int > SI;

#define sz(c) (int((c).size()))
#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)
#define sford(type, e, start, stop) for(type e=start; e>=stop; e--)
#define foru(var, stop) sfor(int, var, 0, stop)
#define ford(var, start) sford(int, var, start, 0)
#define mp make_pair
#define error(msg) {cout << msg << endl; throw;}
#define assert(cond) if(!(cond)){error(#cond);}

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator){
	ostringstream oss;
	tr(v, e)
	oss << *e << seperator;
	oss.flush();
	return oss.str();
}

template <class T1, class T2> std::ostream& operator << ( std::ostream& out,
                        const std::pair< T1, T2 >& rhs )
{
    out << "(" << rhs.first << ", " << rhs.second << ")";
    return out;
}

int P;
VI M;
VVI C;
VVVI stored;

//final = P-1
//noobs = 0

LL go(int d, int cuts, int i){
	if(d == -1){
		if(P-M[i] <= cuts ){//phew!
			return 0;
		}
		else{
			return 200000000LL;
		}
	}
	else{
		LL &dp = stored[d][cuts][i];
		if(dp == -1){
			LL price = C[d][i];
			int i1 = i << 1;
			int i2 = (i << 1)+1;
			LL buy = go(d-1, cuts+1, i1) + go(d-1, cuts+1, i2) + price;
			LL dont = go(d-1, cuts, i1) + go(d-1, cuts, i2);
			LL ans = min(buy, dont);
			dp = ans;
		}
		return dp;
	}
}

int main(){
	VI pots;
	pots.push_back(1);
	foru(i, 10) pots.push_back(pots.back()*2);// pots[a] = 2^a
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		cin >> P;

		M = VI(pots[P]);
		tr(M, it) cin >> *it;

		C = VVI();
		stored = VVVI();

		foru(i, P){
			int j = P-i-1;
			C.push_back(VI(pots[j]));
			tr(C[i], it) cin >> *it;
		}

		stored = VVVI(P+1, VVI(P+1, VI(pots[P]+5,-1)));
		LL ans = go(P-1, 0, 0);

		cout << "Case #" << testCase << ": " << ans << endl;
	}
}











