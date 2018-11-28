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


char s[1000000];
int l;

class pattern
{
public:
	int use[20][256];
	void read()
	{
		gets(s);
		clr(use);
		int pos = 0;
		for(int i = 0; i < l; i++)
		{
			if (s[pos] == '(')
			{
				pos++;
				while(s[pos] != ')')
				{
					use[i][s[pos]] = 1;
					pos++;
				}
				pos++;
			} 
			else
			{
				use[i][s[pos]] = 1;
				pos++;
			}
		}
	}
	int accept(char * s)
	{
		for(int i = 0; i < l; i++)
			if (!use[i][s[i]])
				return 0;
		return 1;
	}
}p;

char strings[10000][20];

int str_cnt;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int ans = 0;
	p.read();
	for(int i = 0; i < str_cnt; i++)
	{
		ans += p.accept(strings[i]);
	}
	printf("%d\n", ans);

}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d%d", &l, &str_cnt);
	scanf("%d\n", &n);
	for(int i = 0; i < str_cnt; i++)
	{
		gets(strings[i]);
	}
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
