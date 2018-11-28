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
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
using namespace std;
 
#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
#define ADJ(_i,_v) for((_i)=kick[_v];(_i)>=0;(_i)=foll[_i])
 
typedef long long i64;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;
typedef complex<double> cd;
 
template<typename T>inline bool remin(T&c,const T&n){if(c>n){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}

int _in;int in(){scanf("%d",&_in);return _in;}

// stuff cutline

char m[28] = " yhesocvxduiglbkrztnwjpfmaq", buf[1000];

int main() {
	freopen("C:\\Users\\anonymous\\Downloads\\A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, it, i;
	scanf("%d\n", &t);
	for (it = 1; it <= t; ++it) {
		gets(buf);
		printf("Case #%d: ", it);
		for (i = 0; buf[i] != '\0'; putchar(buf[i++]))
			if (buf[i] != ' ')
				buf[i] = m[buf[i] & 0x1f] | 0x60;
		putchar('\n');
	}
    return 0;
}
