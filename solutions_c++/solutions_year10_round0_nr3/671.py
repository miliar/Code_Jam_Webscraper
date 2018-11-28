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
#define lng long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int a[1100], b[1100];
long long ss[1100];
int n;
int k;
int r;

void Load()
{
	cin >> r >> k >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
}

void Solve()
{
	long long sum = 0, s1;
	int i, j;
	for (i = 0; i < n; i++)
	{
		s1 = 0;
		j = i;
		while (s1 + a[j] <= k)	
		{
			s1 += a[j];
			j += 1;
			j = j % n;
			if (j == i)
				break;
		}
		b[i] = j;
		ss[i] = s1;
	}
	j = 0;
	for (int t = 1; t <= r; t++)
	{
		sum += ss[j];
		j = b[j]; 
	}
	cout << sum << "\n";
}
                
int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int T,t;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
}
