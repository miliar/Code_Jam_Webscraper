// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<(x)<<endl
#define SIZE(X) int(X.size())

#define MAX 1234

typedef struct {
	ll x, y, r, i;
} circle;

bool cmp1(const circle &a, const circle &b) {
	return a.r < b.r;
}

bool cmp2(const circle &a, const circle &b) {
	return a.i < b.i;
}

int N;
circle C[MAX];
ll W, H;

bool overlap(circle &a, circle &b) {
	ll dx = a.x-b.x;
	ll dy = a.y-b.y;
	ll dr = a.r + b.r;
	return dx * dx + dy * dy < dr * dr;
}

bool go(int i, int tries = 20) {
	if (i == N) return true;
	FOR(k,tries) {
		C[i].x = rand() % (W+1);
		C[i].y = rand() % (H+1);
		FOR(j,i) if (overlap(C[i],C[j])) goto next;
		if (go(i+1)) return true;
		next:;
	}
	return false;
}


int main() {
	int T; scanf("%d", &T);
    FORTO(t,1,T) {
		scanf("%d %lld %lld", &N, &W, &H);
		FOR(i,N) {
			scanf("%lld", &C[i].r);
			C[i].i = i;
		}
		sort(C,C+N,cmp1);
		go(0);
		sort(C,C+N,cmp2);
		printf("Case #%d:", t); FOR(i,N) printf("% lld.0 %lld.0", C[i].x, C[i].y); printf("\n");
	}
	return 0;
}
