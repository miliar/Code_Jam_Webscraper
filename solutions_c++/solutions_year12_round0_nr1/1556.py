#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;
char x[128];
void init()
{
	for (int i = 0; i < 128; ++i)
		x[i] = i;
	x['a'] = 'y';
	x['b'] = 'h';
	x['c'] = 'e';
	x['d'] = 's';
	x['e'] = 'o';
	x['f'] = 'c';
	x['g'] = 'v';
	x['h'] = 'x';
	x['i'] = 'd';
	x['j'] = 'u';
	x['k'] = 'i';
	x['l'] = 'g';
	x['m'] = 'l';
	x['n'] = 'b';
	x['o'] = 'k';
	x['p'] = 'r';
	x['q'] = 'z';
	x['r'] = 't';
	x['s'] = 'n';
	x['t'] = 'w';
	x['u'] = 'j';
	x['v'] = 'p';
	x['w'] = 'f';
	x['x'] = 'm';
	x['y'] = 'a';
	x['z'] = 'q';
}
char buff[1000];
void solve(int n)
{
	gets(buff);
	for (int i = 0; buff[i]; ++i)
		buff[i] = x[buff[i]];
	printf("Case #%d: %s\n", n, buff);
}
int main()
{
#ifdef _DEBUG
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	init();
	scanf ("%d", &T);
	gets(buff);
	for (int i = 0; i < T; ++i)
	{
		solve(i + 1);
	}
	return 0;
}