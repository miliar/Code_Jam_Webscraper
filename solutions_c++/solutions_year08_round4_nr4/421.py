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

#define MAXN (1 << 10)
#define INF (1 << 30)
	char s[MAXN], t[MAXN];


int count(char s[MAXN]) {
	int ret = 1;
	for (int i = 1; i < strlen(s); i++) {
		if (s[i - 1] != s[i]) {
			ret++;
		}
	}
	return ret;
}


int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		printf("Case #%d: ", test);
		int k;
		scanf("%d\n", &k);
		gets(s);

		int a[MAXN];
		for (int i = 0; i < k; i++) {
			a[i] = i;	
		}

		int ans = INF;
		
		do {
			strcpy(t, s);
			for (int i = 0; i < strlen(t); i += k) {
				for (int j = 0; j < k; j++) {
					t[i + j] = s[i + a[j]];
				}
			}
			ans = MIN(ans, count(t));
		} while (next_permutation(a, a + k));
		printf("%d", ans);
		printf("\n");
	}

	return 0;
}
