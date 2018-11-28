#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

char a[110][110];
double ans[110]; 
double wp[110]; 
int winWP[110];
int loseWP[110];  
double owp[110]; 
double oowp[110]; 
int n;

int WWin,WLose;

double WP(int i)
{
	int win = 0, lose = 0,j;
	for (j = 0 ; j < n; ++j)
		if (a[i][j] == '1')
			win++;
		else
			if (a[i][j] == '0')
				lose++;
	WWin = win;
	WLose = lose;
	return (double)win/(double)(win + lose);
}

void solve()
{
	int i,j;
	for (i = 0 ; i < n; ++i)
	{
		wp[i] = WP(i);
		winWP[i] = WWin;
		loseWP[i] = WLose;
	}

	for (i = 0 ; i < n; ++i)
	{
		double st = 0.0;
		int qanak = 0;
		for (j = 0 ; j < n; ++j)
			if (a[i][j] != '.')
			{
				if (a[j][i] == '1')
					st += (double)(winWP[j] - 1)/(double)(winWP[j] + loseWP[j] - 1);
				else
					st += (double)(winWP[j])/(double)(winWP[j] + loseWP[j] - 1);
				qanak++;
			}
		owp[i] = st/(double)qanak;
	}

	for (i = 0 ; i < n; ++i)
	{
		double st = 0.0;
		int qanak = 0;
		for (j = 0 ; j < n; ++j)
			if (a[i][j] != '.')
			{
				st += owp[j];
				qanak++;
			}
		oowp[i] = st/(double)qanak;
	}

	for (i = 0 ; i < n; ++i)
		ans[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
}

int main()
{
	int test,t,i;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		in >> n;
		for (i = 0 ; i < n; ++i)
			in >> a[i];
		solve();
		out << "Case #" << t << ":" << endl;
		for (i = 0; i < n; ++i)
		{
			out << setiosflags(ios::fixed | ios::showpoint);
			out << setprecision(8) << ans[i] << endl;
		}
	}
	return 0;
}