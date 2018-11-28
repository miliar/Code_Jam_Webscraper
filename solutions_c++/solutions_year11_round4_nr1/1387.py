#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

const int maxN = 1010;
const double eps = 1e-10;

fstream fin, fout;
double a[maxN * 2][4];
int index[maxN * 2];

bool comp(int x, int y)
{
	return a[x][3] < a[y][3];
}

void process()
{
	int x, s, r, n;
	double t;
	double answer = 0;
	int b[maxN];
	int e[maxN];
	int w[maxN];

	fin >> x >> s >> r >> t >> n;
	double last = 0;
	int len = 0;
	for (int i = 0; i < n; ++i)
	{
		fin >> b[i] >> e[i] >> w[i];
		if (last < b[i])
		{
			a[len][0] = (b[i] - last) * (r - s) / (double)(s * r);
			a[len][1] = last;
			a[len][2] = b[i];
			a[len][3] = s;
			len++;
		}

		if (b[i] < e[i])
		{
			a[len][0] = (e[i] - b[i]) * (r - s) / (double)(w[i] + s) / (w[i] + r);
			a[len][1] = b[i];
			a[len][2] = e[i];
			a[len][3] = w[i] + s;
			len++;
		}
		last = e[i];
	}
	if (last < x)
	{
		a[len][0] = (x - last) * (r - s) / (double)(s * r);
		a[len][1] = last;
		a[len][2] = x;
		a[len][3] = s;
		++len;
	}

	for (int i = 0; i < len; ++i)
		index[i] = i;

	sort(index, index + len, comp);

	int from = 0;
	while (from < len)
	{
		int at = index[from];
		double temp = (a[at][2] - a[at][1]) / (a[at][3] + r - s);
		if (temp < t + eps)
		{
			t -= temp;
			answer += temp;
		}
		else if (t > eps)
		{
			double fastwalk = t * (a[at][3] + r - s);
			answer += t + (a[at][2] - a[at][1] - fastwalk) / a[at][3];
			t = 0;
		}
		else
		{
			answer += (a[at][2] - a[at][1]) / a[at][3];
		}
		from++;
	}

	fout << setprecision(9) << answer;
}

int main()
{
	fin.open("in.txt", fstream::in);
	fout.open("out.txt", fstream::out);

	int testcase;
	fin >> testcase;
	for (int i = 1; i <= testcase; ++i)
	{
		fout << "Case #" << i << ": ";
		if (i == 24)
		{
			int sdf = 0;
		}
		process();
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}