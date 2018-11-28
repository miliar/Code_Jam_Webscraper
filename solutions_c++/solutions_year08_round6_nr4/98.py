#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef vector< vector<int> > Matrix;

typedef pair<int, int> VertexInfo;
#define index second
#define degree first
bool permTest(int k, const Matrix &g, const Matrix &h,
			  vector<VertexInfo> &gs, vector<VertexInfo> &hs) {
				  const int n = g.size();
				  if (k >= n) return true;
				  for (int i = k; i < n && hs[i].degree == gs[k].degree; ++i) {
					  swap(hs[i], hs[k]);
					  int u = gs[k].index, v = hs[k].index;
					  for (int j = 0; j <= k; ++j) {
						  if (g[u][gs[j].index] != h[v][hs[j].index]) goto esc;
						  if (g[gs[j].index][u] != h[hs[j].index][v]) goto esc;
					  }
					  if (permTest(k+1, g, h, gs, hs)) return true;
esc:swap(hs[i], hs[k]);
				  }
				  return false;
}
bool isomorphism(const Matrix &g, const Matrix &h) {
	const int n = g.size();
	if (h.size() != n) return false;
	vector<VertexInfo> gs(n), hs(n);
	REP(i, n) {
		gs[i].index = hs[i].index = i;
		REP(j, n) {
			gs[i].degree += g[i][j];
			hs[j].degree += h[i][j];
		}
	}
	sort(ALL(gs)); sort(ALL(hs));
	REP(i, n) if (gs[i].degree != hs[i].degree) return false;

	return permTest(0, g, h, gs, hs);
}

int main()
{
	int T;
	cin >> T;
	for (int caseNumber = 1; caseNumber <= T; ++caseNumber){
		int n;
		cin >> n;
		vector<pair<int, int> > v;
		for (int i = 0; i < n - 1; ++i){
			int from, to;
			cin >> from >> to;
			v.push_back(make_pair(from, to));
		}

		int m;
		cin >> m;
		Matrix a(n + 1, vector<int>(n + 1));
		for (int i = 0; i < m - 1; ++i){
			int from, to;
			cin >> from >> to;
			a[from][to] = a[to][from] = true;
		}

		string answer = "NO";
		for (int bit = 1; bit < (1 << n) - 1; ++bit){
			int counter = 0;
			for (int i = 0; i < n; ++i){
				if (bit & (1 << i)){
					++counter;
				}
			}
			if (counter != m){
				continue;
			}

			Matrix b(n + 1, vector<int>(n + 1));
			for (int i = 0; i < n - 1; ++i){
				if (bit & (1 << i)){
					int from = v[i].first;
					int to = v[i].second;
					b[from][to] = b[to][from] = true;
				}
			}

			if (isomorphism(a, b)){
				answer = "YES";
				break;
			}
		}

		cout << "Case #" << caseNumber << ": " << answer << endl;
	}
	return 0;
}
