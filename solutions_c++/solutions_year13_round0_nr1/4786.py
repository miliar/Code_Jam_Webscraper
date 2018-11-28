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
#define MAX(l, r) l = max((l),(r))
#define MIN(l, r) l = min((l),(r))

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator = " "){
  ostringstream oss;
  tr(v, e) {
    oss << *e << seperator;
  }
  oss.flush();
  return oss.str();
}
template <class T1, class T2> std::ostream& operator << ( std::ostream& out,
                        const std::pair< T1, T2 >& rhs )
{
    out << "(" << rhs.first << ", " << rhs.second << ")";
    return out;
}

template <class T> std::ostream& operator << ( std::ostream& out,
                        const vector< T >& rhs )
{
    tr(rhs, it){
      out << *it << " ";
    }
    return out;
}

template <class T> std::istream& operator >> ( std::istream& in,
                        vector< T >& rhs )
{

    if(false /* sz(rhs) == 0 */){
      // Do getline and assume that's our elements
      string s;
      getline(in, s);
      if(s == "\n" || s == "") getline(in, s);
      stringstream sin(s);
      T temp;
      while(sin >> temp) rhs.push_back(temp);
    } else {
      // read fixed number of elements
      tr(rhs, it) in >> *it;
    }
    return in;
}

template <class InIt> string rangeToString(InIt begin, InIt end, string seperator = " "){
  ostringstream oss;
  for(InIt it = begin; it != end; it++)
    oss << *it << seperator;
  oss.flush();
  return oss.str();
}

const int n = 4;

string solve(VS A){
	string marks = "XO";
#define is_a A[y][x] ==
	tr(marks, it){
		char mark = *it;
		string res = "_ won";
		res[0] = mark;
		foru(y, n){ // fix y
			int count = 0;
			foru(x, n){
				count += is_a mark || is_a 'T';
			}
			if(count == 4) {
				return res;
			}
		}
		foru(x, n){ // fix x
			int count = 0;
			foru(y, n){
				count += is_a mark || is_a 'T';
			}
			if(count == 4) {
				return res;
			}
		}

		{
			int count = 0;
			foru(i, n){
				int x = i;
				int y = i;
				count += is_a mark || is_a 'T';
			}
			if(count == 4) {
				return res;
			}
		}
		{
			int count = 0;
			foru(i, n){
				int x = i;
				int y = 3-i;
				count += is_a mark || is_a 'T';
			}
			if(count == 4) {
				return res;
			}
		}
	}
	int count_dots = 0;
	foru(x, n){
		foru(y, n){
			count_dots += is_a '.';
		}
	}
	if(count_dots == 0){
		return "Draw";
	}
	else {
		return "Game has not completed";
	}
}

int main(){
	mr(int, numTestCases);
	sfor(int, testCase, 1, numTestCases+1) {
		VS A(4);
		cin >> A;
		cout << "Case #" << testCase << ": " << solve(A) << endl;
	}
}











