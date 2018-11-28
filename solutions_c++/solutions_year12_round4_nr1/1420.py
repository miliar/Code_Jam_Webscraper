/*
 * a.cpp
 *
 *  Created on: May 26, 2012
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
#define rall(v) v.rbegin(),v.rend()
#ifdef _MSC_VER
#define rep(i,m) for(decltype(m) i=0;i<m;i++)
#define repI(i,m) for(decltype(m.begin()) i = m.begin();i!=m.end();++i)
#define repRI(i,m) for(decltype(m.rbegin()) i = m.rbegin();i!=m.rend();++i)
#else
#define rep(i,m) for(__typeof(m) i=0;i<m;i++)
#define repI(i,m) for(__typeof(m.begin()) i = m.begin();i!=m.end();++i)
#define repRI(i,m) for(__typeof(m.rbegin()) i = m.rbegin();i!=m.rend();++i)
#endif
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define EPS (1e-9)
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;

#define SMALL_INPUT

int main() {
	freopen("a.in", "rt", stdin);
#ifdef SMALL_INPUT
	freopen("a-small-attempt0.in", "rt", stdin);
	freopen("a-small.out", "wt", stdout);
#endif
#ifdef LARGE_INPUT
	freopen("a-large.in", "rt", stdin);
	freopen("a-large.out", "wt", stdout);
#endif
	int tc;
	cin >> tc;
	rep(T,tc) {
		//
		int n, d;
		cin >> n;
		vpii v(n);
		rep(i,n)
			cin >> v[i].first >> v[i].second;
		sort(all(v));
		cin >> d;

		deque<pair<int, int> > q;
		rep(i,v.size())
			if (v[i].first == v[0].first)
				q.pb(mp(0, v[i].first));

		bool f = 0;
		while (!q.empty()) {
			pii p = q.front();
			q.pop_front();
			if (p.first + 2 * p.second >= d) {
				f = 1;
				break;
			}
			vector<pair<int, int> >::iterator it = lower_bound(all(v),
					mp(p.first + p.second, -1));
			++it;
			for (; it != v.end(); ++it) {
				if (it->first <= p.first + 2 * p.second
				/*&& it->second >= it->first - (p.first + p.second)*/) {
					q.pb(mp(max(p.first + p.second, (it->first - it->second)),
					min(it->second,
							it->first - (p.first + p.second))));
				}
			}
		}

		cout << "Case #" << T + 1 << ": ";
		//
		if (f)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
#ifdef SMALL_INPUT
		cerr << T+1 << " of " << tc << " is done." << endl;
#endif
#ifdef LARGE_INPUT
		cerr << T+1 << " of " << tc << " is done." << endl;
#endif
	}
	return 0;
}
