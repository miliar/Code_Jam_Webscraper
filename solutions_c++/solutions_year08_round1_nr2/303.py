#include <cstdio>
#include <algorithm>
using namespace std;

typedef struct {
	int num;
	int ty[2002][2];
}custom;
custom a[2005];
int n, m, b[2002];
bool check (int x)
{
	int i, j;
	for (i = 0; i < n; i++){
		b[n-i] = x%2;
		x /= 2;
	}
	for (i = 0; i < m; i++){
        bool flag = false;
		for (j = 0; j < a[i].num; j++)
			if (b[a[i].ty[j][0]] == a[i].ty[j][1]) {flag = true;break ;}
		if (!flag) return false;
	}
	return true;
}
int cal (int x)
{
	int i, ans = 0;
	for (i = 0; i < n; i++){
		if (x % 2 == 0) ans++;
		x /= 2;
	}
}
int main ()
{
	int t, cnt, i, j;
	scanf ("%d", &t);
	for (cnt = 1; cnt <= t; cnt++){
		scanf ("%d%d", &n, &m);
		for (i = 0; i < m; i++){
			scanf ("%d", &a[i].num);
			for (j = 0; j < a[i].num; j++){
				int c, d;
				scanf ("%d%d", &c, &d);
				a[i].ty[j][0] = c;
				a[i].ty[j][1] = d;
			}
		}
		int tot = 1 << n, ans = -1, max = -1;
		for (i = 0; i < tot; i++){
			if (check (i)){
				int u = cal (i);
				if (u > max) max = u, ans = i;
			}
		}
		if (ans == -1) printf ("Case #%d: IMPOSSIBLE\n", cnt);
		else {
			for (i = 0; i < n; i++){
				b[n-i] = ans%2;
				ans /= 2;
			}
			printf ("Case #%d:", cnt);
			for (i = 1; i <= n; i++)
				printf (" %d", b[i]);
			puts ("");
		}
	}	
}
