#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;
	double answer;

    lint x[1024], y[1024], z[1024];
	lint p[1024];
	int n;

	void readdata()
	{
		fin >> n;
		for (int i = 0; i < n; i++)
			fin >> x[i] >> y[i] >> z[i] >> p[i];
	}

	void outputdata()
	{
		fout.setf(ios::fixed | ios::showpoint);
		fout.precision(6);
		fout << "Case #" << (test + 1) << ": " << answer << endl;
	}

	lint iabs(lint v) {
		return v < 0 ? -v : v;
	}

	bool ok(double need) {
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++) {
				double d1 = need * p[i];
				double d2 = need * p[j];
				lint dist = iabs(x[i] - x[j]) +
							iabs(y[i] - y[j]) +
							iabs(z[i] - z[j]);
				if (dist > d1 + d2)
					return false;
			}
		return true;
	}

	void run()
	{
		double l = 0;
		double r = INF;
		double c;
		while (abs(l - r) > 1e-10) {
			c = (l + r) / 2.;
			if (ok(c))
				r = c;
			else
				l = c;
		}
		answer = (l + r) / 2.;
	}

int main()
{
	fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		run();
		outputdata();
	}
	return 0;
}
