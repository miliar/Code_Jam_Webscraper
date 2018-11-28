#pragma comment(linker,"/STACK:256000000")

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

#define MAXN (90000)

int scan() {
	int h, m;
	scanf("%d:%d", &h, &m);
	int ret = h * 60 + m;
	return ret;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int test = 0; test < tests; test++) {
		int ansa = 0, ansb = 0, t;
		int na, nb;
		int a[MAXN], b[MAXN];
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d\n", &t);
		scanf("%d %d\n", &na, &nb);
		for (int i = 0; i < na; i++) {
			int t1, t2;
			t1 = scan();
			t2 = scan() + t;
			a[t1]++;
			b[t2]--;
			scanf("\n");
		}
		for (int i = 0; i < nb; i++) {
			int t1, t2;
			t1 = scan();
			t2 = scan() + t;
			b[t1]++;
			a[t2]--;
			scanf("\n");
		}
		int cnta = 0, cntb = 0;
		for (int i = 0; i < MAXN; i++) {
			cnta += a[i];
			ansa = MAX(ansa, cnta);
			cntb += b[i];
			ansb = MAX(ansb, cntb);
		}
		printf("Case #%d: %d %d\n", test + 1, ansa, ansb);
	}

	return 0;
}
