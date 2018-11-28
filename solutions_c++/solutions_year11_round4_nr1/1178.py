//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <stdio.h>
#include <string>
#include <memory.h>

using namespace std;

#define ldb long double
#define LL long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000


int x, n;
ldb s, r;
ldb t;
vector <pair <ldb, ldb> > rd;

ldb sp[2000000];


void Load()
{
	cin >> x >> s >> r >> t >> n;

	int a, b, c;
	for (int i = 0; i < x; i++)
		sp[i] = s;

	for (int i = 0; i < n; i++)
	{
		cin >> a >> b >> c;
		for (int j = a; j < b; j++)
			sp[j] += c;
	}
}

void Solve()
{
	rd.clear();
	sp[x] = -1; 	
	int b = 0;
	for (int i = 0; i <= x; i++)	
	{
		if (sp[i] == sp[b])
			continue;
		else
		{
			rd.push_back(make_pair (sp[b], i - b));
			b = i;
		}
	}
	sort (rd.begin(), rd.end());
	ldb ans = 0;
	for (int i = 0; i < (int)rd.size(); i++)
	{
		//cerr << rd[i].first << " " << rd[i].second << "\n"	;
		if (t < EPS)
		{
			ans += rd[i].second / rd[i].first;
		}
		else
		if (t > EPS)
		{
			ldb y = rd[i].second / (rd[i].first + r - s);
		//	cerr << t << "vs " << y << "\n";
			if (y < t + EPS)	
			{
			//	cerr << "here\n ";
				ans += y;
				t -= y; 	
			}
			else
			{
				ans += t;
				ans += (rd[i].second - ((rd[i].first + r - s) * t)) / rd[i].first;
				             
				t = 0;
			}
		}
	}
	cout << ans << "\n";
}
                
int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cout.setf(ios::showpoint | ios ::fixed);
	cout.precision (10);
	int t, T;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
	return 0;
	return 0;
}
