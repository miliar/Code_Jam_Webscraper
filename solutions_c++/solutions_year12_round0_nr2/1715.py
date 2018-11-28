#include <memory.h>
#include <stdio.h>
#include <assert.h>

#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <sstream>

using namespace std;

typedef long long int64;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll> vll;

#define all(x) (x).begin(), (x).end()
#define clear(x) (x).clear()
#define clearm(x) memset((x), 0, sizeof(x))

#define FOR(i, b, e) for (int i = (b); i < (e); ++i)
#define RE(i, n) FOR(i, 0, (n))
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))>0)
#define containL(S,X) (((S)&twoL(X))>0)
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;} 
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;} 
string toString(int64 v){ostringstream sout;sout<<v;return sout.str();} 
string toString(int v){ostringstream sout;sout<<v;return sout.str();} 

template<class T> inline T countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T sqr(T x){return x * x;}
template<class T> inline T gcd(T a,T b){if(a < 0) return gcd(-a,b); if(b < 0) return gcd(a,-b); return (b == 0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){return a*(b/gcd(a,b));}
template<class T> void out(T A[],int n){for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}
template<class T> void out(vector<T> A,int n = -1){if(n==-1) n = A.size();for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}

const int maxn = 32;

int GetMax(int x, int s) {
	int ans = -1000;
	if (s == 0) {
		if (x%3 == 0) {
			ans = x/3;
		} else if (x >= 1 && (x - 1)%3 == 0) {
			ans = (x - 1)/3 + 1;
		} else if (x >= 2 && (x - 2) % 3 == 0) {
			ans = (x - 2)/3 + 1;
		}
	} else {
		if (2 <= x && x <= 28) {
			if (x >= 2 && (x - 2)%3 == 0) {
				ans = (x - 2)/3 + 2;
			} else if (x >= 3 && (x - 3)%3 == 0) {
				ans = (x - 3)/3 + 2;
			} else if (x >= 4 && (x - 4)%3 == 0) {
				ans = (x - 4)/3 + 2;
			}
		}
	}
	return ans;
}

int a[maxn];
int mem[maxn][101];
int n,t,s,p;

int F(int x, int s) {
	if (x < 0 && s == 0) return 0;
	if (x < 0 && s > 0) return -2;
	if (mem[x][s] != -1) return mem[x][s];
	int & ref = mem[x][s];
	ref = -2;
	int m1 = GetMax(x, 1);
	int m0 = GetMax(x, 0);

	if (F(x-1, s) >= 0) {
		ref = F(x - 1, s) + ((m0 >= p)?a[x]:0);
	}
	if (m1 < 0) {
		return ref;
	}

	int len = min(s, a[x]);
	for (int i = 1; i <= len; ++i) {
		int r = F(x - 1, s - i);
		if (r < 0) continue;
		if (m1 >= p) {
			ref = max(ref, r + i);
		} else {
			ref = max(ref, r);
		}
	}
	return ref;
}

int main() {

    //freopen("in.txt", "r", stdin);
    //freopen("B-large(1).in", "r", stdin);
    //freopen("B-large(1).out", "w", stdout);
    //freopen("out.txt", "w", stdout);
    // freopen("out.txt", "w", stdout);

	int ncase;
	cin >> ncase;
	RE(tt, ncase) {	
		cout << "Case #" << tt + 1 << ": ";
		memset(a, 0, sizeof(a));
		memset(mem, -1, sizeof(mem));
		cin >> n >> s >> p;
		RE(i, n) {
			int x;
			cin >> x;
			++a[x];
		}
		int ans = F(30, s);
		/*
		int ans = 0;	
		for (int i = 0; i < (1 << n); ++i) if (countbit(i) == s) {
			int t = 0;
			for (int j = 0; j < n; ++j) {
				if (contain(i, j)) {
					int tmp = GetMax(b[j], 1);
					if (tmp < 0) t = tmp;
					else t += (tmp >= p);
				} else {
					int tmp = GetMax(b[j], 0);
					if (tmp < 0) t = tmp;
					else t += (tmp >= p);
				}
			}
			ans = max(ans, t);
		}
		*/
		cout << ans << endl;
	}
    return 0;
}