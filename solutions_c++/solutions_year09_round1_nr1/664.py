#include <cstdio>
#include <algorithm>
using namespace std;
#include <cstring>
#define MAXN 100
#define MAX 100000000
bool cmp(int a, int b) {return a > b; }
int tail, ok, num, sum, test, t, m, a[MAXN], f[MAX];
char st[MAXN];
int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &test); gets(st);
	for (int tt = 1; tt <= test; tt++)
	{
		gets(st);
		st[strlen(st) + 1] = 0; st[strlen(st)] = ' ';
		tail = 0; num = 0;
		for (int i = 0; st[i];)
			if (!(st[i] >= '0' && st[i] <= '9'))
			{
				while (st[i] && !(st[i] >= '0' && st[i] <= '9')) i++;
				a[tail++] = num;
				num = 0;
			}
			else num = num * 10 + st[i] - 48, i++;
		sort(a, a + tail, cmp);
		ok = 0;
		for (int i = 2; !ok; i++)
		{
			ok = 1; memset(f, -1, sizeof(f[0]) * m);
			if (m < i) m = i;
			for (int j = 0; j < tail; j++)
			{
				t = i; f[t] = j;
				while (t != 1)
				{
					sum = 0;
					while (t)
					{
						sum += (t % a[j]) * (t % a[j]);
						t /= a[j];
					}
					if (f[sum] == j){ok = 0; break;	}
					t = sum; f[t] = j;
					if (m < t) m = t;
				}
				if (!ok) break;
			}
			if (ok) printf("Case #%d: %d\n", tt, i);
		}
	}
	fclose(stdin); fclose(stdout);
	return 0;
}