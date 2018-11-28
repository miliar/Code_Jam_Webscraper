/*
 * BSpaceEmergency.cpp
 *
 *  Created on: May 22, 2011
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;
const int mx = 1009;
int a[mx];
int main()
{

	freopen("B-large.in", "rt", stdin);
	freopen("b.txt", "wt", stdout);

	int d;scanf("%d", &d);
	for (int ii = 0; ii < d; ++ii) {
		printf("Case #%d: ", ii+1);
		ll l, t, n, c;
//		scanf("%lld%lld%lld%lld", &l, &t, &n, &c);
		cin>>l>>t>>n>>c;
		for (int i = 0; i < c; ++i) {
			scanf("%d", a + i);
		}
		int idx = -1;
		long double res = 0;
		for (int i = 0; i < n; ++i) {
			if( t  >= a[i%c] * 2)
				idx = i, t -= a[i%c] * 2, res+=a[i%c]*2;
			else break;
		}
		++idx;
		vector<long double>dist;
		if(idx<n)
			dist.pb(a[idx%c] - t/2), res+=t;
		for (int i = idx + 1; i < n; ++i) {
			dist.pb(a[i%c]);
		}
		sort(dist.rbegin(), dist.rend());

		for (int i = 0; i < (int )dist.size(); ++i) {
//		cout<<dist[i]<<endl;
			if(i < l)
				res+=dist[i];
			else
				res+=(dist[i]*2);
		}
		ll r = (ll)(res+1e-6);
		cout<<r<<endl;
	}
	return 0;
}
/*
2
2 20 8 2 3 5
1 4 2 2 10 4

 */
