#include <iostream>
#include <ctime>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <iomanip>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long LL;
typedef long double ldb;

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;
const ldb PI = fabs(atan2(0.0, -1.0));
const int MAXN = 15;

int n, w, l;
vector <pii> students;

void load()
{
	scanf("%d%d%d", &n, &w, &l);
	students.resize(n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &students[i].fi);
		students[i].se = i;
	}
}

inline double randDouble()
{
	return (double)rand() / RAND_MAX;
}

double x[MAXN];
double y[MAXN];

void solve(int test)
{
	sort(students.begin(), students.end());
	reverse(students.begin(), students.end());

	x[students[0].se] = y[students[0].se] = 0.0;
	while (true)
	{
		for (int i = 1; i < n; i++)
		{
			int id = students[i].se;
			x[id] = randDouble() * w;
			y[id] = randDouble() * l;
		}

		bool ok = true;
		for (int i = 0; ok && i < n; i++)
		{
			int ii = students[i].se;
			for (int j = i + 1; j < n; j++)
			{
				int jj = students[j].se;
				double d = sqr(x[ii] - x[jj]) + sqr(y[ii] - y[jj]);
				if (d + EPS < sqr((LL)students[i].fi + (LL)students[j].fi))
				{
					ok = false;
					break;
				}
			}
		}
		if (ok) break;
	}

	printf("Case #%d:", test);
	for (int i = 0; i < n; i++)
		printf(" %.6lf %.6lf", x[i], y[i]);
	printf("\n");	
}

int main()
{
	srand(time(NULL));
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		load();
		solve(test);
	}	
	return 0;
}
