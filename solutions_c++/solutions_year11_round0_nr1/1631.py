#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextline { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define PII pair<int,int>
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;

int n;
char op[105];
int wh[105];
void Load()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> op[i] >> wh[i];
}

struct State
{
	int o, b, i;
	State() {};

	State(int o_, int b_, int i_): o(o_), b(b_), i(i_) {};
};

vector <State> q;
int d[105][105][105];

inline bool good(int x)
{
	return 1 <= x && x <= 100;
}

inline void relax(const State &s, int dst)
{
	if (good(s.o) && good(s.b) && dst < d[s.o][s.b][s.i])
	{
		d[s.o][s.b][s.i] = dst;
		q.pb(s);
	}
}

void Solve()
{
	memset(d, 0x7F, sizeof(d));
	int res = 0x7F7F7F7F;
	int hd = 0;
	q.resize(0);
	d[1][1][0] = 0;
	q.pb(State(1, 1, 0));
	int o, b, i;
	while (hd < (int)q.size())
	{
		o = q[hd].o;
		b = q[hd].b;
		i = q[hd].i;
		hd++;
		if (i == n)
		{
			res = d[o][b][i];
			break;
		}
		for (int d1 = -1; d1 <= 1; d1++)
			for (int d2 = -1; d2 <= 1; d2++)
				relax(State(o + d1, b + d2, i), d[o][b][i] + 1);
		if (op[i] == 'O' && o == wh[i])
		{
			relax(State(o, b + 1, i + 1), d[o][b][i] + 1);
			relax(State(o, b, i + 1), d[o][b][i] + 1);
			relax(State(o, b - 1, i + 1), d[o][b][i] + 1);
		}
		else if (op[i] == 'B' && b == wh[i])
		{
			relax(State(o + 1, b, i + 1), d[o][b][i] + 1);
			relax(State(o, b, i + 1), d[o][b][i] + 1);
			relax(State(o - 1, b, i + 1), d[o][b][i] + 1);
		}
	}
	cout << res;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
