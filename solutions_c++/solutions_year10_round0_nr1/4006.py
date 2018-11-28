
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define clr(x)         memset((x), 0, sizeof(x))
#define all(x)         (x).begin(), (x).end()
#define pb             push_back
#define mp             make_pair
#define sz(x)          ((int)((x).size()))
#define FOR(i,a,b)     for(i = (a); i <= (b); ++i) //__typeof(st)
#define FORD(i,a,b)    for(i = (b); i >= (a); --i)
#define REP(i,n)       for(i = 0; i < (n); ++i)
#define REPD(i,n)      for(i = (n)-1; i >= 0; --i)
#define FOREACH(it,n)  for(it = (n).begin(); it != (n).end(); ++it) // __typeof((n).begin()) 

#define setbit(n,i)    ((n) = (n) | (1<<(i)))
#define bitset(n,i)    ((n) & (1<<(i)) == (n))

typedef vector< int >     vi;
typedef vector< vi >      vii;
typedef pair< int, int >  pii;
typedef vector< pii >     vpii;
typedef vector< string >  vs;

//typedef long long         i64;
typedef unsigned long     ul;

template<class T>
static std::string tostring(T val) {
    std::ostringstream stream;
    stream << val;
    return stream.str();
}

//const string INPUT = "A-input.in"; const string OUTPUT = "A-output.out";
//const string INPUT = "A-small-attempt2.in"; const string OUTPUT = "A-small-attempt2.out";
const string INPUT = "A-large.in"; const string OUTPUT = "A-large.out";

//const string INPUT = "B-input.in"; const string OUTPUT = "B-output.out";
//const string INPUT = "B-small-attempt0.in"; const string OUTPUT = "B-small-attempt0.out";
//const string INPUT = "B-large-practice.in"; const string OUTPUT = "B-large-practice.out";

string tobin(ul d, int n) {
	string a = "";
	while (d) {
		a += tostring(d & 1);
		d >>= 1;
	}
	int i;
	FOR(i,sz(a),n-1) a+="0";
	return a;
}

void solve(int t) {
	__int64 n,k;
	cin >> n >> k;
	/*
	ul i, final = (1<<n)-1;
	FOR(i,0,final) {
		cout << tobin(i,n) << "\n";
	}*/
	k %= (1<<n);
	bool res = (1 << n) - 1 <= k;
	cout <<"Case #"<< t <<": "<< (res?"ON":"OFF") << "\n";
}

int main() {

	freopen(INPUT.c_str(), "r", stdin); freopen(OUTPUT.c_str(), "w", stdout);
	int t,T;
	cin >> T;
	FOR(t,1,T) {
		solve(t);
	}
	return 0;
}






