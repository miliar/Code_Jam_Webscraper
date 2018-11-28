//105514SN
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, a, b) for(int i=(a);i<int(b);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);

int a, b;


int contar(int x) {

	int y;
	string s;
	ostringstream salida;
	salida << x;
	s = salida.str();
	set<int> S;

	forn(i, 0, SZ(s)-1) {
		char aux = s[0];
		s.erase(s.begin());
		s += aux;
		if(s[0] == '0') continue;
		
		istringstream in(s);
		in >> y;

		if(a<=x && x<=b && a<=y && y<=b && x < y) {
//			cout << a<< " / " << x << " " << y << " / " << b << endl;
			S.insert(y);
		}
	}
	return S.size();
}

int main(void) {

	int casos;
	cin >> casos;
	forn(q, 0, casos) {
	
		ll ret = 0;
		cin >> a >> b;
		
		forn(k, a, b) {
			ret += contar(k);		
		}
		cout << "Case #"<< q+1 << ": " << ret << endl;
	}

	return 0;
}
