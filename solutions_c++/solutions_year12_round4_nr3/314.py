#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef pair<int, int> PI;
typedef vector<int> VI;
typedef long long LL;
typedef double LF;
const int INF = 1000000000;
const int MAXN = 100010;

int res[2222], t[2222], n, lzd, tt;

int szukaj2 (int pos) {
	//printf("szukaj2 na %d\n", pos);
	LL ret = INF-1;
	for (int i=1; i<pos; i++)
		if (res[i] > 0 && res[t[i]] > 0) {
			LL diffx = t[i] - i;
			LL diffy = res[t[i]] - res[i];
			LL xprim = pos - i;
			ret = min(ret, xprim*diffy/diffx + res[i] - 1);
		}
	//printf("daje2 %lld\n", ret);
	return ret;
}

LL det (pair<LL, LL> a, pair<LL, LL> b, pair<LL, LL> c) {
	return a.ST * (b.ND - c.ND) + b.ST * (c.ND - a.ND) + c.ST * (a.ND - b.ND);
}

int szukaj1 (int pos) {
//	printf("szukaj1 na %d\n", pos);
	LL ret = min(szukaj2(pos), res[t[pos]])-1000000;
	for (int i=t[pos]+1; i<=n; i++)
		if (res[i] > 0) {
			while (det(MP(pos, ret), MP(t[pos], res[t[pos]]), MP(i, res[i])) >= 0)
				ret-=1000000;
		}
	for (int i=pos+1; i<t[pos]; i++)
		if (res[i] > 0) {
			while (det(MP(pos, ret), MP(i, res[i]), MP(t[pos], res[t[pos]])) <= 0)
				ret++;
		}
//	printf("daje1 %lld\n", ret);
	return ret;
}

int solve (int beg, int end) {
	if (beg == 1 && end == n) {
		for (int i=1; i<=n; i++)
			for (int j=i+1; j<=n; j++)
				if (t[i] > j && t[j] > t[i])
					return -1;
	}


//	printf("jestem %d %d\n", beg, end);
	if (beg == end) {
		return 0;
	}
	for (int i=beg; i<end; i++)
		if (t[i] > end)
			return -1;
	if (t[beg] == end) {
		// rosnij begiem
		if (solve(beg+1, end) == -1)
			return -1;
		
		res[beg] = szukaj1(beg);
		return 0;
	}
	// rosnij t[beg]iem
	int r2 = solve(t[beg]+1, end);
	if (r2 == -1) return -1;

	res[t[beg]] = szukaj1(t[beg]);
	
	int r1 = solve(beg, t[beg]);
	if (r1 == -1 || r2 == -1)
		return -1;
	return 0;
}

int main () {
	scanf("%d", &lzd);
	while (lzd--) {
		scanf("%d", &n);
		for (int i=1; i<n; i++)
			scanf("%d", &t[i]);
		
		for (int i=1; i<n;i ++)
			res[i] = 0;
		res[n] = INF;
		
		if (solve(1, n) == -1)
			printf("Case #%d: Impossible\n", ++tt);
		else {
			printf("Case #%d:", ++tt);
			for (int i=1; i<=n; i++)
				printf(" %d", res[i]);
			printf("\n");

			for (int i=1; i<=n; i++) {
				for (int j=i+1; j<=n; j++) {
					bool ok = true;
					for (int k=i+1; k < j; k++)
						if (det(MP(i, res[i]), MP(k, res[k]), MP(j, res[j])) <= 0)
							ok = false;
					for (int k=j+1; k<=n; k++)
						if (det(MP(i, res[i]), MP(j, res[j]), MP(k, res[k])) > 0)
							ok = false;
	//				if (ok)
	//					printf("%d ", j);
					if (ok)
						if (j != t[i])
							printf("                                    bug!\n");
				}
			}
	//		printf("\n");
	//		for (int i=1; i<=n; i++)
	//			printf("%d ", t[i]);
	//		printf("\n");
		}
	}
}

