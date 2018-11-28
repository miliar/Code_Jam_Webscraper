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

const int MAX = 2001;

int caso;

int n, m;
int G[MAX][MAX][2];
int g[MAX];

void printMasc (int masc, bool f) {
	int cnt = 0;
	while (masc > 0) {
		printf ("%d ", masc % 2);
		masc /= 2;
		cnt++;
	}
	while (cnt < n) {
		printf ("0 ");
		cnt++;
	}
	if (f) printf ("\n");
}

void processa () {
	int i, j, masc, ret = MAX, melhor;

	for (masc = 0; masc < (1 << n); masc++) {
		//printMasc (masc, true);
		for (i = 0; i < m; i++) {
			bool ok = false;
			for (j = 0; j < g[i]; j++) {
				if (G[i][j][1]) {
					ok |= (masc & (1 << G[i][j][0])) != 0;
				}
				else {
					ok |= (masc & (1 << G[i][j][0])) == 0;
				}
			}
			//printf ("%d %s\n", i, ok ? "ok" : "nao");
			if (!ok)
				break;
		}	
		if (i == m) {
			int cnt = 0, t = masc;
			while (t > 0) {
				cnt += (t % 2);
				t   /= 2;
			}
			if (cnt < ret) {
				ret    = cnt;
				melhor = masc;
			}
		}
	}

	// resposta
	printf ("Case #%d: ", caso);

	if (ret == MAX) {
		printf ("IMPOSSIBLE\n");
		return;
	}
	printMasc (melhor, true);
}

void le () {
	scanf ("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		scanf ("%d", &g[i]);
		for (int j = 0; j < g[i]; j++) {
			int x, y;
			scanf ("%d %d", &x, &y);
			G[i][j][0] = x - 1;
			G[i][j][1] = y;
		}
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
