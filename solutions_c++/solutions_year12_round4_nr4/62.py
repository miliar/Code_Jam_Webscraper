#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <fstream>
#include <iostream>
#include <queue>
#include <algorithm>
#include <time.h>
#include <sstream>
#include <assert.h>
#include <limits>
#define _USE_MATH_DEFINES
#include <math.h>

#define pb(a) push_back(a)
#define sz size()
#define ALL(a) a.begin(),a.end()
#define ALLR(a) a.rbegin(),a.rend()
#define X first
#define Y second
#define mp(a,b) make_pair(a,b)

typedef long long ll;
typedef long double ld;

template<typename T> inline void SWAP(T &a, T &b) {
	T tmp = a;
	a = b;
	b = tmp;
}
template<typename T> inline T ABS(const T &VAL) {
	return VAL < 0 ? -VAL : VAL;
}
template<typename T> inline T MAX(const T &a, const T &b) {
	return a < b ? b : a;
}
template<typename T> inline T MIN(const T &a, const T &b) {
	return a < b ? a : b;
}
template<typename T> inline T SQR(const T &a) {
	return a * a;
}

#define MSET(d) memset(d,0,sizeof(d))
#define forn(i,n) for(int i=0;i!=n;i++)
#define for1(i,n) for(int i=1;i<=n;i++)
#define forab(i,a,b) for(int i=a;i!=b;i++)
#define for1ab(i,a,b) for(int i=a+1;i<=b;i++)
#define fordab(i,a,b) for(int i=b-1;i>=a;i--)
#define ford1ab(i,a,b) for(int i=b;i!=a;i--)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)

//const int INTinf = 2147483647;
const int INTinf = 1000000005;
const int nINTinf = 0 - 2147483648;
const ll LLinf = 9223372036854775807LL;

using namespace std;
typedef pair<int, int> pii;
typedef unsigned int uint;

int t, n, m;
char a[64][64];
bool met[64][64];
bool met2[64][64];
int answ[11];
bool lucky[11];
int mx;
inline void clear() {
	forn(i,n) {
		forn(j,m) {
			met2[i][j] = false;
		}
	}
}
struct node {
	bool isEnd;
	map<pii, node*> nodes;
	~node() {
		clean();
	}
	void clean() {
		for (map<pii, node*>::iterator it = nodes.begin(); it != nodes.end(); it++) {
			delete it->Y;
		}
		nodes.clear();
		isEnd = false;
	}
};
node root;
map<pii, node*>::iterator pam;
node *pam2;
inline bool not_was(const vector<pii> &vc) {
	node* now = &root;

	forn(i,vc.sz) {
		if ((pam = now->nodes.find(vc[i])) != now->nodes.end()) {
			now = pam->Y;
		} else {
			pam2 = new node();
			now->nodes.insert(make_pair(vc[i], pam2));
			now = pam2;
		}
	}
	if (now->isEnd) {
		return false;
	}
	return now->isEnd = true;
}
bool dfs(const vector<pii> &vc) {
	if (vc.sz == 1) {
		return true;
	}
	vector<pii> vc2;
	clear();
	forn(i, vc.sz) {
		if (a[vc[i].X][vc[i].Y - 1] != '#') {
			if (!met2[vc[i].X][vc[i].Y - 1]) {
				met2[vc[i].X][vc[i].Y - 1] = true;
				vc2.pb(pii(vc[i].X, vc[i].Y-1));
			}
		} else {
			if (!met2[vc[i].X][vc[i].Y]) {
				met2[vc[i].X][vc[i].Y] = true;
				vc2.pb(pii(vc[i].X, vc[i].Y));
			}
		}
	}

	sort(ALL(vc2));
	if (not_was(vc2)) {
		if (dfs(vc2)) {
			return true;
		}
	}

	clear();
	vc2.clear();
	forn(i, vc.sz) {
		if (a[vc[i].X][vc[i].Y + 1] != '#') {
			if (!met2[vc[i].X][vc[i].Y + 1]) {
				met2[vc[i].X][vc[i].Y + 1] = true;
				vc2.pb(pii(vc[i].X, vc[i].Y + 1));
			}
		} else {
			if (!met2[vc[i].X][vc[i].Y]) {
				met2[vc[i].X][vc[i].Y] = true;
				vc2.pb(pii(vc[i].X, vc[i].Y));
			}
		}
	}

	sort(ALL(vc2));
	if (not_was(vc2)) {
		if (dfs(vc2)) {
			return true;
		}
	}

	clear();
	vc2.clear();
	forn(i, vc.sz) {
		if (a[vc[i].X + 1][vc[i].Y] != '#') {
			if (!met[vc[i].X + 1][vc[i].Y]) {
				return false;
			}
			if (!met2[vc[i].X + 1][vc[i].Y]) {
				met2[vc[i].X + 1][vc[i].Y] = true;
				vc2.pb(pii(vc[i].X + 1, vc[i].Y));
			}
		} else {
			if (!met2[vc[i].X][vc[i].Y]) {
				met2[vc[i].X][vc[i].Y] = true;
				vc2.pb(pii(vc[i].X, vc[i].Y));
			}
		}
	}
	sort(ALL(vc2));
	if (not_was(vc2)) {
		return dfs(vc2);
	}
	return false;
}
void proceed(int x, int y) {
	queue<pii> q;
	vector<pii> reached;
	q.push(pii(x, y));
	forn(i,n) {
		forn(j,m) {
			met[i][j] = false;
		}
	}
	met[x][y] = true;
	int val = a[x][y] - '0';
	mx = MAX(val, mx);
	while (!q.empty()) {
		pii top = q.front();
		reached.pb(top);
		q.pop();
		if (a[top.X - 1][top.Y] != '#' && !met[top.X - 1][top.Y]) {
			met[top.X - 1][top.Y] = true;
			q.push(pii(top.X - 1, top.Y));
		}
		if (a[top.X][top.Y - 1] != '#' && !met[top.X][top.Y - 1]) {
			met[top.X][top.Y - 1] = true;
			q.push(pii(top.X, top.Y - 1));
		}
		if (a[top.X][top.Y + 1] != '#' && !met[top.X][top.Y + 1]) {
			met[top.X][top.Y + 1] = true;
			q.push(pii(top.X, top.Y + 1));
		}
	}
	answ[val] = reached.sz;
	sort(ALL(reached));
	root.clean();
	not_was(reached);
	lucky[val] = dfs(reached);
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);
#endif
	cin >> t;
	for1(x,t) {
		cin >> n >> m;
		forn(i,n) {
			cin >> a[i];
		}
		mx = -1;
		forn(i,n) {
			forn(j,m) {
				if (a[i][j] != '.' && a[i][j] != '#') {
					proceed(i, j);
				}
			}
		}
		cout << "Case #" << x << ":" << endl;
		mx++;
		forn(i, mx) {
			cout << i << ": " << answ[i];
			if (lucky[i]) {
				cout << " Lucky" << endl;
			} else {
				cout << " Unlucky" << endl;
			}
		}
	}

#ifndef ONLINE_JUDGE
	fclose(stdout);
	fclose(stdin);
#endif
	return 0;
}
