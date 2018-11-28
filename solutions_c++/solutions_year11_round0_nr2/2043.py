#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 0

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;

char buf[1000];
char s[1000];
char str[10];

int len;
char combine[128][128];
int used[128];

vector <string> opposed;

void dbgBuf()
{
	buf[len] = 0;
	dbg("%s\n", buf);
}

void clearBuf()
{
	len = 0;
	clr(used);
}

void addC(char * s)
{
	if (combine[s[0]][s[1]] != 0)
	{
		dbg("%s\n", s);
		throw 42;
	}

	combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
}

void addD(char * s)
{
	opposed.push_back(string(s));
}

void addLetter(char ch)
{
	dbg("addLetter %c\n", ch);
	buf[len++] = ch;
	used[ch] ++;

	char comb;
	if (len >= 2 && (comb = combine[buf[len - 1]][buf[len - 2]]) != 0)
	{
		for (int i = 0; i < 2; ++i)
		{
			--len;
			used[buf[len]]--;
		}
		buf[len++] = comb;
		used[comb]++;
//		addLetter(comb);
		return;
	}

	for (int i = 0; i < int(opposed.size()); ++i)
	{
		char ch1 = opposed[i][0];
		char ch2 = opposed[i][1];
		if ((ch1 == ch2 && used[ch1] >= 2) || (ch1 != ch2 && used[ch1] >= 1 && used[ch2] >= 1))
		{
			clearBuf();
			return ;
		}
	}
}

void printRes(int t)
{
	printf("Case #%d: [", t);
	if (len > 0)
	{
		printf("%c", buf[0]);
		for (int i = 1; i < len; ++i)
			printf(", %c", buf[i]);
	}
	printf("]\n");
}

int main()
{
#ifdef DBG1
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 0; ii < tt; ++ii)
	{
		opposed.clear();
		fill(combine, 0);
		int c;
		scanf("%d", &c);
		for (int i = 0; i < c; ++i)
		{
			scanf("%s", str);
			addC(str);
		}
		int d;
		scanf("%d", &d);
		for (int i = 0; i < d; ++i)
		{
			scanf("%s", str);
			addD(str);
		}

		int n;
		scanf("%d", &n);
		scanf("%s", s);
		clearBuf();
		for (int i = 0; i < n; ++i)
		{
			addLetter(s[i]);
			dbgBuf();
		}
		buf[len] = 0;
		printRes(ii + 1);
	}

	return 0;
}
