//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 1000000000;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, N, ans = 0, k;
string s;
int a[20];

int fact(int n) {
	if (n == 0) return 1;
	return n * fact(n - 1);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> N;
	forn(test, N) {
		cin >> k >> s;
		int tmp = fact(k);
		forn(i, k) a[i] = i;
		int mi = INF;
		forn(i, tmp) {
			string str = s;
			for (int j = 0; j < s.length() / k; ++j) {
				for (int q = 0; q < k; ++q) {
					str[j * k + q] = s[a[q] + j * k];
				}
			}
			
			int kol = 1;
			for(int j = 1; j < str.length(); ++j) {
				if (str[j] != str[j - 1]) ++kol;
			}
			if (kol < mi) mi = kol;
			next_permutation(a, a + k);
		}
		printf("Case #%d: %d\n", test + 1, mi);
	}
	

	return 0;
}

 
