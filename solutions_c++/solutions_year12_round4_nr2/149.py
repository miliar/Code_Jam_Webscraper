#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cerr << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

#define MAXN 1200

int t, T, N, W, H;
int R[MAXN];
int posx[MAXN], posy[MAXN];
bool cmpi(int i1, int i2) { return R[i1] > R[i2]; }
typedef multiset<int, bool(*)(int,int)> tt;
tt todo(cmpi);

void place(int x, int y, int width, bool openLeft, bool openTop, bool openRight) {
	//fprintf(stderr, "place %d %d %d %d %d %d\n", x, y, width, openLeft, openTop, openRight);
	if (todo.empty()) return;
	int tr = (openRight && openLeft) ? INF : (openRight || openLeft) ? width : width/2;
	tr = min(tr, openTop ? INF : H-y);
	tt::iterator it = todo.begin();
	while (it != todo.end() && R[*it] > tr) ++it;
	if (it == todo.end()) return;
	int i = *it;
	//{DEBUG(i);DEBUG(R[i]);}
	todo.erase(it);
	posx[i] = x+R[i]; posy[i] = y+R[i];
	if (openLeft) posx[i] = 0;
	if (openTop) posy[i] = 0;
	int xsh = openLeft ? R[i] : 2*R[i];
	int ysh = openTop  ? R[i] : 2*R[i];
	place(x, y+ysh, xsh, openLeft, false, false);
	place(x+xsh, y, width-xsh, false, openTop, openRight);
}

double dist(int i1, int i2) {
	double dx = posx[i1]-posx[i2];
	double dy = posy[i1]-posy[i2];
	return sqrt(dx*dx+dy*dy);
}

int main() {
	scanf("%d", &T);
	t = 0;
	while (t < T) {
		++t;
		scanf("%d%d%d", &N, &W, &H);
		REP(i,N) scanf("%d", R+i);
		todo.clear();
		REP(i,N) todo.insert(i);
		place(0, 0, W, true, true, true);
		if (!todo.empty()) {
			fprintf(stderr, "FAIL\n");
			return 1;
		}
		REP(i,N) REP(j,N) if (i!=j) {
			if (dist(i,j) < R[i]+R[j]) cerr << "ERROR " << t << ' ' << i << ' ' << j << endl;
		}
		printf("Case #%d:", t);
		REP(i,N) printf(" %d %d", posx[i], posy[i]);
		printf("\n");
	}
	return 0;
}
