#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

int Solution()
{
	int n;
	cin >> n;
	char mas[100][100];
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j)
			cin >> mas[i][j];
	//	RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	double wp[100];
	int wins[100], games[100];
	fill(wins, wins + 100, 0);
	fill(games, games + 100, 0);
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			if(mas[i][j] != '.')
				++games[i];
			if(mas[i][j] == '1')
				++wins[i];
		}
		wp[i] = (double)wins[i] / games[i];
	}

	double owp[100];
	for(int i = 0; i < n; ++i)
	{
		double sum = 0.;
		int cnt = 0;
		for(int j = 0; j < n; ++j)
			if(mas[i][j] != '.')
			{
				if(mas[i][j] == '0')
					sum += (double)(wins[j] - 1) / (games[j] - 1);
				else
					sum += (double)(wins[j]) / (games[j] - 1);
				++cnt;
			}
		owp[i] = sum / cnt;
	}

	double oowp[100];
	for(int i = 0; i < n; ++i)
	{
    	double sum = 0.;
		int cnt = 0;
		for(int j = 0; j < n; ++j)
			if(mas[i][j] != '.')
			{
				sum += owp[j];
				++cnt;
			}
		oowp[i] = sum / cnt;
	}

	for(int i = 0; i < n; ++i)
		printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ':' << endl;
		Solution();
	}
#ifdef debug
	system("@pause");
#endif
	return 0;
}
