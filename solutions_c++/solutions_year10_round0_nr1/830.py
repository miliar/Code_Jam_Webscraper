#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define For(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,n) For(i,0,n)
#define re return
#define fi first
#define se second
#define y0 y47847892
#define y1 y47824262
#define fill(x, val) memset(x, val, sizeof(x))

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

#pragma comment(linker, "/STACK:16777216")

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n;
int m;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tc;
	cin >> tc;

	rep(tt, tc) {
		cout << "Case #" << tt + 1 << ": ";
		int k;
		cin >> n >> k;

		/*
		int use[1000];
		fill(use, 0);
		rep(i, k) {
			int p = 0;
			while (p < n && use[p]) {
				use[p] = 0;
				p++;
			}
			if (p < n)
				use[p] = 1 - use[p];
		}*/

		if (k % (1 << n) == (1 << n) - 1)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;

	}

	return 0;
}
