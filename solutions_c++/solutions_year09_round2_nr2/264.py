#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
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


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	char old[100], _new[100];
	int count[100];
	clr(old);
	scanf("%s", &old);
	int l = strlen(old);
	clr(count);
	for(int i = 0; i < l; i++)
	{
		count[old[i]-'0']++;
	}
	if (!std::next_permutation(old, old+l))
	{
		l = 0;
		for(int i = 1; i < 10; i++)
		{
			if (count[i])
			{
				old[l++] = i + '0';
				count[i] --;
				break;
			}			
		}
		old[l++] = '0';
		for(int i = 0; i < 10; i++)
		{
			while (count[i]--)
			{
				old[l++] = i + '0';
			}
		}
	}
	printf("%s\n", old);
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
