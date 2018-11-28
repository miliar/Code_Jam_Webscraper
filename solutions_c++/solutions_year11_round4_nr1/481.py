#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

typedef pint Walkways;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		
		int X = in();
		int S = in();
		int R = in();
		int maxrun = in();
		int N = in();
		
		vector<pint> data;
		int len = 0;
		rep(i, N) {
			int b = in();
			int e = in();
			int w = in();
			
			data.pb(mp(w, e - b));
			len += e - b;
		}
		data.pb(mp(0, X - len));
		
		sort(data.begin(), data.end());
		
		double ans = 0;
		
		rep(i, N + 1) {
			int w = data[i].first;
			int l = data[i].second;
			
			if(ans > maxrun) {
				ans += 1. * l / (S + w);
			}
			else {
				double t_run = 1. * l / (R + w);
				if(ans + t_run > maxrun) {
					double runned = (maxrun - ans) * (R + w); // run-ran-run, of course :-)
					double remain = l - runned;
					ans = maxrun + remain / (S + w);
				}
				else {
					ans += t_run;
				}
			}
		}
		
		printf("%.12f\n", ans);
	}
	return 0;
}
