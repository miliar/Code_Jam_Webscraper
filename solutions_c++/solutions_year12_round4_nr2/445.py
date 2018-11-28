#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

const int maxn = 1010;
const double eps = 1e-6;
int T, n, m, w, l;
struct C{int x, y, r, no;} r[maxn];
long long x, y;

LL sqr(LL x){return x * x;}
bool operator < (C a, C b){return a.r > b.r;}
bool cmp(C a, C b){return a.no < b.no;}

bool ok(int T){
	for (int i = 0; i < T; i++){
		LL d = sqr(r[i].x - x) + sqr(r[i].y - y);
		if (sqr(r[i].r + r[T].r) > d) return false;
	}
	return true;
}

int main(){
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	scanf("%d", &T);
	srand(time(0));
	for (int ca = 1; ca <= T; ca++){
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; i++) scanf("%d", &r[i].r), r[i].no = i;
		sort(r, r + n);

		for (int i = 0; i < n; i++){
			x = (LL)rand() * rand() * rand() % (w + 1), y = (LL)rand() * rand() * rand() % (l + 1);
			while (!ok(i)){
				x = (LL)rand() * rand() * rand() % (w + 1), y = (LL)rand() * rand() * rand() % (l + 1);
			}
			r[i].x = x, r[i].y = y;
		}

		sort(r, r + n, cmp);
		printf("Case #%d:", ca);
		for (int i = 0; i < n; i++) printf(" %d %d", r[i].x, r[i].y);
		printf("\n");
	}
}
