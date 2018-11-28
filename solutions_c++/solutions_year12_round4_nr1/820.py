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
#include <iostream>
using namespace std;

#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FORE(_i,_a,_b) for((_i)=(_a);(_i)<=(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
#define ADJ(_i,_v) for((_i)=kick[_v];(_i)>=0;(_i)=foll[_i])
#define I64 "%I64d"

typedef long long i64;
typedef unsigned long long u64;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;
typedef complex<double> cd;

template<typename T>inline bool remin(T&c,const T&n){if(n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remin2(T&c,const T&n){if(c<0||n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}
template<typename T>inline void addmod(T&c,const T&n,const T&m){c = (c + n) % m;}

int _in;int in(){scanf("%d",&_in);return _in;}

// stuff cutline

const int N = 1e4 + 5;

bool used[N][N];

i64 d[N], l[N], n, dest, longest[N];

queue<int> qu;

bool solve() {
    while (!qu.empty()) qu.pop();
    qu.push(0);
    qu.push(1);
    used[0][1] = true;
    int a, b, i, j;
    i64 span;
    while (!qu.empty()) {
        a = qu.front(); qu.pop();
        b = qu.front(); qu.pop();
        span = min(d[b] - d[a], l[b]);
        if (span < longest[b]) continue;
        longest[b] = span;
        if (d[b] + span >= dest) return true;
        i = upper_bound(d, d + n + 1, d[b]) - d;
        j = upper_bound(d, d + n + 1, d[b] + span) - d;
        for (; --j >= i; ) {
            if (!used[b][j]) {
                used[b][j] = true;
                qu.push(b);
                qu.push(j);
            }
        }
    }
    return false;
}

int main() {
	/**/
	freopen("C:\\Users\\Dvorak\\Downloads\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Dvorak\\Desktop\\out.txt", "w", stdout);
	/**/
	int t = in(), it, i;
    d[0] = 0;
	FORE(it, 1, t) {
        C(used, 0);
        C(longest, 0);
        n = in();
        FORE (i, 1, n) scanf(I64 I64, d + i, l + i);
        dest = in();
		printf("Case #%d: %s\n", it, solve() ? "YES" : "NO");
	}
	return 0;
}