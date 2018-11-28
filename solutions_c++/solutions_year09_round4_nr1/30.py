#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstdlib> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include "float.h" 
#include <ctime> 
using namespace std; 

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

const int maxn = 40;
int n;
char a[maxn][maxn+1];

bool isOk(char* s, int r) {
	FOR(i, r+1, n-1)
		if (s[i] == '1')
			return false;
	return true;
}

void swap(char* s1, char* s2) {
	REP(i, n)
		swap(s1[i], s2[i]);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		scanf("%d", &n);
		REP(i, n) {
			scanf("%s", a[i]);
			assert(strlen(a[i]) == n);
		}
		int res = 0;
		REP(i, n) {
			int j = i;
			while (j < n && !isOk(a[j], i))
				++j;
			assert(j < n);
			while (j > i) {
				++res;
				swap(a[j], a[j-1]);
				--j;
			}
		}
		printf("Case #%d: %d\n", test, res);
	}

	exit(0);
}
