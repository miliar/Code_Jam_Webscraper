#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define re return
#define fi first
#define se second
#define sqr(x) (x)*(x)
#define sz(x) (x).size ()
#define all(x) x.begin(), x.end ()
#define fill(x,y) std::memset(x,y,sizeof(x))

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;
typedef set<int> si;
typedef map<int, int> mii;

template <class T>T abs (T x) { if (x < 0) return -x; else return x; }

const int di[4] = {1, -1, -1, 1};
const int dj[4] = {1, 1, -1, -1};
const int ddi[4] = {1, -1, 0, 0};
const int ddj[4] = {0, 0, 1, -1};

int get (int j, char c) {
	return int (c == '-') * (- j) + int (c == '+') * j;
}

int qi[4000000], qj[4000000], qk[4000000];
int res[20][20][20000];
string bs[20][20][20000];
char g[21][21];
string cur;
int n;

string out (int i, int j, int k) {
	string tmp = "";
	tmp += char (g[i][j] + '0');
	if (k == 0) return tmp;
	if (bs[i][j][k + 10000] != "") return bs[i][j][k + 10000];
	char sign = '-' + 1;
	int next = 10, mi, mj, mk;
	tmp = "";
	for (int l = 0; l < 4; l++) {
		int ni = i + di[l];
		int nj = j + dj[l];
		if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
			int nk = k - get (g[ni][nj], g[i][nj]);
			if (abs (nk) < 10000 && res[ni][nj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[i][nj] < sign || g[i][nj] == sign && g[ni][nj] < next) {
					sign = g[i][nj];
					next = g[ni][nj];
				}
			}             
			nk = k - get (g[ni][nj], g[ni][j]);
			if (abs (nk) < 10000 && res[ni][nj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][j] < sign || g[ni][j] == sign && g[ni][nj] < next) {
					sign = g[ni][j];           
					next = g[ni][nj];
				}
			}
		}
	}
	for (int l = 0; l < 4; l++) {
		int ni = i + ddi[l];
		int nj = j + ddj[l];
		if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
			int nk = k - get (g[i][j], g[ni][nj]);
			if (abs (nk) < 10000 && res[i][j][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][nj] < sign || g[ni][nj] == sign && g[i][j] < next) {
					sign = g[ni][nj];           
					next = g[i][j];
				}
			}
		}
		int li = i + 2 * ddi[l];
		int lj = j + 2 * ddj[l];
		if (li >= 0 && li < n && lj >= 0 && lj < n) {
			int nk = k - get (g[li][lj], g[ni][nj]);
			if (abs (nk) < 10000 && res[li][lj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][nj] < sign || g[ni][nj] == sign && g[li][lj] < next) {
					sign = g[ni][nj];           
					next = g[li][lj];
				}
			}
		}
	}
	for (int l = 0; l < 4; l++) {
		int ni = i + di[l];
		int nj = j + dj[l];
		if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
			int nk = k - get (g[ni][nj], g[i][nj]);
			if (abs (nk) < 10000 && res[ni][nj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[i][nj] == sign && g[ni][nj] == next) {
					string tmp2 = out (ni, nj, nk);
					if (tmp == "" || tmp > tmp2) tmp = tmp2;
				}
			}             
			nk = k - get (g[ni][nj], g[ni][j]);
			if (abs (nk) < 10000 && res[ni][nj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][j] == sign && g[ni][nj] == next) {
					string tmp2 = out (ni, nj, nk);
					if (tmp == "" || tmp > tmp2) tmp = tmp2;
				}
			}
		}
	}
	for (int l = 0; l < 4; l++) {
		int ni = i + ddi[l];
		int nj = j + ddj[l];
		if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
			int nk = k - get (g[i][j], g[ni][nj]);
			if (abs (nk) < 10000 && res[i][j][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][nj] == sign && g[i][j] == next) {
					string tmp2 = out (i, j, nk);
					if (tmp == "" || tmp > tmp2) tmp = tmp2;
				}
			}
		}
		int li = i + 2 * ddi[l];
		int lj = j + 2 * ddj[l];
		if (li >= 0 && li < n && lj >= 0 && lj < n) {
			int nk = k - get (g[li][lj], g[ni][nj]);
			if (abs (nk) < 10000 && res[li][lj][nk + 10000] + 1 == res[i][j][k + 10000]) {
				if (g[ni][nj] == sign && g[li][lj] == next) {
					string tmp2 = out (li, lj, nk);
					if (tmp == "" || tmp > tmp2) tmp = tmp2;
				}
			}
		}
	}
	string tmp2 = "";
	tmp2 += char (g[i][j] + '0');
	tmp2 += char (sign);
	tmp2 += tmp;
	bs[i][j][k + 10000] = tmp2;
	return tmp2;
}

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 1; it <= tt; it++) {
		int m;
		scanf ("%d%d\n", &n, &m);
		for (int i = 0; i < n; i++)
			scanf ("%s", g[i]);
		fill (res, -1);
		int r = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (g[i][j] != '-' && g[i][j] != '+') {
					g[i][j] -= '0';
					bs[i][j][10000] = "";
					res[i][j][10000] = 0;
					qi[r] = i;
					qj[r] = j;
					qk[r++] = 0;
				}
		int l = 0;
		while (l < r) {
			int i = qi[l];
			int j = qj[l];
			int k = qk[l++];
			bs[i][j][k + 10000] = "";
			for (int l = 0; l < 4; l++) {
				int ni = i + di[l];
				int nj = j + dj[l];
				if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
					int nk = k + get (g[i][j], g[i][nj]);
					if (abs (nk) < 10000 && res[ni][nj][nk + 10000] == -1) {
						res[ni][nj][nk + 10000] = res[i][j][k + 10000] + 1;
						qi[r] = ni;
						qj[r] = nj;
						qk[r++] = nk;
					}    
					nk = k + get (g[i][j], g[ni][j]);
					if (abs (nk) < 10000 && res[ni][nj][nk + 10000] == -1) {
						res[ni][nj][nk + 10000] = res[i][j][k + 10000] + 1;
						qi[r] = ni;
						qj[r] = nj;
						qk[r++] = nk;
					}
				}
			}
			for (int l = 0; l < 4; l++) {
				int ni = i + ddi[l];
				int nj = j + ddj[l];
				if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
					int nk = k + get (g[i][j], g[ni][nj]);
					if (abs (nk) < 10000 && res[i][j][nk + 10000] == -1) {
						res[i][j][nk + 10000] = res[i][j][k + 10000] + 1;
						qi[r] = i;
						qj[r] = j;
						qk[r++] = nk;
					}
				}
				int li = i + 2 * ddi[l];
				int lj = j + 2 * ddj[l];
				if (li >= 0 && li < n && lj >= 0 && lj < n) {
					int nk = k + get (g[i][j], g[ni][nj]);
					if (abs (nk) < 10000 && res[li][lj][nk + 10000] == -1) {
						res[li][lj][nk + 10000] = res[i][j][k + 10000] + 1;
						qi[r] = li;
						qj[r] = lj;
						qk[r++] = nk;
					}
				}
			}
		}
		printf ("Case #%d:\n", it);
		cerr << "Case #" << it << endl;
	        for (int i = 0; i < m; i++) {
	        	int a;
	        	scanf ("%d", &a);
	        	int ans = -1;
	        	for (int j = 0; j < n; j++)
	        		for (int k = 0; k < n; k++)
	        			if (res[j][k][a - g[j][k] + 10000] != -1)
	        				if (ans == -1 || res[j][k][a - g[j][k] + 10000] + 1 < ans)
	        					ans = res[j][k][a - g[j][k] + 10000] + 1;
//	        	printf ("%d %d %d %d\n", 1, 1, 27, res[1][1][19 + 10000]);
//	        	printf ("%d %d %d %d\n", 3, 1, 23, res[3][1][23 + 10000]);
//	        	printf ("%d %d %d %d\n", 4, 2, 18, res[4][2][18 + 10000]);
//	        	printf ("%d %d %d %d\n", 4, 0, 9, res[4][0][9 + 10000]);
//	        	printf ("%d %d %d %d\n", 4, 0, 0, res[4][0][0 + 10000]);
	        	string best = "";
	        	for (int j = 0; j < n; j++)
	        		for (int k = 0; k < n; k++)
	        			if (res[j][k][a - g[j][k] + 10000] != -1)
	        			if (res[j][k][a - g[j][k] + 10000] + 1 == ans) {
	        				cur = out (j, k, a - g[j][k]);
	        				if (best == "" || best > cur) best = cur;
//	        				cout << "   " << cur << endl;
	        			}
	        	cout << best << endl;
	        }                                  
	}                                          
}                
