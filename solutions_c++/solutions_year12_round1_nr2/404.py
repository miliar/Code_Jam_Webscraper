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

bool pone[N], ptwo[N];

int first[N], second[N], secondDone;

int main() {
	freopen("C:\\Users\\anonymous\\Downloads\\B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = in(), it, n, i, a, b, s, turns, best;
	FOR (it, t) {
		secondDone = turns = s = 0;
		C(pone, 0);
		C(ptwo, 0);
		n = in();
		FOR (i, n) scanf("%d%d", first + i, second + i);
		while (secondDone != n) {
			FOR (i, n)
				if (second[i] <= s && !ptwo[i]) {
					if (pone[i]) ++s;
					else s += 2;
					ptwo[i] = true;
					++secondDone;
					break;
				}
			if (i == n) {
				best = -1;
				FOR (i, n)
					if (first[i] <= s && !ptwo[i] && !pone[i] && (best < 0 || second[best] < second[i]))
						best = i;
				if (best < 0)
					break;
				pone[best] = true;
				++s;
			}
			++turns;
		}
		printf("Case #%d: ", it + 1);
		if (secondDone == n) {
			printf("%d\n", turns);
		} else {
			puts("Too Bad");
		}
	}
    return 0;
}