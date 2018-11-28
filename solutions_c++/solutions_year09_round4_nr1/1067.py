#define IN "A-large.in"
#define dbg(x)  //cout << #x << "  -> " << (x) << "\t"
#define dbge(x) //cout << #x << "  -> " << (x) << "\n"
#include <cassert>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PI;

#define REP(i,n)		for (int i = 0; i < int(n); ++ i)
#define FOR(i,a,b)		for (int i = int(a); i < int(b); ++ i)
#define EACH(t,it,v)	for (t it = (v).begin(); it != (v).end(); ++ it)

int GI() { int t; scanf("%d",&t); return t; }
void solve();

int main()
{
	assert(freopen(IN, "r", stdin));
	assert(freopen(IN ".out.txt", "w", stdout));
	for (int kases = GI(), kase = 0; kase < kases; kase ++)
	{
		cout << "Case #" << kase+1 << ":";
		solve();
	}
	// while (1);
	return 0;
}

//////////////////////////////////////////////////////////////////////////
char A[50][50];
int Go[50], P[50];
int GoB[50], PB[50];
int n;

bool Good(int x) {
	for (int i = n - 1; i >= x; i --) {
		int cnt = 0;
		REP(j,n) cnt += Go[j] >= i;
		if (cnt > n - i) return false;
	}
	return true;
}

void solve()
{
	n = GI();
	REP(i,n) {
		scanf("%s", A[i]);
		Go[i] = -1; P[i] = i; 
		REP(j,n) if (A[i][j] == '1') Go[i] = j;
	}
	assert (Good(0));
	int ans = 0;
	REP(i,n) {
		bool ok = false;
		FOR(j, i, n) if (Go[j] <= i) {
			memcpy(GoB, Go, sizeof(Go));
			memcpy(PB, P, sizeof(P));
			int cur = 0;
			for(int k = j - 1; k >= i; k --) swap(Go[k], Go[k+1]), swap(P[k], P[k+1]), cur ++;
			if (Good(i + 1)) { ans += cur; ok = true; dbge(j); break; }
			memcpy(Go, GoB, sizeof(Go));
			memcpy(P, PB, sizeof(P));
		}
		assert (ok);
		//REP(i,n) printf("%s\n", A[P[i]]); printf("\n\n");
	}
	

	cout << " " << ans << endl;
}