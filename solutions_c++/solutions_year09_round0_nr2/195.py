#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)
#define cont(s,u) (s.find(u) != s.end())

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }

int T, H, W;
int h[100][100];
int s[100][100];

#define in_map(i,j) ((i >= 0) && (i < H) && (j >= 0) && (j < W))

int dj[4] = {0, -1, 1, 0};
int di[4] = {-1, 0, 0, 1};

int find_sink(int i, int j) {
//	cout << "find_sink " << i << " " << j << endl;
	if (s[i][j] != -1) return s[i][j];
	int ni = i;
	int nj = j;
	rep(k,4) if (in_map(i+di[k], j+dj[k]) && (h[i+di[k]][j+dj[k]] < h[ni][nj])) {
		ni = i + di[k];
		nj = j + dj[k];
	}
	if ((ni != i) || (nj != j)) {
		s[i][j] = find_sink(ni, nj);
		return s[i][j];
	} else {
		s[i][j] = W*i + j;
		return s[i][j];
	}
}


main() {
	cin >> T;

	rep(test, T) {
		cin >> H >> W;
		rep(i,H) rep(j,W) {
			cin >> h[i][j];
			s[i][j] = -1;
		}

		rep(i,H) rep(j,W) if (s[i][j] == -1) {
			find_sink(i,j);
		}

		char next_letter = 'a';
		map<int,char> dic;

		cout << "Case #" << test+1 << ":" << endl;

		rep(i,H) {
			rep (j,W) {
				if (!cont(dic,s[i][j])) dic[s[i][j]] = next_letter++;
				cout << dic[s[i][j]] << " ";
			}
			cout << endl;
		}

	}
}
