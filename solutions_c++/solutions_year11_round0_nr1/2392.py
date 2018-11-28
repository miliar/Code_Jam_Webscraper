#include <cstdio>
#include <algorithm>

const int maxn = 130;
int n;
char cmd[maxn][3];
int num[maxn];

void work(const int _)
{
    int ans = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
	scanf("%s%d", cmd[i], &num[i]);
    int o = 1, b = 1, no = 0, nb = 0;
    while (no < n && cmd[no][0] == 'B')
	++no;
    while (nb < n && cmd[nb][0] == 'O')
	++nb;
    while (nb < n || no < n)
    {
#if DB & 1
	fprintf(stderr, "ans %d, b %d, o %d, nb %d, no %d\n", ans, b, o, nb, no);
#endif
	if (nb < no)
	{
	    int t;
	    ans += t = abs(num[nb] - b) + 1;
	    b = num[nb];
	    if (abs(num[no] - o) <= t)
		o = num[no];
	    else if (num[no] < o)
		o -= t;
	    else
		o += t;
	    while (++nb < n && cmd[nb][0] == 'O')
		;
	}
	else
	{
	    int t;
	    ans += t = abs(num[no] - o) + 1;
	    o = num[no];
	    if (abs(num[nb] - b) <= t)
		b = num[nb];
	    else if (num[nb] < b)
		b -= t;
	    else
		b += t;
	    while (++no < n && cmd[no][0] == 'B')
		;
	}
    }
    printf("Case #%d: %d\n", _, ans);
}

int main()
{
    int _;
    scanf("%d", &_);
    for (int i = 1; i <= _; ++i)
	work(i);
}
