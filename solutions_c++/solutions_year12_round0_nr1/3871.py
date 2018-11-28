#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue> 
#include <cfloat>
#include <string> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <complex>

using namespace std;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define EPS 1e-7

#define FILL(X, V) memset(X, V, sizeof(X))
#define TI(X) __typeof((X).begin())

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FORIT(it, i) for(typeof((i).begin()) it = (i).begin(); it != (i).end(); it++)

#define ALL(V) V.begin(), V.end()
#define S(V) (int)V.size()

#define pb push_back
#define mp make_pair

template<typename T> T inline SQR( const T &a ){ return a*a; }

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio( false );
	string a, b;
	char yo[256];
	yo[' '] = ' ';
	yo['a'] = 'y';
	yo['b'] = 'h';
	yo['c'] = 'e';
	yo['d'] = 's';
	yo['e'] = 'o';
	yo['f'] = 'c';
	yo['g'] = 'v';
	yo['h'] = 'x';
	yo['i'] = 'd';
	yo['j'] = 'u';
	yo['k'] = 'i';
	yo['l'] = 'g';
	yo['m'] = 'l';
	yo['n'] = 'b';
	yo['o'] = 'k';
	yo['p'] = 'r';
	yo['r'] = 't';
	yo['s'] = 'n';
	yo['t'] = 'w';
	yo['u'] = 'j';
	yo['v'] = 'p';
	yo['w'] = 'f';
	yo['x'] = 'm';
	yo['y'] = 'a';
	yo['q'] = 'z';
	yo['z'] = 'q';
	
	int t, tes = 1;
	cin>>t;
	cin.ignore();
	while(t--){
		string s;
		getline(cin, s);
		int sz = S(s);
		cout<<"Case #"<<tes++<<": ";
		REP(i, sz){
			cout<<yo[s[i]];
		}
		
		cout<<'\n';
	}
	
	return 0;
}
