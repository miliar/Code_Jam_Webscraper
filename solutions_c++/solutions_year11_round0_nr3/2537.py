/*
 * CandySplitting
 * May 7, 2011,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int num[1120];
int n;
bool fe;
int ans;
int vis[20];
void clc(int idx) {
	if (idx >= n) {
		int c = 0;
		int c2 = 0;
		int sum1 = 0, sum2 = 0, ret = 0;
		for (int i = 0; i < n; i++) {
			if (vis[i]) {
				c2++;
				sum1 = sum1 ^ num[i];
				ret += num[i];
			} else
				c++, sum2 = sum2 ^ num[i];
		}
		if (c && c2 && sum1 == sum2) {
			fe = 1;
			ans = max(ans, ret);
		}
		return;
	}
	for (int i = 0; i < 2; i++) {
		vis[idx] = i;
		clc(idx + 1);
	}

}
vector<ll> v;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	loop(id,t) {
		ll ans = 0;
		ll sum = 0;
		scanf("%d", &n);
		v.clear(), v.resize(n);
		loop (i,n) {
			scanf("%d", num + i);
			ans += num[i];
			v[i] = num[i];
			sum = sum ^ num[i];
		}
		if (sum)
			printf("Case #%d: NO\n", id + 1);
		else {
			sort(ALL(v));
			ans -= v[0];
			printf("Case #%d: ", id + 1);
			cout << ans << endl;
		}
		//		fe = 0;
		//		ans = -OO;
		//		CLR(vis,0);
		//		clc(0);
		//		if (fe == 0)
		//			printf("Case #%d: NO\n", id + 1);
		//		else
		//			printf("Case #%d: %d\n", id + 1, ans);

	}

	return 0;
}
