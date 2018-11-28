#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

string mapa[100];
vector<int> vec[7000];
int M, N;
int m1[7000], m2[7000];
bool v[7000];

inline bool valid(int r, int c) {
	return 0 <= r && r < M && 0 <= c && c < N && mapa[r][c] == '.';
}

inline int id(int r, int c) {
	return r*N+c;
}

bool match(int x) {
	if (x < 0) return true;
	if (v[x]) return false;
	v[x] = true;
	REP(i, SZ(vec[x])) {
		int &der = vec[x][i];
		if (match(m2[der])) {
			m1[x] = der;
			m2[der] = x;
			return true;
		}
	}
	return false;
}

int main() {
	int casos, res;
	cin >> casos;
	REP(caso, casos) {
		res = 0;
		cin >> M >> N;
		REP(r, M) cin >> mapa[r];
		REP(r, M) REP(c, N) if (valid(r,c)) {
			res++;
			int x = id(r,c);
			vec[x].clear();
			if (valid(r-1, c-1)) vec[x].pb(id(r-1, c-1));
			if (valid(r-1, c+1)) vec[x].pb(id(r-1, c+1));
			if (valid(r, c-1)) vec[x].pb(id(r, c-1));
			if (valid(r, c+1)) vec[x].pb(id(r, c+1));
			if (valid(r+1, c-1)) vec[x].pb(id(r+1, c-1));
			if (valid(r+1, c+1)) vec[x].pb(id(r+1, c+1));
		}
		CLEAR(m1, -1); CLEAR(m2, -1);
		REP(r, M) REP(c, N) if (valid(r,c) && (c%2)) {
			CLEAR(v, false);
			if (match(id(r, c))) res--;
			//if (m1[id(r,c)] == -1) printf("%d %d\n", r, c);
		}
		//debug
		/*int k = id(5, 1);
		REP(i, SZ(vec[k])) printf("%d\n", vec[k][i]);*/
		/*int cnt = 0;
		REP(r, M) REP(c, N) if (valid(r,c) && (c%2)) {
			if (m1[id(r,c)] >= 0) {
				int r2 = m1[id(r,c)]/N, c2 = m1[id(r,c)]%N;
				//printf("%d %d %d %d\n", r, c, r2, c2);
				mapa[r][c] = cnt+'A';
				mapa[r2][c2] = cnt+'A';
				cnt++;
			}
		}
		REP(r, M) cout << mapa[r] << endl;*/
		cout << "Case #" << caso+1 << ": " << res << endl;
	}
	return 0;
}
