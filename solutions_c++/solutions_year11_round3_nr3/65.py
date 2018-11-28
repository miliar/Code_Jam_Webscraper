//Arash Rouhani
#define _GLIBCXX_DEBUG
//#define NDEBUG
#include <iostream>
#include <iomanip>
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
#include <map>
#include <bitset>
#include <assert.h>

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
typedef set < SI > SSI;
typedef vector < SI > VSI;

#define sz(c) (int((c).size()))
#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)
#define foru(var, stop) sfor(int, var, 0, stop)
#define sford(type, e, start, stop) for(type e=start; e>=stop; e--)
#define ford(var, start) sford(int, var, start, 0)
#define mp make_pair
#define error(msg) {cout << msg << endl; throw;}
#define mr(type, v1) \
	type v1; \
	cin >> v1;
#define mr2(type, v1, v2) \
	type v1, v2; \
	cin >> v1 >> v2;
#define mr3(type, v1, v2, v3) \
	type v1, v2, v3; \
	cin >> v1 >> v2 >> v3;
#define mr4(type, v1, v2, v3, v4) \
	type v1, v2, v3, v4; \
	cin >> v1 >> v2 >> v3 >> v4;
#define mr5(type, v1, v2, v3, v4, v5) \
	type v1, v2, v3, v4, v5; \
	cin >> v1 >> v2 >> v3 >> v4 >> v5;

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

template <class InIt> string rangeToString(InIt begin, InIt end, string seperator){
	ostringstream oss;
	for(InIt it = begin; it != end; it++)
		oss << *it << seperator;
	oss.flush();
	return oss.str();
}


int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		mr(int, n);
		mr2(LL, L, H);
		VI a(n);
		tr(a, it) cin >> *it;

		LL ans = 1234567890123456789LL;
		sfor(LL, freq, L, H+1){
			bool ok = true;
			foru(i, n){
				ok &= a[i]%freq == 0 || freq%a[i] == 0;
			}
			if(ok){
				ans = min(ans, freq);
				break;
			}
		}

		cout << "Case #" << testCase << ": " << (ans < 1234567890123456789LL ? toString(ans) : "NO") << endl;
	}
}






