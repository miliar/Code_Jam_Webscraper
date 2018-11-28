#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

void solve(void)
{
	int kol;
	cin >> kol;
	int i, j;
	double v[3] = {0, 0, 0}, t[3] = {0, 0, 0};
	double x[3], vx[3];
	for (i = 0; i < kol; i++)
	{
		for (j = 0; j < 3; j++)
			cin >> x[j];
		for (j = 0; j < 3; j++)
			cin >> vx[j];
		for (j = 0; j < 3; j++)
		{
			t[j] += x[j];
			v[j] += vx[j];
		}
	}
	for (j = 0; j < 3; j++)
	{
		t[j] /= kol;
		v[j] /= kol;
		//cerr << t[j] << " " << v[j] << "; ";
	}
	//cerr << endl;
	
	double xmin = 0, vmin = 0;
	for (j = 0; j < 3; j++)
		xmin -= t[j] * v[j];
	for (j = 0; j < 3; j++)
		vmin += v[j] * v[j];
	double res;
	if (abs(vmin) < 1e-7)
	{
		res = 0;
	}
	else
	{
		res = xmin / vmin;
		if (res < 0)
			res = 0;
	}
	double rast = 0;
	for (j = 0; j < 3; j++)
		rast += (t[j] + v[j] * res) * (t[j] + v[j] * res);
	rast = sqrt(rast);
	cout << rast << " " << res;
}

int main (void) 
{
	//freopen("input2.txt", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}