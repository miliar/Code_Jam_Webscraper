#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#define _CRT_SECURE_NO_DEPRECATE
using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double

#define PII pair <int, int>

#define x first
#define y second

const int MAXN = 400;
const ld EPS = 1e-9;

char tmp[MAXN];
string s;
int n;
int a[MAXN];

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	int tk;
	cin >> tk;

	forn(test, tk){
		cin >> n;

		forn(i, n){
			scanf("%s", &tmp);
			s = tmp;
			a[i] = 0;
			forn(j, n){
				if (s[j] == '1') a[i] = j;
			}
		}

		int ans = 0;

		forn(i, n){
			if (a[i] <= i) continue;

			int idx = -1;

			fore(j, i + 1, n){
				if (a[j] <= i){
					idx = j;
					break;
				}
			}

			for(int j = idx; j > i; --j){
				swap(a[j], a[j - 1]);
				++ans;
			}
		}

		printf("Case #%d: %d\n", test + 1, ans);
		
	}

	return 0;
};