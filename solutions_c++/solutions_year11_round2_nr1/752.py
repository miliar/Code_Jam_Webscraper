#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

string Table[100];
double wp[100];
double owp[100];
double oowp[100];
int n;

double getWP(int idx, int ignore = -1)
{
	double res = 0.0;
	double Count = 0.0;
	for (int i=0;i<n;i++)
	{
		if (i==ignore)
			continue;

		if (Table[idx][i]!='.')
		{
			Count++;
			if (Table[idx][i]=='1')
				res++;
		}
	}
	return res/Count;
}
double getOWP(int idx)
{
	double res = 0.0, Count = 0.0;
	for (int i=0;i<n;i++)
		if (Table[idx][i]!='.')
		{
			Count++;
			res+=getWP(i, idx);
		}
	return res/Count;
}

double getOOWP(int idx)
{
	double res = 0.0, Count = 0.0;
	for (int i=0;i<n;i++)
		if (Table[idx][i]!='.')
		{
			Count++;
			res+=owp[i];
		}
	return res/Count;
}

int main()
{
	int T, test;
	cin >> T;
	for (test=1;test<=T;test++)
	{
		cin >> n;

		for (int i=0;i<n;i++)
			cin >> Table[i];

		

		for (int i=0;i<n;i++)
			wp[i] = getWP(i);

		for (int i=0;i<n;i++)
			owp[i] = getOWP(i);

		for (int i=0;i<n;i++)
			oowp[i] = getOOWP(i);

		cout << "Case #" << test <<":" << endl;
		for (int i=0;i<n;i++)
		{
			double res = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%1.15lf\n", res);
		}


	}
}