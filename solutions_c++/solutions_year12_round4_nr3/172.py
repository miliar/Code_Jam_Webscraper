#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long LL;

const int MAX_N = 2000 + 10;
const LL INF = 1000000000;
int N;
int see[MAX_N];
LL h[MAX_N];

LL xmult(LL sx, LL sy, LL ux, LL uy, LL vx, LL vy)
{
	return (ux - sx) * (vy - sy) - (vx - sx) * (uy - sy);
}

LL get(int l, int r, int x)
{
	LL p = 0, q = INF + 1, mid;
	for( ; p + 1 < q; ) {
		mid = p + q >> 1;
		if (xmult(l, h[l], x, mid, r, h[r]) > 0 && xmult(x, mid, r, h[r], see[r], h[see[r]]) <= 0)
			p = mid;
		else 
			q = mid;
	}
	return p;
}

void calc(int l, int r)
{
	if (l + 1 == r) return;
	for(int i = l + 1; i < r; ++ i)
		if (see[i] == r) {
			h[i] = get(l, r, i);
			calc(l, i);
			calc(i, r);
			return;
		}
}

int permit(int i, int j)
{
	if (see[i] <= j || see[i] >= see[j])
		return false;
	return true;
}

void solve()
{
	scanf("%d", &N);
	for(int i = 1; i < N; ++ i)
		scanf("%d", &see[i]);
	int flag = true;
	for(int i = 1; i < N; ++ i)
		for(int j = i + 1; j < N; ++ j)
			if (permit(i, j)) 
				flag = false;
	if (! flag) {
		puts("Impossible");
		return;
	}
	
	h[0] = INF + 1; h[N] = INF; 
	see[N] = N + 1;h[N + 1] = INF;
	
	calc(0, N);
	for(int i = 1; i < N; ++ i)
		printf("%lld ", h[i]);
	printf("%lld\n", h[N]);
}

int main()
{
//	freopen("C.in","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		solve();
	}
	return 0;
}
