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
typedef vector < int > VI;
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

typedef map <pair<char, char>, char> MCC_C;

int f(int a, int b){ return a xor b;}

int main(){
	string _bases = "QWERASDF";
	SI bases(all(_bases));
	int numTestCases;
	cin >> numTestCases;
	sfor(int, _testCaseNum, 1, numTestCases+1){
		int n;
		cin >> n;
		VI vi(n);
		tr(vi, it) cin >> *it;
		int s = accumulate(all(vi), 0);
		s -= *min_element(all(vi));
		int x = accumulate(all(vi),0, f);
		cout << "Case #" << _testCaseNum << ": " << (x?"NO":toString(s)) << endl;
	}
}







