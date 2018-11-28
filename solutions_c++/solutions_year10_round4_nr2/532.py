#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#define mp make_pair
using namespace std;

int perde [10000];
int pd [100000][20];
int preco[100000];
int p;
int n;

int go (int ini, int fim, int pos, int tick) {
	if (fim == ini+1) return tick >= p-perde[ini]? 0 : -1;;
	if (pd[pos][tick] != -1) return pd[pos][tick];
	
	int res = -1;
	int med = (fim+ini)/2;
	int r1 = go (ini, med, 2*pos+1, tick);
	int r2 = go (med, fim, 2*pos+2, tick);
	if (r1 >= 0 && r2 >= 0) res = r1 + r2;
	r1 = go (ini, med, 2*pos+1, tick+1);
	r2 = go (med, fim, 2*pos+2, tick+1);
	if (r1 >= 0 && r2 >= 0) {
		if (res < 0 || res > r1 + r2 + preco[pos]) res = r1 + r2 + preco[pos];
	}
	//printf ("%d~%d (%d) = %d\n", ini, fim, tick, res);
	return pd[pos][tick] = res;
}


int read () {
	scanf ("%d", &p);
	n = 1<<p;
	for (int i = 0; i < n; ++i) {
		scanf ("%d", &perde[i]);
	}
	
	
	for (int i = 0; i < p; ++i) {
		int lim = 1 << (p-i-1);
		for (int j = 0; j < lim; ++j) {
			scanf ("%d", &pd[j][i]);
		}
	}
	
	int ind = 0;
	for (int i = p-1; i >= 0; --i) {
		int lim = 1 << (p-i-1);
		for (int j = 0; j < lim; ++j) {
			preco [ind++] = pd[j][i];
			//printf ("preco[%d] = %d\n", ind-1, pd[j][i]);
		}
	}
}

int caso = 1;
void process () {
	memset (pd, -1, sizeof (pd));
	//memset (preco, 1, sizeof (preco));
	printf ("Case #%d: %d\n", caso++, go (0, n, 0, 0));
}

int main () {
	int t;
	scanf ("%d", &t);
	
	
	while (t--) { read(); process(); }
	return 0;
}

