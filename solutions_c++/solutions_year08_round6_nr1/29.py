#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);

const int Max = 1000;

int H[Max], W[Max], n;
int sH, SH, sW, SW;

void input() {
	scanf("%d", &n);
	sH = sW = 1000000;
	SH = SW = -sH;
	for(int i = 0;i < n;i ++) {
		int h, w;
		char buf[100];
		scanf("%d%d%s", &h, &w, buf);
		if(buf[0] == 'N') {
			scanf("%s", buf);
			H[i] = h; W[i] = w;
		}
		else {
			if(h < sH) sH = h;
			if(h > SH) SH = h;
			if(w < sW) sW = w;
			if(w > SW) SW = w;
			i --;
			n --;
		}
	}
}

void solve() {
	int m;
	scanf("%d", &m);
	while(m --) {
		int h, w;
		scanf("%d%d", &h, &w);
		if(h >= sH&&h <= SH&&w >= sW&&w <= SW) printf("BIRD\n");
		else {
			int nsH = sH, nsW = sW, nSH = SH, nSW = SW;
			if(h < nsH) nsH = h;
			if(h > nSH) nSH = h;
			if(w < nsW) nsW = w;
			if(w > nSW) nSW = w;
			int i = 0;
			for(i = 0;i < n;i ++) if(H[i] >= nsH&&H[i] <= nSH&&W[i] >= nsW&&W[i] <= nSW) break;
			if(i < n) printf("NOT BIRD\n");
			else printf("UNKNOWN\n");
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for(int ca = 1;ca <= cas;ca ++) {
		input();
		printf("Case #%d:\n", ca);
		solve();
	}
	return 0;
}
