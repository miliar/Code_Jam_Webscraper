#include <iostream>
#include <vector>
#include <string>
using namespace std;

double get_wp(const vector<string>& vs, int index)
{
	double w = 0, p = 0;

	for (int i = 0; i < vs[index].size(); i++)
	{
		if (vs[index][i] == '1')
			w++;
		if (vs[index][i] == '1' || vs[index][i] == '0')
			p++;
	}

	return w/p;
}

double get_owp(const vector<string>& vs, int index)
{
	double a = 0, c = 0;

	for (int i = 0; i < vs.size(); i++)
	{
		if (vs[i][index] == '1' || vs[i][index] == '0')
		{
			double w = 0, p = 0;

			for (int j = 0; j < vs[i].size(); j++)
			{
				if (index == j) continue;
				if (vs[i][j] == '1')
					w++;
				if (vs[i][j] == '1' || vs[i][j] == '0')
					p++;
			}

			a += w/p;
			c++;
		}
	}

	return a/c;
}

double get_oowp(const vector<string>& vs, int index)
{
	double a = 0, c = 0;

	for (int i = 0; i < vs.size(); i++)
	{
		if (vs[i][index] == '1' || vs[i][index] == '0')
		{
			double owp = get_owp(vs, i);

			a += owp;
			c++;
		}
	}

	return a/c;
}

int main()
{
	long long i, n, pd, pg, t;

	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n;

		vector<string> vs(n);
		vector<double> wp, owp, oowp;

		for (int x = 0; x < n; x++)
			cin >> vs[x];

		for (int x = 0; x < n; x++)
		{
			wp.push_back(get_wp(vs, x));
			owp.push_back(get_owp(vs, x));
			oowp.push_back(get_oowp(vs, x));
		}

		cout << "Case #" << i << ":\n";

		for (int x = 0; x < n; x++)
		{
			printf("%.10f\n", 0.25 * wp[x] + 0.50 * owp[x] + 0.25 * oowp[x]);
			//cout << 0.25 * wp[x] + 0.50 * owp[x] + 0.25 * oowp[x] << endl;
		}
	}

	return 0;
}
