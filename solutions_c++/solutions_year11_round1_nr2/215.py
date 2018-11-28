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

#define DBG2 1

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

const int N = 20000;

int n, m;
char d[N][20];
char l[30];

int score[N];

void solve(vector <int> & idx, char * l, int curScore)
{
	if (idx.empty())
		return ;

	if ((int)idx.size() == 1)
	{
		for (int i = 0; i < int(idx.size()); ++i)
			score[idx[i]] = curScore;
		return ;
	}

	map < int, vector <int> > classes;

	//vector <int> idx1, idx2;
	for (int i = 0; i < int(idx.size()); ++i)
	{
		int num = idx[i];
		int mask = 0;
		for (int j = 0; d[num][j]; ++j)
			if (d[num][j] == *l)
				mask ^= (1 << j);
		classes[mask].push_back(num);
	}

	if (classes[0].size() == idx.size())
	{
		solve(idx, l + 1, curScore);
	}
	else
	{
//		solve(classes[0], l + 1, curScore + 1);
		for (map<int, vector<int> >::iterator it = classes.begin(); it != classes.end(); ++it)
		{
			solve(it -> second, l + 1, curScore + (it -> first == 0));
		}
	}

/*	dbg("%c:", *l);
	for (int i = 0; i < int(idx1.size()); ++i)
		dbg(" %s", d[idx1[i]]);
	dbg(" |");
	for (int i = 0; i < int(idx2.size()); ++i)
		dbg(" %s", d[idx2[i]]);
	dbg("\n");*/

}

void solve()
{
//	dbg("\n");
	for (int i = 0; i < n; ++i)
		score[i] = -1;


	for (int len = 1; len <= 10; ++len)
	{
//		dbg("%d\n", len);
		vector <int> idx;
		for (int i = 0; i < n; ++i)
			if ((int)strlen(d[i]) == len)
				idx.push_back(i);

		solve(idx, l, 0);
	}

//	for (int i = 0; i < n; ++i)
//		dbg("%s %d\n", d[i], score[i]);

	int best = 0;
	for (int i = 1; i < n; ++i)
		if (score[i] > score[best])
			best = i;
	printf(" %s", d[best]);
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
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", d[i]);
		printf("Case #%d:", ii + 1);
		for (int i = 0; i < m; ++i)
		{
			scanf("%s", l);
			solve();

				fflush(stdout);
		}
		printf("\n");

	}

	return 0;
}
