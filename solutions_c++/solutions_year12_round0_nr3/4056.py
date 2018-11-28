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

int getSize(int num){
	int tam = 0;
	while(num){
		num /= 10;
		tam++;
	}
	
	return tam;
}

string toString(int num){
	string out;
	out.reserve(getSize(num));
	while(num){
		out.insert(out.begin(), char('0' + num % 10));
		num /= 10;
	}
	
	return out;
}

int toInt(string &str){
	int res = 0, sz = S(str);
	REP(i, sz){
		res *= 10;
		res += str[i] - '0';
	}
	
	return res;
}

int main(){
	ios::sync_with_stdio( false );
	int t, tes = 1;
	cin>>t;
	while(t--){
		int a, b;
		cin>>a>>b;
		
		int64 ans = 0;
		FOR(i, a, b+1){
			string aux = toString(i), s;
			int sz = getSize(i);
			s = aux + aux;
			set<string> vals;
			REP(i, sz){
				string aux2 = s.substr(i, sz);
				if(aux < aux2 && toInt(aux2) <= b) vals.insert(aux2);
			}
			
			ans += S(vals);
		}
		
		cout<<"Case #"<<tes++<<": "<<ans<<'\n';
	}
	return 0;
}
