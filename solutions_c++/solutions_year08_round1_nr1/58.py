#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

#define FORALL(var,x) for (typeof(x.begin()) var=x.begin(); var!=x.end(); var++)
#define FOR(var,lo,hi) for (int var=(lo); var<(hi); var++)
#define SORT(x) sort(x.begin(), x.end())
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;

int main(void)	{
	int T, n, nc;

	cin >> T;
	vector<ll> v, w;

	for (int nc = 1; nc <= T; nc++)	{
		cin >> n;
		v.clear();
		w.clear();
		for (int i = 0; i < n; i++)	{
			ll x;
			cin >> x;
			v.pb(x);
		}
		for (int i = 0; i < n; i++)	{
			ll x;
			cin >> x;
			w.pb(x);
		}
		sort(v.begin(), v.end());
		sort(w.begin(), w.end());
		ll ans = 0;
		FOR(i,0, n)	{
			ans += v[i] * w[n-i-1];
		}
		cout << "Case #" << nc << ": " << ans << endl;
	}
}
