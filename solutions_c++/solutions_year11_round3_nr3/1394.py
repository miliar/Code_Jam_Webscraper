#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

typedef unsigned long long ull;

ull gcd(ull a, ull b){
	if (b == 0) return a;
	else return gcd(b, a % b);
}

ull lcm(ull a, ull b){
	return (a*b)/gcd(a,b);
}



int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	ull tst;
	ull n, l, h, tc;
	
	cin >> tst;
	FORN(tc, 1, tst+1){

		cin >> n >> l >> h;	
		vector<ull> in;
		for(ull k = 0; k < n; ++k){
			ull t; 
			cin >> t;
			in.push_back(t);
		}
		sort(ALL(in));
		
		bool res = true;
		ull i;
		for(i = l ; i <= h; ++i){
			res = true;
			FORN(j, 0, n){
				if (not((in[j] >= i and in[j] % i == 0) or 
					(in[j] <= i and i % in[j] == 0))){
					res = false; break;
				}
			}
			if (res) break;
		}

		cout << "Case #" << tc << ": ";
		if (res) cout << i << endl;
		else cout << "NO" << endl;

	}
	
}
