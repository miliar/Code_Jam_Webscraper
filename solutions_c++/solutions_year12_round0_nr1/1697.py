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
#include <iomanip>
#include <iostream>
#include <limits>
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

//#define NDEBUG

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

char code_map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
					'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
					'j', 'p', 'f', 'm', 'a', 'q'};


int main(){
	int ntc;
	cin >> ntc;
	cin.get();
	FORN(tc, 0, ntc){
		string line;
		getline(cin, line);
		FOREACH(c, line)
			if(*c != ' ')
				*c = code_map[*c - 'a'];
		cout << "Case #" << (tc + 1) << ": " << line << endl;
	}
}
