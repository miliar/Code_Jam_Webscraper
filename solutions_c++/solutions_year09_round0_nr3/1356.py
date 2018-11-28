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


string s; 
string w = "welcome to code jam";
//string w = "abc";

int dp[20][MAXN];
char d[MAXN];
int n, sum;


void Load()
{
	s = "";
	
	gets(d);
	int i;
	for (i = 0; i < (int)strlen(d); i++)
		s += d[i];
	n = (int)s.size();
}

void Solve()
{
	int i, j, t;
	for (i = 0; i < n; i++)
		if (w[0] == s[i]) dp[0][i] = 1;

	for (i = 0; i < 17; i++)
		for (j = 0; j <= n; j++)
			if (w[i] == s[j])
				for (t = j + 1; t < n; t++)
					if (w[i + 1] == s[t])
					{
						dp[i + 1][t] += dp[i][j];
						dp[i + 1][t] = dp[i + 1][t] % 10000;
					}

	sum = 0;

	for (i = 0; i < n; i++)
		if (w[17] == s[i])
		{
			j = 0;
			for (t = i + 1; t < n; t++)
				if (w[18] == s[t]) j++;
			sum += dp[17][i] * j;
			sum = sum % 10000;
		}			
}

void print(int a)
{
	if (a < 10)	
		cout << "000" << a;
	else
	if (a < 100) cout << "00" << a;
	else
	if (a < 1000) cout << "0" << a;
	else cout << a;
}              
int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);

	int t, i;
	scanf("%d\n", &t);
	for (i = 1; i <= t; i++)
	{
		memset(dp, 0, sizeof(dp));
		Load();
		Solve();
		cout << "Case #" << i << ": ";
	 	print(sum);
	 	cout << "\n";
	}
	return 0;
}
