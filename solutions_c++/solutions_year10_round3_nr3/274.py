#include <algorithm>  
#include <iostream>  
#include <cstring>  
#include <ctype.h>  
#include <sstream>  
#include <cstdio>  
#include <string>
#include <vector>  
#include <cmath>  
#include <queue>  
#include <map>  
#include <set>  

using namespace std;  

typedef long long i64;
typedef unsigned long long u64;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(),(a).end()
#define mset(a,byteval) memset(a, byteval, sizeof(a))
#define ff(i,b) for(i=0;i<(b);++i)
#define fr(i,a,b) for(i=(a);i<(b);++i)

int n, m;
bool good (int a[][40], int used[][40], int I, int J, int K) {
	int first = a[I][J] + I + J;
	if (I+K > m || J+K > n) return false;
	for (int i = I; i < I+K; ++i) for (int j = J; j < J+K; ++j) {
		if (used[i][j]) return false;
		if (a[i][j] != ( (i+j+first)&1 )) {
			return false;
		}
	}
	return true;
}
 int main() {

	 
	 freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	 int T;
	 scanf("%d", &T);

	 for (int test = 1; test <= T; ++test) {
		 scanf("%d%d", &m, &n);

		 char s[40][40];
		 int res[40] = {0};

		 for (int i = 0; i < m; ++i) {
			scanf("%s", s[i]);
		 }

		 int a[40][40] = {0}, used[40][40] = {0};
		 for (int i = 0; i < m; ++i) {
			 for (int j = 0; j < n; j += 4) {
				 char c = s[i][j/4];
				 int val = 0;
				 if (c >= '0' && c <= '9') val = c - '0';
				 else val = c - 'A' + 10;

				a[i][j+3] = val & 1;
				a[i][j+2] = val & 2;
				a[i][j+1] = val & 4;
				a[i][j+0] = val & 8;
			 }
		 }
		 for (int i = 0; i < m; ++i) {
			 for (int j = 0; j < n; ++j) {
				if (a[i][j] > 0) a[i][j] = 1;
			 }
		 }
		 int maxsize = min(n,m);

		 while (true) {
			 int best = 0, bi, bj;
			 for (int i = 0; i < m; ++i) {
				 for (int j = 0; j < n; ++j) {
					if (used[i][j] == 1) continue;

					for (int k = 1; k <= maxsize; ++k) {
						if (good(a, used, i, j, k)) {
							if (best < k) {
								best = k;
								bi = i;
								bj = j;
							}
						}
						else break;
					}
				 }
			 }
			 if (best == 0) break;

			 for (int i = bi; i < bi+best; ++i) {
				 for (int j = bj; j < bj+best; ++j) {
					 used[i][j] = 1;
				 }
			 }

			 res[best]++;
		 }
		 int ans1 = 0;
		 for (int i = 1; i <= maxsize; ++i)
			 if (res[i] > 0) ++ans1;

		 printf ("Case #%d: %d\n", test, ans1);

		 for (int i = maxsize; i >= 1; --i) {
			if (res[i] > 0) printf ("%d %d\n", i, res[i]);
		 }

	 }
	 return 0;
} 

