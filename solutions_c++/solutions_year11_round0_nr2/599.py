#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <vector>
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


char good[128][128];
bool bad[128][128];
char s[128];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	std::vector<char> ans;
	clr(good); clr(bad);
	int n;
	char buf[16];
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%s", buf);
		good[buf[0]][buf[1]] = good[buf[1]][buf[0]] = buf[2];
	}
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%s", buf);
		bad[buf[0]][buf[1]] = bad[buf[1]][buf[0]] = 1;
	}
	scanf("%d", &n);
	scanf("%s", s);
	for(int i = 0; i < n; i++)
	{
		ans.push_back(s[i]);
		int l = ans.size();
		if (l == 1)
			continue;
		if (good[ans[l-2]][ans[l-1]])
		{
			char c = good[ans[l-2]][ans[l-1]];
			ans.pop_back(); ans.pop_back();
			ans.push_back(c);
		} 
		else
		{
			for(int j = 0; j < l - 1; j++)
				if (bad[ans[j]][ans[l-1]])
				{
					ans.clear();		
					break;
				}
		}
	}
	printf("[");
	for(int i = 0; i < (int) ans.size(); i++)
	{
		printf("%s%c", i ? ", " : "", ans[i]);
	}
	printf("]\n");
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
