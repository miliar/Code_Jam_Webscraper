#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

typedef string answer_type;

const int N = 150;

int T[N][N];

answer_type solve()
{
	int n;
	cin >> n;
	char c;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cin >> c, T[i][j] = ((c == '1') ? 1 : (c == '0') ? -1 : 0);
	}
	double WP[N];
	double col[N];
	double won[N];
	for (int i = 0; i < n; i++)
	{
		col[i] = 0;
		won[i] = 0;
		for (int j = 0; j < n; j++)
		{
			if (i == j)
				continue;
			col[i] += T[i][j] != 0;
			won[i] += T[i][j] == 1;
		}
		WP[i] = won[i] / (double)col[i];
	}
	double OWP[N];
	for (int i = 0; i < n; i++)
	{
		double sum = 0;
		int tcol = 0;
		for (int j = 0; j < n; j++)
		{
			if (i == j)
				continue;
			if (T[i][j] == 0)
				continue;
			sum += (double)(won[j] - (T[j][i] == 1)) / (col[j] - 1);
			tcol++;
		}
		OWP[i] = sum / (tcol);
	}
	double OOWP[N];
	
	for (int i = 0; i < n; i++)
	{
		OOWP[i] = 0;
		int tcol = 0;
		for (int j = 0; j < n; j++)
		{
			if (i == j || T[i][j] == 0)
				continue;
			OOWP[i] += OWP[j];
			tcol++;
		}
		OOWP[i] /= tcol;
	}
	stringstream ss;
	ss << fixed << setprecision(10);
	string tmp;
	string ans = "";
	for (int i = 0; i < n; i++)
		ss << 0.25 * OOWP[i] + 0.5 * OWP[i] + 0.25 * WP[i] << "\n", ss >> tmp, ans += "\n" + tmp;
	return ans;
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
