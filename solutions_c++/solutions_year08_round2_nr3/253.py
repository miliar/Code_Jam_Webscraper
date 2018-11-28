#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <utility>
#include <numeric>
#include <set>
#include <map>
#include <iostream>

using namespace std;


#define TRACE(x) 
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)
#define DEBUG(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define MSET(c, v) memset(c, v, sizeof(c))
#define FOR(i,a,b) for (int i=(a); i < (b); i++)

/////


set<int> pos;
int k_i[1000010], d_i[1000010];


int get_idx(int x, int l) {
	int sz = pos.size()-1;
	WATCH(x);
	x = x%sz;
	WATCH(x);
	int c=0;
	int val=-1;
	set<int>::iterator init = pos.find(l);
	++init;
	for(set<int>::iterator it=init; it != pos.end(); ++it) {
		WATCH(*it);
		if (c == x) {
			val = *it;
			pos.erase(l);
			break;
		}
		c++;
	}
	if (val != -1) return val;
	DEBUG("procurando idx p/ %d -> wrap around e procura %d!\n", x, x-c);
	pos.erase(l);
	pos.insert(-1);
	return get_idx(x-c, -1);
}


int main () {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		int K, n;
		scanf(" %d", &K);
		scanf(" %d", &n);
		FOR(i,0,n) scanf(" %d", &k_i[i]);
		pos.clear();

		FOR(i,-1,K) pos.insert(i);
		int last = -1;
		for (int i=0; i < K; i++) {
			last = get_idx(i, last);
			d_i[ last ] = i+1;
		}
		FOR(i,0,K) DEBUG("d_i[%d] = %d\n", i, d_i[i]);

		printf("Case #%d:", _42);
		for (int i=0; i < n; i++) {
			printf(" %d", d_i[ k_i[i]-1 ]);
		}
		printf("\n");
	}


	return 0;
}



