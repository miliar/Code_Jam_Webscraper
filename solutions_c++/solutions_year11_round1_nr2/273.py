// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("in.txt", "r", stdin); 
	freopen("b.out", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

const uint P = 3731;

struct node {
	uint h;
	node * ne;	
	int lets;
};

typedef node * tnode;

node hh[10000 * 1151];
int chh = 0;
tnode ht[11][1 << 10][1 << 10];
bool was[11][1<<10][1<<10];

int getpos(uint h) {
	return (h & ((1 << 10) - 1));
}

char s[10004][14];

void inith() {
	fi(11) {
		fj(1 << 10) fk(1 << 10) {
			was[i][j][k] = false;
			ht[i][j][k] = NULL;
		}
	}
}

void add(int len, int mask, int nmask, uint h) {
	tnode t = & hh[chh++];
	t->h = h;
	t->lets = mask;
	int pos = getpos(h);
	t->ne = ht[len][nmask][pos];
	was[len][nmask][pos] = true;
	ht[len][nmask][pos] = t;
}

int L[10004];

bool correct(int id, int mask) {
	int mm = 0;
	fi(L[id]) {
		if (mask & (1 << i)) {
			mm |= (1 << (s[id][i] - 'a'));
		}
	}
	fi(L[id]) {
		if (!(mask & (1 << i))) {
			if (mm & (1 << (s[id][i] - 'a'))) {
				return false;
			}
		}
	}
	return true;
}

void doHash(int id) {
	int len = L[id];
	int mask = 0;
	uint h = 0;
	fi(len) {
		mask |= (1 << (s[id][i] - 'a'));
	}
	fi(1 << len) {
		if (correct(id, i)) {
			h = 0;
			fj(len) {
				if (i & (1 << j)) {
					h = h * P + (s[id][j] - 'a' + 1);
				}
			}
    		add(len-1, mask, i, h);
		}
	}
}

char t[30];
int n, m;

void addMaskAndHash(int id, char c, int & mask, uint & h) {
	h = 0;
	fi(L[id]) {
		if (c == s[id][i]) {
			mask |= (1 << i);
		}
		if (mask & (1 << i)) {
			h = h * P + (s[id][i] - 'a' + 1);
		}
	}
}

bool have(int bit, int len, int mask, uint h, int gg) {
	--len;
	int pos = getpos(h);
	if (!was[len][mask][pos]) {
		return false;
	}
	for (tnode t = ht[len][mask][pos]; t != NULL; t = t->ne) {
		if (t->h == h && (t->lets & (1 << bit)) && ((gg & t->lets) == 0)) {
			return true;
		}
	}
	return false;
}

void solve(int test_id) {
	inith();
 	chh = 0;
	printf("Case #%d:", test_id);
	scanf("%d%d", &n, &m);
	fi(n) {
		scanf("%s", s[i]);
		L[i] = strlen(s[i]);
		doHash(i);
 	}	
	while (m--) {
		scanf("%s", t);
		int id = -1;
		int ma = -1;
		
		fi(n) {
			int let_mask = 0;

			int guessed = 0;

			fk(L[i]) {
				let_mask |= (1 << (s[i][k] - 'a'));
			}	
			int cmask = 0;
			uint ch = 0;
			int cur = 0;
			fk(26) {
				if (let_mask & (1 << (t[k]-'a'))) {
					//guessed |= (1 << (t[k] - 'a'));
					addMaskAndHash(i, t[k], cmask, ch);
					if (cmask == (1 << L[i]) - 1) {
						break;
					}
				} else {
					char c = t[k];
					if (have(t[k]-'a', L[i], cmask, ch, guessed)) {
						++cur;
					}
					guessed |= (1 << (t[k] - 'a'));
				}
			}
			if (ma < cur) {
				ma = cur;
				id = i;
			}
		}
		printf(" %s", s[id]);
	}
	printf("\n");
 	
}

int main() {
	initf();
	int T, i;
	scanf("%d", &T);
	for (i = 1; i <= T; ++i) { 
		solve(i);
	}
	return 0;
}
