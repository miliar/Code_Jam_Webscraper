// Includes {{{
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
using namespace std;
// }}}

// Defines úteis {{{
#ifdef DEBUG
#define TRACE(x...) x
#else
#define TRACE(x...) 
#endif
#define PRINT(x...) TRACE(printf (x))
#define WATCH(x) TRACE(cout << #x << ": " << x << endl)
#define SZ(x) ((int) (x).size ())
#define FOREACH(it,c) for (typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it) 
// }}}

const int MAX = 900;

int caso;

int v1[MAX], v2[MAX];
int n;

#ifdef FB
void processa () {
	int ret = (1 << 30);

	if (n > 5) {
		printf ("Case #%d: NAO\n", caso);
		return;
	}

	sort (v1, v1 + n);
	do {
		sort (v2, v2 + n);

		do {
			int atual = 0;
			for (int i = 0; i < n; i++) {
				atual += v1[i] * v2[i];
			}
#ifdef DEBUG
			if (ret > atual) {
				for (int i = 0; i < n; i++) {
					printf ("[%d|%d] ", v1[i], v2[i]);
				}
				printf ("\n");
			}
#endif
			ret = min (ret, atual);
		} while (next_permutation (v2, v2 + n));

	} while (next_permutation (v1, v1 + n));

	printf ("Case #%d: %d\n", caso, ret);
}
#else
void processa () {
	sort (v1, v1 + n);
	sort (v2, v2 + n);

	long long ret = 0;
	for (int i = 0; i < n; i++) {
		ret += v1[i] * v2[n - i - 1];
	}
	printf ("Case #%d: %lld\n", caso, ret);
}
#endif

void le () {
	scanf ("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf ("%d", &v1[i]);
	}
	for (int i = 0; i < n; i++) {
		scanf ("%d", &v2[i]);
	}

}

// Função main {{{
int main()
{
	int casos; scanf ("%d", &casos);

	for (caso = 1; caso <= casos; caso++) {
		le ();
		processa ();
	}

	return 0;
} 
// }}}
