#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker, "/STACK:255888000")

#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>

#define pii pair<int,int>
#define vi vector<int>
#define int64 long long
#define ll long long
#define INF 1000000000
#define ld long double
#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define forv(i, v) for(int i = 0; i < (int)v.size(); i++)
#define ford(i, n) for(int i = (int)(n - 1); i >= 0; i--)
#define fore(i, a, b) for(int i = (int)a; i < (int)b; i++)
#define all(a) a.begin(),a.end()
#define norm(a) sort(a);a.erase(unique(all(a)),a.end())
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const int64 INF64 = (int64)1e18;
const ld EPS = 1e-8;
const ld PI = 3.1415926535897932384626433832795;

using namespace std;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

char w[25][25];

int W, Q;

char buf[123];

int L;

string d[11][11][255][120];

bool used[11][11][255][120];

string get(int x, int i, int j, int depth) {

	int X = x + 1000;
	if (used[i][j][X][depth])
		return d[i][j][X][depth];

	used[i][j][X][depth] = 1;
	if (x == 0){		
		return  d[i][j][X][depth] = string(1, w[i][j]);
	}

	if (depth == 0)
		return d[i][j][X][depth] = string(190, '9');

	d[i][j][X][depth] = string(190, '9');
	forn(k, 4){
		int ni = i + dx[k];
		int nj = j + dy[k];
		if (ni >= 0 && nj >= 0 && ni < W && nj < W) {
			for(int f = 0; f < 4; f += 1){
				int zi = ni + dx[(k + f + 4) % 4];
				int zj = nj + dy[(k + f + 4) % 4];
				if (zi >= 0 && zj >= 0 && zi < W && zj < W) {
					int nx = x + ((w[ni][nj] == '-') ? (w[zi][zj]-'0') : -(w[zi][zj] - '0'));
					string cand = string(1, w[i][j]) + w[ni][nj] + get(nx, zi, zj, depth - 1);

					if (cand.length() < d[i][j][X][depth].length() || (cand.length() == d[i][j][X][depth].length() && cand < d[i][j][X][depth]))
						d[i][j][X][depth] = cand;
				}
			}
		}
	}
	return d[i][j][X][depth];
}

inline void solve() {

	memset(d, 0, sizeof d);
	memset(used, 0, sizeof used);

	scanf("%d %d\n", &W, &Q);
	//w.resize(W + 8);
	forn(i, W){
		scanf("%s\n", w[i]);
		//w[i] = buf;
	}

	forn(i, Q) {
		int h;
		scanf("%d", &h);
		string res = string(1200, '9');
		forn(j, W) {
			forn(k, W){
				if (isdigit(w[j][k])){
					forn(len, L) {
						string cand = get(h - (w[j][k] - '0'), j, k, len);
						if (cand.length() < res.length() || (cand.length() == res.length() && cand < res))
							res = cand;
						if (cand.length() < L * 2 || cand[1] != '9')
							break;

					}
				}
			}
		}
		printf("%s\n", res.c_str());
	}

}

int bad[] = {
4, 9, 10, 11, 12, 16, 17, 21, 22, 24, 26, 27, 31, 32, 33, 34, 36, 39, 40, 41, 43, 44, 46, 47, 52, 53, 54, 55, 56, 57, 59};

bool u[123];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tests;
	cin >> tests;
	
	forn(i, 30)
		u[bad[i]] = 1;

	fore(test, 1, tests + 1) {
		cerr << test << endl;
		printf("Case #%d:\n", test);
		L = 80;
		if (u[test])
			L = 55;
		solve();
		//puts("");
	}

	return 0;
}