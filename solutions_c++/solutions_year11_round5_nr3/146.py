#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>
using namespace std;

#define mp make_pair

template <typename T>
string str(T x)
{
	stringstream s;
	s << fixed << setprecision(20);
	s << x;
	return s.str();
}

typedef string answer_type;

void precalc()
{
	cerr << "Precalc finished" << endl;
}



answer_type solve()
{
	int n, m;
	cin >> n >> m;
	const int N = 10;
	char F[N][N];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> F[i][j];
		
	bool g[N][N];
	int cnt = 0;
	for (int msk = 0; msk < (1 << (n * m)); msk++)
	{
		memset(g, 0, sizeof(g));

		for (int i = 0; i < (n * m); i++)
		{
			int f = ((msk >> i) & 1) * 2 - 1;
			int x = i % m;
			int y = (i - x) / m;
			int xx = x + (F[y][x] == '-') * f + (F[y][x] == '/') * f + (F[y][x] == '\\') * f;
			int yy = y + (F[y][x] == '|') * f - (F[y][x] == '/') * f + (F[y][x] == '\\') * f;
			xx = (xx + m) % m;
			yy = (yy + n) % n;
			if (g[yy][xx])
				goto nmsk;
			else
				g[yy][xx] = 1;
		}
		cnt++;
		nmsk:;
	}
	return str((cnt % 1000003));
}

int main()
{
	precalc();
	int T;
	cin >> T;
	cout << fixed << setprecision(10);
	cerr << fixed << setprecision(10);
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
