#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

int ar[1000];
char s[1000];
bool used[1000];


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%s", &s);
		ar[i] = 0;
		for(int j = 0; j < n; j++)
		{
			if (s[j] == '1')
				ar[i] = j + 1;
		}
	}
	clr(used);
	int ans = 0;
	for(int i = 1; i <= n; i++)
	{
		for(int j = 0;;j++)
		{
			if (used[j])
				continue;
			if (ar[j] <= i)
			{
				used[j] = true;
				break;
			}
			ans++;
		}
	}
	printf("%d\n", ans);


}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
