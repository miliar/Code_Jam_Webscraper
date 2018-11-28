#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T; int testid;

int N;
string play[200];
int win[200];
int total[200];
double WP[200];
double OWP[200];
double OOWP[200];
void init()
{
	scanf("%d", &N);
	string line;
	memset(win, 0, sizeof(win));
	memset(total, 0, sizeof(total));

	getline(cin, line);
	for (int i = 0; i < N; ++i)
	{
		getline(cin, play[i]);
		for (int j = 0; j < N; ++j)
			if (play[i][j] != '.')
			{
				total[i]++;
				if (play[i][j] == '1') win[i]++;
			}
	}

	for (int i = 0; i < N; ++i)
	{
		WP[i] = (double)win[i] / (double) total[i];
		//cout << WP[i] << endl;
	}

	for (int i = 0; i < N; ++i)
	{
		OWP[i] = 0;
		for (int j = 0; j < N; ++j)
			if (play[i][j] != '.') 
			{
				double temp = 0;
				if (play[j][i] == '1') temp = (win[j] - 1) / (double) (total[j] - 1);
				else temp = (win[j]) / (double)(total[j] - 1);
				OWP[i] += temp;
			}
		OWP[i] /= total[i];
	}

	for (int i = 0; i < N; ++i)
	{
		OOWP[i] = 0;
		for (int j = 0; j < N; ++j)
			if (play[i][j] != '.')
				OOWP[i] += OWP[j];
		OOWP[i] /= total[i];
	}

	printf("Case #%d:\n", testid);
	for (int i = 0; i < N; ++i)
	{
		double ans = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		printf("%.10f\n", ans);
	}
}

void york()
{
}

int main()
{
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}