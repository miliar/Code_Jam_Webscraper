/*
 * c.cpp
 *
 *  Created on: May 5, 2012
 *      Author: AhmedHamza
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <complex>

#ifdef _MSC_VER
#include<hash_set>
#include<hash_map>
using namespace stdext;
#else
#if __GNUC__ >2
#include<ext/hash_set>
#include<ext/hash_map>
using namespace __gnu_cxx;
#else
#include<hash_set>
#include<hash_map>
#endif
#endif

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(__typeof(m) i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<long long> vi;
typedef vector<vector<int> > vii;
typedef long long ll;


#define SMALL_INPUT
int main() {
//	freopen("c.in", "rt", stdin);
#ifdef SMALL_INPUT
	freopen("c-small-attempt0.in", "rt", stdin);
	freopen("c-small.out", "wt", stdout);
#endif
#ifdef LARGE_INPUT
	freopen("c-large.in", "rt", stdin);
	freopen("c-large.out", "wt", stdout);
#endif
	int tc;
	cin >> tc;
	rep(T,tc) {
		int n;
		cin >> n;
		vi v(n);
		rep(i,n)
			cin >> v[i];
		map<ll, vi> m;
		rep(i,(1<<n)) {
			ll s = 0;
			rep(j,32) {
				if ((i >> j) & 1)
					s += v[j];
			}
			m[s].pb(i);
		}
		for (map<ll, vi>::iterator it = m.begin(); it != m.end(); ++it)
			if (it->second.size() > 1) {
				cout << "Case #" << T + 1 << ":" << endl;
				rep(i,2) {
					string sep;
					rep(j,32) {
						if ((it->second[i] >> j) & 1)
							cout << sep << v[j], sep = " ";
					}
					cout << endl;
				}
				break;
			}

	}
	return 0;
}

