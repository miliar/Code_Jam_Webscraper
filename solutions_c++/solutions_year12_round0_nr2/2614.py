#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
#define rep(i, j, k) for( i = j;i <= k;++i)
#define Maxn 105
struct node
{
	int fir, sec;
	inline void pair (int a, int b)
	{
		fir = a, sec = b;
	}
}Q[Maxn];
int T, n, S, P, ar[Maxn], tp, ans;
inline bool cmp (node a, node b)
{
	return ((a.sec < b.sec) ||  (a.sec == b.sec && a.fir < b.fir)); 
}
int main()
{
	int i, p, C = 0;
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		++C;
		printf("Case #%d: ",C);
		ans = tp = 0;
		scanf("%d%d%d", &n, &S, &P);
		rep (i, 1, n) scanf("%d", &ar[i]);
		rep (i, 1, n)
		{
			if (ar[i] > 1)
			{
				if (ar[i] % 3 == 0)
					Q[++tp].pair(ar[i] / 3 - 1, ar[i] / 3);
				else if (ar[i] % 3 == 1) Q[++tp].pair(ar[i] / 3 - 1, ar[i] / 3 + 1);
				else Q[++tp].pair(ar[i] / 3, ar[i] / 3 + 1);
				Q[tp].fir += 2;
			}
			else 
				Q[++tp].pair(0, ar[i]);
		}
		sort(Q + 1, Q + 1 + tp, cmp);
		for (p = 1, i = 0;;)
		{
			if (i == S || p > tp) break;
			if (Q[p].fir >= P) 
			{
				++ans;++i;
			}
			++p;
		}
		for(;;) 
		{
			if (p > tp) break;
			if (Q[p].sec >= P) 
				++ans;
			++p;
			
		}
		printf("%d\n",ans);
	}
	return 0;	
}
