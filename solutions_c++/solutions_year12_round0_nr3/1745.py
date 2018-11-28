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
#include <ctime>

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

//const int maxn = 5555 + 5;
const int maxn = 2000000 + 5;

bool chk[maxn];
struct Node {
	string str;
	int x;
	int next;
};

Node dic[maxn];

bool operator < (const Node & x, const Node & y) {
	if (x.str != y.str) {
		return x.str < y.str;
	} else {
		return x.x < y.x;
	}
}

// pair<string, int> dic[maxn];
int hash[maxn];

void Init() {
	double start_time=(double)clock();
	RE(i, maxn) {
		dic[i].str = toString(i);
		dic[i].x = i;
		dic[i].next = maxn;

		string tmp = dic[i].str;
		int ans = maxn;
		RE(j, tmp.size()) {
			tmp = tmp.substr(1) + tmp[0];
			if (tmp[0] == '0') continue;
			int x = toInt(tmp);
			if (x <= i) continue;
			ans = min(ans, x);
		}
		dic[i].next = ans;
	}
	sort(dic, dic + maxn);
	RE(i, maxn) {
		hash[dic[i].x] = i;
	}

	double end_time=(double)clock();
	//printf("%.3lf\n",(end_time-start_time)/CLOCKS_PER_SEC);
}



int main() {

    //freopen("in.txt", "r", stdin);
    //freopen("C-large(1).in", "r", stdin);
    //freopen("C-large(1).out", "w", stdout);
    //freopen("out.txt", "w", stdout);
    // freopen("out.txt", "w", stdout);

	Init();
	int ncase;
	cin >> ncase;
	double start_time=(double)clock();
	RE(tt, ncase) {	
		cout << "Case #" << tt + 1 << ": ";
		int a, b;
		cin >> a >> b;
		memset(chk, 0, sizeof(chk));
		int ans = 0;
		for (int i = a; i <= b; ++i) if (chk[i] == 0) {
			int cnt = 1;
			chk[i] = 1;
			int cur = i;
			while (cur < maxn) {
				cur = dic[hash[cur]].next;
				if (a <= cur && cur <= b && chk[cur] == 0) {
					++cnt;
				}
				if (cur < maxn)
					chk[cur] = 1;
			}

			if (cnt >= 2) {
				ans += cnt * (cnt - 1)/2;
			}
		}
		cout << ans << endl;
	}

	double end_time=(double)clock();
	//printf("%.3lf\n",(end_time-start_time)/CLOCKS_PER_SEC);
    return 0;
}