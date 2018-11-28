#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <stack>
#include <map>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <fstream>
#include <cassert>
using namespace std;
 
#ifdef MYDEBUG
#pragma comment(linker, "/stack:1000000000")
#endif

typedef pair<int, int> PII;
typedef long long LL;
typedef unsigned long long ULL;
 
#define MAX(a, b) ((a >= b) ? a : b)
#define MIN(a, b) ((a <= b) ? a : b)
#define ABS(a) ((a < 0) ? -(a) : a)
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define sz size()
#define mp make_pair
#define pb push_back
#define HAS(S, v) ((S).find(v) != (S).end())
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define CLR(a, b) memset(a, b, sizeof(a))
#define sqr(a) ((a) * (a))
#define V(t) vector<t>
#define VV(t) V(V(t))

V(int) mas;
bool chk(int sum, int p, int s) {
	if (s) {
		sum -= p;
		if (p >= 2) sum -= 2 * (p - 2);
		return sum >= 0;
	} else {
		sum -= p;
		if (p) sum -= 2 * (p - 1);
		return sum >= 0;
	}
}
int main() {
#ifdef MYDEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    clock_t beg = clock();
#endif

	int T;
	scanf("%d", &T);
	FOR (t, 0, T) {
		mas.clear();
		printf("Case #%d: ", t + 1);
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		mas.resize(n);
		FOR (i, 0, n)
			scanf("%d", &mas[i]);
		sort(RALL(mas));
		int count = 0;
		FOR (i, 0, n)
			if (chk(mas[i], p, 0))
				++count;
			else if(chk(mas[i], p, 1) && s) {
				--s;
				++count;
			} else break;
		printf("%d\n", count);
	}

#ifdef MYDEBUG
    fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0 * (clock() - beg) / CLOCKS_PER_SEC);
#endif
	return 0;
}
