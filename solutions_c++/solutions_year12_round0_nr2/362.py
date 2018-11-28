#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

void solve(istream& input, ostream& output)
{
	int N, S, p;
	input >> N >> S >> p;

	int n1 = 0, n2 = 0;
	for (int i = 0; i < N; ++i)
	{
		int t, t1 = 0, t2 = 0;
		input >> t;
		if (t > 0)
		{
			t1 = t / 3 + (t % 3 + 1) / 2;
			t2 = t / 3 + 1 + (t % 3) / 2;
		}

		if (t1 >= p)
			++n1;
		else if (t1 < p && t2 == p)
			++n2;
	}
	output << n1 + min(n2, S) << ' ';
}

void main()
{
	int n;

	ifstream fin("B-large.in");
	fin >> n;

	ofstream fout("output.txt");

	for (int i = 1; i <= n; ++i)
	{
		fout << "Case #" << i << ": ";
		solve(fin, fout);
		fout << '\n';
	}
}