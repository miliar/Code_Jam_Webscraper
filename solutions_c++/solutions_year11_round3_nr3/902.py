/*
 * c.cpp
 *
 *  Created on: May 22, 2011
 *      Author: user1
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
#include <valarray>
#include <ctime>
#include <string.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(typeof(m) i=0;i<m;++i)
#define forin(i,a,b) for(typeof(a) i=a;i<=b;++i)
#define foreach(i,m) for(typeof((m).begin()) i=(m).begin();i!=(m).end();++i)
#define rrep(i,m) for(typeof(m) i=m-1;i>=0;--i)
#define rforin(i,a,b) for(typeof(b) i=b;i>=b;--i)
#define rforeach(i,m) for(typeof((m).rbegin()) i=(m).rbegin();i!=(m).rend();++i)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

int a[100000];

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("in.out", "wt", stdout);
#endif

	int t, n, K = 0, l, h;
	scanf("%d", &t);
	while (t--) {

		scanf("%d%d%d", &n, &l, &h);

		rep(i,n)
			scanf("%d", a + i);

		bool f;
		int i;
		for (i = l; i <= h; ++i) {
			f = 1;
			rep(j,n)
				if (a[j] % i != 0 && i % a[j] != 0) {
					f = 0;
					break;
				}
			if (f) {
				break;
			}
		}

		if (f)
			printf("Case #%d: %d\n", ++K, i);
		else
			printf("Case #%d: NO\n", ++K);
	}

	return 0;
}

