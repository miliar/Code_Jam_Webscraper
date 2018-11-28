#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int N = 25;

int main(int argc, char *argv[])
{
#if 0
	freopen(argv[1],"r",stdin);
#endif
#if 1
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	int T,n;
	cin >> T;
	FOR(t,1,T+1) {
		vi o,b;
		vpii v;
		char r;
		int p;
		cin >> n;
		FOR(i,0,n) {
			cin >> r >> p;
			if (r == 'O')
				o.pb(p);
			else
				b.pb(p);
			v.pb(pii(r,p));
		}
		int i = 0;
		int io = 0, ib = 0;
		int s = 0;
		int cur_o = 1, cur_b = 1;
		while (true) {
			if (i == v.size())
				break;
			++s;
			r = v[i].first;
			p = v[i].second;
			if (r == 'O') {
				if (cur_o == p) {
					++io;
					++i;
				} else if (cur_o < p) {
					++cur_o;
				} else {
					--cur_o;
				}
				if (ib == b.size())
					continue;
				if (cur_b < b[ib])
					++cur_b;
				else if (cur_b > b[ib])
					--cur_b;
			} else {
				if (cur_b == p) {
					++ib;
					++i;
				} else if (cur_b < p) {
					++cur_b;
				} else {
					--cur_b;
				}
				if (io == o.size())
					continue;
				if (cur_o < o[io])
					++cur_o;
				else if (cur_o > o[io])
					--cur_o;
			}
		}
		cout << "Case #" << t << ": " << s << endl;
	}
	return 0;
}
