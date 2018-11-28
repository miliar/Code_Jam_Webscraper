#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <list>
using namespace std;
 
#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
 
typedef long long i64;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;
 
template<typename T>inline bool remin(T&c,const T&n){if(n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}
template<typename T>inline void addmod(T& c,const T&n,const T&m){c=(c+n)%m;}
 
int _in;int in(){scanf("%d",&_in);return _in;}
 
// stuff cutline

const int N = 1e5 + 5;

double p[N];

int main() {
	freopen("C:\\Users\\anonymous\\Downloads\\A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	double best, cur;
	int t = in(), it, n, k, i;
	FOR (it, t) {
		scanf("%d%d", &k, &n);
		FOR (i, k) scanf("%lf", p + i);
		best = n + 1;
		cur = 1;
		FOR (i, k) {
			remin(best, ((k - i) * 2 + n - k) * cur + ((k - i) * 2 + n - k + 1 + n) * (1 - cur));
			cur *= p[i];
		}
		remin(best, cur * (n - k) + (1 - cur) * (n - k + 1 + n));
		printf("Case #%d: %.10lf\n", it + 1, best + 1);
	}
    return 0;
}