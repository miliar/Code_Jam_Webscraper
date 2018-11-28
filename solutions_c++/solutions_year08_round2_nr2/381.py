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


const int MAX = 1010;

int caso;

int A, B, P;

int pai[MAX];

int Find (int a) {
	if (pai[a] != a)
		pai[a] = Find (pai[a]);

	return pai[a];
}

void Union (int a, int b) {
	pai[Find (a)] = Find(b);
}

set <int> fatores (int n) {
	set <int> r;
	
	//printf ("Fatores de %d --> ", n);

	while ((n % 2) == 0) {
		r.insert (2);
		n /= 2;
	}

	for (int p = 3; p * p <= n; p += 2) {
		while ((n % p) == 0) {
			r.insert (p);
			n /= p;
		}
	}
	r.insert (n);

	//FOREACH (it, r) { printf ("%d ", *it); } printf ("\n");

	return r;
}



void processa () {
	for (int i = A; i <= B; i++) {
		pai[i] = i;
	}
	for (int i = A; i <= B; i++) {
		for (int j = i + 1; j <= B; j++) {
			set <int> fi = fatores (i);
			set <int> fj = fatores (j);

			FOREACH (it, fi) {
				if (*it < P)
					continue;
				//printf ("*%d\n", *it);
				if (fj.count (*it)) {
					Union (i, j);
					break;
				}
			}
		}
	}

	set <int> ret;
	for (int i = A; i <= B; i++) {
		ret.insert (Find (i));
	}
	
	// resposta
	printf ("Case #%d: %d\n", caso, ret.size ());
}

void le () {
	scanf ("%d %d %d", &A, &B, &P);
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
