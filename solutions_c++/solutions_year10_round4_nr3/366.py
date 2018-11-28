#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
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

int a[105][105];
int b[105][105];

 int main() {

	 freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);

	 int Tests;
	 scanf("%d", &Tests);

	 for (int Test = 1; Test <= Tests; ++Test) {
		 int R;
		 scanf("%d", &R);

		 memset (a, 0, sizeof(a));
		 int n = 0;

		 for (int i = 0; i < R; ++i) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);

			n = max(n, x2);
			n = max(n, y2);

			for (int j = x1; j <= x2; ++j)
				for (int k = y1; k <= y2; ++k) {
					a[k][j] = 1;
				}
		 }
		 ++n;

		 int time = 0;

		 while (true) {
			memset (b, 0, sizeof(b));

			int haslife = false;

			for (int i = 1; i < n; ++i) {
				for (int j = 1; j < n; ++j) {
					b[i][j] = a[i][j];
					if (a[i][j-1] == 1 && a[i-1][j] == 1) {
						b[i][j] = 1;
					} else if (a[i][j-1] == 0 && a[i-1][j] == 0) {
						b[i][j] = 0;
					}	
					if (b[i][j]) haslife = true;
				}
			}
/*
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					printf ("%d ", b[i][j]);
				}
				printf ("\n");
			}
			printf ("\n");
*/
			++time;
			if (!haslife) break;

			memcpy(a, b, sizeof(b));
		 }
		 printf ("Case #%d: %d\n", Test, time);
	 }

	 return 0;
} 

