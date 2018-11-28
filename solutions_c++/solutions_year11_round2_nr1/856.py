#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

const int MaxN = 105;

int N;
string m[MaxN], m1[MaxN];
double WP[MaxN], OWP[MaxN], OOWP[MaxN];

void getWP(double WP[MaxN])
{
	for (int i = 0; i < N; ++i)
	{
		int win = 0;
		int all = 0;
		for (int j = 0; j < N; ++j)
		{
			if (m[i][j] == '1') win++;
			if (m[i][j] != '.') all++;
		}
		WP[i] = 1.0 * win / all;
	}
}

int main()
{
	int Ncase;
	freopen("a_large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> N;
		for (int i = 0; i < N; ++i)
		{
			cin >> m[i];
			m1[i] = m[i];
		}

		getWP(WP);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
				m[j][i] = '.';

			double WP1[MaxN];
			getWP(WP1);

			double sum = 0;
			int all = 0;
			for (int j = 0; j < N; ++j)
				if (m[i][j] != '.') 
				{
					sum += WP1[j];
					all++;
				}
			OWP[i] = 1.0 * sum / all;

			for (int j = 0; j < N; ++j)
				m[j][i] = m1[j][i];
		}

		for (int i = 0; i < N; ++i)
		{
			double sum = 0;
			int all = 0;
			for (int j = 0; j < N; ++j)
				if (m[i][j] != '.') 
				{
					sum += OWP[j];
					all++;
				}
			OOWP[i] = sum / all;
		}

/*
		for (int i = 0; i < N; ++i)
			cout << WP[i] << " ";
		cout << endl;
		for (int i = 0; i < N; ++i)
			cout << OWP[i] << " ";
		cout << endl;
		for (int i = 0; i < N; ++i)
			cout << OOWP[i] << " ";
		cout << endl;
		*/

		cout << "Case #" << run+1 << ":" << endl;
		for (int i = 0; i < N; ++i)
			cout << 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] << endl;
	}
}
