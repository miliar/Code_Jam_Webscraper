//	GCJ 2009 Round 1B (B)

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef vector<int> vint;
typedef pair<int,int> pint;
#define mp make_pair

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) throw ~0; } return c; }
int in() {
	int x = 0, c;
	while ((uint)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) throw ~0; }
	do { x = (x << 3) + (x << 1) + (c - '0'); } while ((uint)((c = getchar()) - '0') < 10);
	return x;
}

int L;
char S[30];

int main() {
	int i;
	
	for (int TC = in(), tc = 0; TC--; ) {
		
		scanf("%s", S);
		L = strlen(S);
		
		printf("Case #%d: ", ++tc);
		
		if (next_permutation(S, S + L)) {
			puts(S);
		} else {
			S[L] = '0'; S[L + 1] = 0;
			sort(S, S + L + 1);
			for (i = 0; S[i] == '0'; ++i);
			swap(S[0], S[i]);
			puts(S);
		}
		
	}
	
	
	return 0;
}

