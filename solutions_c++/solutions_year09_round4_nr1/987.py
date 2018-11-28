#pragma comment(linker, "/STACK:512000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back


typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1000 + 7;
const ld EPS = 1E-9;


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	int T;
	scanf("%d\n", &T);
	for1(Q, T){
		int n;
		scanf("%d\n", &n);
		string a[50];
		vector<int> b(n, 0);
		forn(i, n){
			getline(cin, a[i]);
			forn(j, n)
				if(a[i][j] == '1') b[i] = j;
		}
		int ans = 0;
		forn(i, n){
			if(b[i] + 1 > (i + 1)){
				int can = -1;
				fore(j, i + 1, n){
					if(b[j] + 1 <= i + 1){
						can = j;
						break;
					}
				}
				int val = b[can];
				b.erase(b.begin() + can);
				b.insert(b.begin() + i, val);
				ans += can - i;
			}
		}
		printf("Case #%d: %d\n", Q, ans);
	}

    return 0;
}
