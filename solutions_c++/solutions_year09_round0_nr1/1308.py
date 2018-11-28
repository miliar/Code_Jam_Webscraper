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
#include <string>

using namespace std;

#define ldb long double
#define lng long long
#define nextline {int c; while ((int c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-12

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int l, d, n;
bool a[20][300];

vector <string> r;
string s;


void Load()
{
	cin >> l >> d >> n;
	for (int i = 1; i <= d; i++)
	{
		cin >> s;
		r.push_back(s);
	}
}

void Solve()
{
	int i, j, c, k, ans;
	for (i = 1; i <= n; i++)
	{
		memset(a, 0, sizeof(a));
		cin >> s;
		k = 0;	
		for (j = 1; j <= l; j++)
		{
			if (s[k] == '(')
			{
				k++;
				while (s[k] != ')')
				{
					a[j][s[k]] = 1;
					k++;
				}
			}
			else
			{
				a[j][s[k]] = 1;
			}
			k++;
		}
		ans = 0;
		for (j = 0; j < d; j++)
		{
			c = 0;
			for (k = 1; k <= l; k++)
				if (a[k][r[j][k - 1]] == 1)
					c++;
			if (c == l) ans++;
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}
}
                
int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	Load();
	Solve();
	return 0;
}
