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

class my
{
public:
	ldb val;
	string s;
	int leef;
};

#define MAXN 100000

my t[MAXN];
char d[200];

void rec(int i)
{
	char c;
	ldb q;
	string s;
	my tmp;

	c = getchar();
	while (c == ' ')
		c = getchar();

	cin >> q;

	s = "";

	c = getchar();
	while (c == ' ')
		c = getchar();

	while (c != ' ' && c != '\n' && c != ')')
	{
		s += c;
		c = getchar();
	}

	while (c == ' ' && c != ')' && c != '\n')
		c = getchar();

	tmp.leef = 0;
	if (c == ')')
	{
		tmp.leef = 1;
		while (c != '\n')
			c = getchar();
	}
	tmp.val = q;
	tmp.s = s;	

	t[i * 2] = tmp;
	if (tmp.leef != 1)
		rec(i * 2);

	
	c = getchar();
	while (c == ' ')
		c = getchar();

	cin >> q;

	s = "";

	c = getchar();
	while (c == ' ')
		c = getchar();

	while (c != ' ' && c != '\n' && c != ')')
	{
		s += c;
		c = getchar();
	}

	while (c == ' ' && c != ')' && c != '\n')
		c = getchar();
	tmp.leef = 0;
	if (c == ')')
		tmp.leef = 1;
	tmp.val = q;
	tmp.s = s;	
	t[i * 2 + 1] = tmp;
	if (tmp.leef != 1)
		rec(i * 2 + 1);

	c = getchar();
	while (c != ')')
		c = getchar();
	while (c != '\n')
		c = getchar();
}



void Load()
{       	
	int dep;
	cin >> dep;
	char c;
	ldb q;
	string s;
	cin >> c;
	cin >> q;
	s = "";
	c = getchar();
	while (c == ' ')
		c = getchar();

	while (c != ' ' && c != ')' && c!= '\n')
	{
		s += c;
		c = getchar();
	}

	while (c == ' ' && c != ')' && c != '\n')
		c = getchar();

	my tmp;
	tmp.val = q;
	tmp.s = s;

	if (c == ')')
		tmp.leef = 1;
	else
	   tmp.leef = 0;
	t[1] = tmp;
	if (c != ')')
		rec(1);
}

set <string> st;
ldb p;


void solv_rec(int i)
{
	p *= t[i].val;
	if (t[i].leef == 1) return;
	if (st.find(t[i].s) == st.end())
		solv_rec(i * 2 + 1);
	else
		solv_rec(i * 2);
}

void solution()
{
	p = 1;
	solv_rec(1);

	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(10);

	cout << p << "\n";

} 

void Solve()
{
	int i, n, j, m;
	
	cin >> n;
	string s;
	for (i = 1; i <= n; i++)
	{
		cin >> s;
		cin >> m;
		st.clear();
		for (j = 0; j < m; j++)	
		{
			cin >> s;
			st.insert(s);
		}
		solution();
	}
}
                
int main()
{
	freopen(".in", "rt", stdin);
	freopen(".out", "wt", stdout);
	int i, t;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cout << "Case #"  << i << ":\n";
		Load();
		Solve();
	}

	return 0;
}
