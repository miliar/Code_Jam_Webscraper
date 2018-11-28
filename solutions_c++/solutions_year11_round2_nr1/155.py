#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
using namespace std;

const int N_MAX = 110;
char a[N_MAX][N_MAX];
int wins[N_MAX];
int games[N_MAX];
LD owp[N_MAX];

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	cin >> tst;
	cout << fixed << setprecision(8);

	for (int t = 1; t <= tst; ++t)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		for (int i = 0; i < n; ++i)
		{
			wins[i] = games[i] = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] != '.') games[i]++;
				if (a[i][j] == '1') wins[i]++;
			}
		}

		for (int i = 0; i < n; ++i)
		{
			owp[i] = 0.0L;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '.') continue;
				int cwc = wins[j];
				if (a[i][j] == '0') --cwc;
				owp[i] += (LD)cwc / (games[j] - 1);
			}
			owp[i] /= games[i];
		}

		cout << "Case #" << t << ':' << '\n';
		for (int i = 0; i < n; ++i)
		{
			LD cur = 0.25L * wins[i] / games[i] + 0.50L * owp[i];
			LD add = 0.0L;
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.')
					add += owp[j];
			cur += 0.25L * (add / games[i]);
			cout << cur << '\n';
		}
	}

	return 0;
}
