#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#pragma comment (linker, "/STACK:99000111")

#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <ctime>
#include <cassert>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)a; i < (int)b; ++i)
#define ford(i, n) for(int i = (int)(n - 1); i >= 0; --i)
#define forv(i, v) for(int i = 0; i < (int)(v.size()); ++i)
#define fs first 
#define sc second
#define mp make_pair
#define pb push_back
#define last(a) a[a.size() - 1]
#define all(a) a.begin(), a.end()
#define norm(a) sort(all(a));a.erase(unique(all(a)), a.end())
#define sz(a) a.size()
#define vi vector<int>
#define pii pair<int,int>

#define INF 1000 * 1000 * 1000
#define EPS 1e-9
#define MAXN 1001

using namespace std;

bool u[16][53];

string s[5100], t;

int L, m, n;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin >> L >> m >> n;
	forn(i, m)
		cin >> s[i];

	forn(i, n){
		cin >> t;
		int p = 0, k = 0;
		memset(u, 0, sizeof u);
		while(p < (int)t.size()){
			if (t[p] != '(') {
				u[k][t[p] - 'a'] = 1;
				p++, k++;
			}else{
				p++;
				while (t[p] != ')') {
					u[k][t[p] - 'a'] = 1;
					p++;
				}
				p++, k++;
			}
		}
		int res = 0;
		forn(j, m){
			int add = 1;
			forn(pp, L) {
				if (!u[pp][s[j][pp] - 'a']) {
					add = 0;
					break;
				}
			}
			res += add;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}



	return 0;
}