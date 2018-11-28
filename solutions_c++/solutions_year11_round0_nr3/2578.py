#include <cstdio>
#include <algorithm>

using namespace std;

int T, N, v[1005], S;
int a[1005], b[1005], sp[1005];

int addS(int x, int y)
{
	int z = 0;
	int i;
	for (i = 0; i <= 20; i++)
	{
		int t = 1 << i;
		if (t > x && t > y) break;
		if (t & x && t & y) continue;
		z += (t & x);
		z += (t & y);
	}
	return z;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int i, k;
	scanf("%d", &T);
	
	//printf("%d %d %d", addS(4, 5), addS(7, 9), addS(50, 10));
	
	for (k = 1; k <= T; k++)
	{
		S = 0;
		scanf("%d", &N);
		for (i = 1; i <= N; i++) scanf("%d", &v[i]);
		
		sort(v + 1, v + N + 1);
		
		a[0] = sp[0] = 0; b[N + 1] = 0;
		for (i = 1; i <= N; i++)
		{
			sp[i] = sp[i - 1] + v[i];
			S += v[i];
			a[i] = addS(a[i - 1], v[i]);
			b[N - i + 1] = addS(b[N - i + 2], v[N - i + 1]);
		}
		int ok = 0, rez = 0;
		for (i = 1; i < N; i++)
			if (a[i] == b[i + 1])
			{
				ok = 1;
				rez = S - sp[i];
				break;
			}
		printf("Case #%d: ", k);
		if (ok) printf("%d\n", rez);
		else printf("NO\n");		
	}
	
	
	return 0;
}
