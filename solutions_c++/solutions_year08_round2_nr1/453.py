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

const int MAX = 100010;

typedef long long ll;

int caso;
ll p[MAX][2];

int n;
int A, B, C, D, X, Y, M;

void gera () {
	int i;

	for (i = 0; i < n; i++) {
		p[i][0] = X;
		p[i][1] = Y;
#ifdef DEBUG
		printf ("(%d, %d)\n", X, Y);
#endif
		X = ((ll) A * X + B) % M;
		Y = ((ll) C * Y + D) % M;	
	}
}

bool proc (int X, int Y) {
	int i;
	for (i = 0; i < n; i++) {
		if (p[i][0] == X && p[1][1] == Y)
			return true;
	}
	return false;
}

void processa () {
	int i, j, k, l, cnt;

	gera ();
	cnt = 0;

	for (i = 0; i < n; i++) {
		for (j = i + 1; j < n; j++) {
			for (k = j + 1; k < n; k++) {
				ll x = (p[i][0] + p[j][0] + p[k][0]), 
					y = (p[i][1] + p[j][1] + p[k][1]);

				if ((x % 3) == 0 && (y % 3) == 0)
					cnt++;
			
			}
		}
	}

	// resposta
	printf ("Case #%d: %d\n", caso, cnt);
}

void le () {
	scanf ("%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &X, &Y, &M);
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
