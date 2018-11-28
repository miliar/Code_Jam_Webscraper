#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

void makepoints(vector <long long> & x, vector <long long> & y, long long m, long long a, long long b, long long c, long long d, long long n)
{
	int i;

	for(i = 1; i < n; ++i)
	{
		x[i] = (a * x[i - 1] + b) % m; 
		y[i] = (c * y[i - 1] + d) % m;
	}
}

int main()
{
	int T, N;
	ifstream fin("a.in");
	ofstream fout("a.out");

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		fout << "Case #" << T << ": ";
		long long n, a, b, c, d, x0, y0, m;
		fin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		vector <long long> x(n);
		vector <long long> y(n);
		x[0] = x0;
		y[0] = y0;
		makepoints(x, y, m, a, b, c, d, n);

		//cout << x[3] << " " << y[3] << endl;

		int i, j, k, res = 0;

		for(i = 0; i < n; ++i)
		{
			for(j = i + 1; j < n; ++j)
			{
				for(k = j + 1; k < n; ++k)
				{
					if ((x[i] + x[j] + x[k]) % 3 == 0 && (y[i] + y[j] + y[k]) % 3 == 0) ++res;
				}
			}
		}

		fout << res << endl;
	}
	return 0;
}

