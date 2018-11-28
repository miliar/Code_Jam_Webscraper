#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int> > a;

void solve(int test)
{
	
	vector<double> wp, rpi, owp, oowp;
	vector<int> wn, sm;
	wn.resize(n);
	sm.resize(n);
	wp.resize(n);
	rpi.resize(n);
	owp.resize(n);
	oowp.resize(n);
	
	for (int i = 0; i < n; ++i)
	{
		int sum = 0, win = 0;
		for (int j = 0; j < n; ++j)
		{
//			cerr << a[i][j] << " ";
			if (a[i][j] != -1)
				++sum, win += a[i][j];
		}
//		cerr << endl;
		wn[i] = win;
		sm[i] = sum;
		wp[i] = 1.0 * win / sum;
//		cerr << wp[i] << endl;
		rpi[i] += 0.25 * wp[i];
	}


	for (int i = 0; i < n; ++i)
	{
		double sum = 0;
		int col = 0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != -1)
			{
//				sum += wp[j], ++col;
				++col;
				if (a[i][j] == 1)
					sum += 1.0 * (wn[j]) / (sm[j] - 1);
				else
					sum += 1.0 * (wn[j] - 1) / (sm[j] - 1);
//				cerr << "!!!" << j << " " << wp[j] << endl;
			}
		owp[i] = sum / col;
		rpi[i] += 0.5 * owp[i];
	}

	for (int i = 0; i < n; ++i)
	{
		double sum = 0;
		int col = 0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != -1)
				sum += owp[j], ++col;
		oowp[i] = sum / col;
		rpi[i] += 0.25 * oowp[i];
	}



//	sort(rpi.rbegin(), rpi.rend());
	
	cout << "Case #" << test + 1 << ":" << endl;

	for (int i = 0; i < n; ++i)
		printf("%.9f\n", rpi[i]);
//	cerr << "___________________________";
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int T;
	cin >> T;
	
	for (int colT = 0; colT < T; ++colT)
	{
		a.clear();
		cin >> n;
		a.resize(n);
		for (int i = 0; i < n; ++i)
		{
			a[i].resize(n);
			for (int j = 0; j < n; ++j)
			{
				char c;
				cin >> c;
				if (c == '.')
					a[i][j] = -1;
				else
					a[i][j] = c - '0';
			}
		}
		
		solve(colT);
	}
	
	return 0;
}
