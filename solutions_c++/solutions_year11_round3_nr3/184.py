#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define FORE(i,v) for(typeof((v).begin())i=(v).begin();i!=(v).end();i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define pf printf
typedef long long ll;
using namespace std;



void solve() {
	int n, l, h;
	scanf("%d%d%d", &n, &l, &h);
	int freq[120];
	FOR(i, n)
		scanf("%d", &freq[i]);
	for (int mf = l; mf <= h; mf++) {
		bool ok = true;
		FOR(i, n)
			if (mf % freq[i] != 0 && freq[i] % mf != 0) {
				ok = false;
				break;
			}
		if (ok) {
			pf("%d\n", mf);
			return;
		}
	}
	pf("NO\n");
}


int main() {
	//freopen(".in", "r", stdin); freopen(".out", "w", stdout);
	int n;
	scanf("%d", &n);
	FORO(i, n) {
		pf("Case #%d: ", i);
		solve();
	}
}


