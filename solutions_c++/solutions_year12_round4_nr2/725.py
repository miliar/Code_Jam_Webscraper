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

const int N = 1000, MI = 1000;

const double eps = 1e-3;

double r[N], x5[N], y5[N];
int n, w, h;

double randDouble() {
    return double((rand() * RAND_MAX) + rand()) / (RAND_MAX * RAND_MAX);
}

bool place() {
    int i, j, t;
    FOR (i, n) {
        FOR (t, MI) {
            x5[i] = randDouble() * w;
            y5[i] = randDouble() * h;
            FOR (j, i) {
                if (hypot(x5[i] - x5[j], y5[i] - y5[j]) - eps < r[i] + r[j]) {
                    break;
                }
            }
            if (j == i) break;
        }
        if (t == MI) return false;
    }
    return true;
}

int main() {
	/**/
	freopen("C:\\Users\\Dvorak\\Downloads\\B-small-attempt2.in", "r", stdin);
	freopen("C:\\Users\\Dvorak\\Desktop\\out.txt", "w", stdout);
	/**/
    int t = in(), it, i;
    srand(time(NULL));
	FORE(it, 1, t) {
        scanf("%d%d%d", &n, &w, &h);
        FOR (i, n) r[i] = in();
        sort(r, r + n, greater<double>());
        while (!place());
		printf("Case #%d:", it);
        FOR (i, n) printf(" %.6lf %.6lf", x5[i], y5[i]);
        putchar('\n');
	}
	return 0;
}