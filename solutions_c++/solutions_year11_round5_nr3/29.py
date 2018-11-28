#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

typedef unsigned int dword;

int r, c;
char pict[128][128];

const int SIZE = 10<<10;
const int MOD = 1000003;

int n;
dword matr[SIZE][SIZE/32+1];

inline int Norm(int a, int p) {
	if (a < 0) a += p;
	if (a >= p) a -= p;
	return a;
}

void Xor(dword *arr, int k) {
	arr[k>>5] ^= (1<<(k&31));
}

int Get(dword *arr, int k) {
	return (arr[k>>5] >> (k&31)) & 1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i<r; i++) scanf("%s", pict[i]);

		n = r*c;
		int n32 = n / 32 + 2;
		memset(matr, 0, sizeof(matr));
        for (int i = 0; i<r; i++) {
			for (int j = 0; j<c; j++) {
				int dx, dy;
				if (pict[i][j] == '-') { dx = 0; dy = 1; }
				if (pict[i][j] == '|') { dx = 1; dy = 0; }
				if (pict[i][j] == '/') { dx = 1; dy = -1; }
				if (pict[i][j] == '\\') { dx = 1; dy = 1; }

				int curr = i * c + j;
				int next = Norm(i+dx, r) * c + Norm(j+dy, c);
				int prev = Norm(i-dx, r) * c + Norm(j-dy, c);

				Xor(matr[curr], n);
				Xor(matr[next], n);
				Xor(matr[next], curr);
				Xor(matr[prev], curr);
			}
        }

/*        for (int i = 0; i<n; i++) {
        	for (int j = 0; j<n; j++) printf("%d", Get(matr[i], j));
			printf("=%d\n", Get(matr[i], n));
        } printf("\n");*/

        int r = 0;
        for (int c = 0; c<n; c++) {
        	int i;
			for (i = r; i<n; i++) if (Get(matr[i], c)) break;
			if (i == n) continue;

        	int c32 = c/32;
			for (int j = c32; j<n32; j++) swap(matr[r][j], matr[i][j]);

			for (i = r+1; i<n; i++) if (Get(matr[i], c)) {
				for (int j = c32; j<n32; j++) matr[i][j] ^= matr[r][j];
			}
			r++;
        }

/*        for (int i = 0; i<n; i++) {
        	for (int j = 0; j<n; j++) printf("%d", Get(matr[i], j));
			printf("=%d\n", Get(matr[i], n));
        } printf("\n");*/

        bool ok = true;
        for (int i = r+1; i<n; i++) if (Get(matr[i], n)) ok = false;

        int ans = 0;
        if (ok) {
        	ans = 1;
			for (int i = 0; i<n-r; i++) ans = (ans*2) % MOD;
        }
		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
