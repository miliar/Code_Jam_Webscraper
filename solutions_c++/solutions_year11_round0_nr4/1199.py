#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
int p[1 << 20];
bool use[1 << 20];

vi getC(vi p) {
	int n = sz(p) - 1;
	vi use(n + 1, 0);
	vi r;
	for (int i = 1; i <= n; ++i) {
		int cur = i;
		int c = 0;
		while (!use[cur]) {
			use[cur] = 1;
			++c;
			cur = p[cur];
		}
		if (c) r.pb(c);
	}
	return r;
}
double dp[100];
bool testBit(int x, int p) { return (x >> p) & 1; }
double get(int n) {
	vi p(n + 1, 0);
	for (int i = 1; i <= n; ++i) 
		p[i] = i + 1;
	p[n] = 1;
	double r = 1e30;
	for (int use = 1; use < (1 << n); ++use) {
		if (((use - 1) & use) == 0) continue;
		int nf = 0;
		double a = 0;
		int cnt = 0;
		//print(use);
		vi p1(n, 0);
		for (int i = 0; i < n; ++i) p1[i] = i;
		vi cur = p1;
		do {
			bool ok = true;
			for (int i = 0; i < n; ++i) {
				if (!testBit(use, i) && cur[i] != p1[i]) {
					ok =false;
					break;
				}
			}
			if (!ok) continue;
			++nf;
			vi p2 = p;
			for (int i = 0; i < n; ++i)
				p2[i + 1] = p[cur[i] + 1];
			vi u = getC(p2);
			//print(p2);
			if (sz(u) == 1) ++cnt;
			else {
				for (int j = 0; j < sz(u); ++j) {
					a += dp[u[j]];
				}
			}

		} while (next_permutation(cur.begin(), cur.end()));
		double t = (a + nf) * 1.0 / (nf - cnt);
		//cout << t << endl;
		if (r > t) {
			r = t;
		}
	}
/*	for (int c = 2; c <= n; ++c) {
//	for (int c = n - 1; c < n; ++c) {
//	for (int c = 2; c <= 2; ++c) {
		vi cur = p;
		int nf = 0;
		double a = 0;
		int cnt = 0;
		do {
			++nf;
			vi u = getC(cur);
			if (sz(u) == 1) ++cnt;
			else {
				for (int j = 0; j < sz(u); ++j) {
					a += dp[u[j]];
				}
			}
		} while (next_permutation(cur.begin() + 1, cur.begin() + 1 + c));
		double t = (a + nf) * 1.0 / (nf - cnt);
//		cout << t << endl;
		r = min(r, t);
	}*/
	return r;
}

void init() {
	dp[2] = 2;
//	dp[3] = 4;
	for (int i = 3; i <= 7; ++i) {
//		puts("-=-=");
		dp[i] = get(i);
		printf("%0.12lf\n", dp[i]);
	}
	exit(0);
}

void solve(int tst) {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		use[i] = false;
		cin >> p[i];
	}
	
	double ans = 0;
	for (int i = 1; i <= n; ++i) {
		int cur = i;
		int cnt = 0;
		while (!use[cur]) {
			use[cur] = true;
			++cnt;
			cur = p[cur];
		}
		//if (cnt > 1) ans += (cnt - 1) * 2;
		//if (cnt > 1) ans += dp[cnt];
		if (cnt > 1) ans += cnt;
	}
	printf("Case #%d: %0.6lf\n", tst, ans); 
}
int main() {
//	init();
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i)
		solve(i);
    return 0;
}
