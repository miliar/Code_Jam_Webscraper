#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <deque>
#include <string>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#define eps 1e-11
using namespace std;
int n, t, s, x, m; vector<int> c;
int main()
{
	scanf("%d", &t);
	for (int T=0; T<t; T++)
	{
		scanf("%d", &n); c.resize(n); s=0; x=0; m=1<<30;
		for (int i=0; i<n; i++) scanf("%d", &c[i]), s+=c[i], x^=c[i], m=min(m, c[i]);
		if (x) printf("Case #%d: NO\n", T+1); else printf("Case #%d: %d\n", T+1, s-m);
	}
	return 0;
}
