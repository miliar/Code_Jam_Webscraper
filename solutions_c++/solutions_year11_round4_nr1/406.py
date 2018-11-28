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
#define INF 1000000000
#define EPS 1e-9
typedef long long ll;

int x, s, r, t, n;
struct Node
{
	int len, v;
};
bool operator<(Node A, Node B)
{
	return A.v < B.v;
}
Node nn[50000];
void _main()
{
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	int lr = 0, total = 0;
	for (int i = 0; i < n; i++)
	{
		int l, r, w;
		scanf("%d%d%d", &l, &r, &w);
		if (l > lr) total += l - lr;
		lr = r;
		nn[i].len = r - l;
		nn[i].v = w + s;
	}
	if (x > lr) total += (x - lr);
	nn[n].len = total;
	nn[n++].v = s;
	sort(nn, nn + n);
	r -= s;

	double tt = t, res = 0.0;
	for (int i = 0; i < n; i++)
	{
		double lll = nn[i].len;
		double vvv = nn[i].v;
		if (lll / (vvv + r) < tt + EPS)
		{
			tt -= lll / (vvv + r);
			res += lll / (vvv + r);
		}
		else
		{
			if (tt > EPS) 
			{
				res += tt;
				res += (lll - (vvv + r) * tt) / vvv;
				tt = 0.0;
			}
			else
			{
				res += (lll - (vvv + r) * tt) / vvv;
				tt = 0.0;
			}
		}
	}
	printf("%.6lf\n", res);
}
int main()
{
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		printf("Case #%d: ", cases);
		_main();
	}
}