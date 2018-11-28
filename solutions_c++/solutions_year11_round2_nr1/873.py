#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int testNum = 0;
int n;
int result;
char ch[1000][1000];

void read()
{
	cin >> n;
	int i, j;
	for (i = 1; i <= n; ++i)
		for (j = 1; j <= n; ++j)
			cin >> ch[i][j];
}

int count[1000];
double WP[1000];
double OWP[1000];
double OOWP[1000];
double RPI[1000];

void printOut()
{
	cout << "Case #" << testNum << ": \n";
	int i;
	for (i = 1; i <= n; ++i)
		cout << fixed << setprecision(12) << RPI[i] << "\n";
}

void solve()
{
	read();
	int i,j,k, c;
	
	///////// Counting WP //////////////////
	for (i = 1; i <= n; ++i)
	{
		c = 0; // total number of games
		WP[i] = 0.0;
		for (j = 1; j <= n; ++j)
		{
			if (ch[i][j] != '.')	
			{
				WP[i] += ch[i][j] - '0';
				++c;
			}
		}
		count[i] = c;
		if (c != 0)
			WP[i] /= c;
	}

	///////// Counting OWP //////////////////
	for (i = 1; i <= n; ++i)
	{
		c = 0; // total number of games
		OWP[i] = 0.0;
		for (j = 1; j <= n; ++j)
		{
			if (ch[i][j] != '.')	
			{
				if (count[j] != 1)
					OWP[i] += (WP[j] * count[j] - (ch[j][i] - '0')) / (count[j] - 1);
				else
					OWP[j] = 0.0;
				++c;
			}
		}
		if (c != 0)
			OWP[i] /= c;
	}

	///////// Counting OOWP //////////////////
	for (i = 1; i <= n; ++i)
	{
		c = 0; // total number of games
		OOWP[i] = 0.0;
		for (j = 1; j <= n; ++j)
		{
			if (ch[i][j] != '.')	
			{
				OOWP[i] += OWP[j];
				++c;
			}
		}
		if (c != 0)
			OOWP[i] /= c;
	}

	///////// Counting RPI //////////////////
	for (i = 1; i <= n; ++i)
	{
		RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
	}
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		++testNum;
		solve();
		--t;
	}
return 0;
}