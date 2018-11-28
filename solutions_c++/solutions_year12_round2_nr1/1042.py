#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

struct S
{
	int s;
	int i;
	bool incl;
};

S s[200];

void solve(istream& input, ostream& output)
{
	int n;
	input >> n;
	double dsum = 0, sum = 0;
	for (int i = 0; i < n; ++i)
	{
		s[i].i = i;
		s[i].incl = true;
		input >> s[i].s;
		sum += s[i].s;
		dsum += 2 * s[i].s;
	}

	int nn = n;
	sort(s, s + n, [](const S& s1, const S& s2) { return s1.s > s2.s; });
	for (int i = 0; i < n; ++i)
	{
		if (s[i].s <= dsum / nn)
			break;
		dsum -= s[i].s;
		s[i].incl = false;
		--nn;
	}
	sort(s, s + n, [](const S& s1, const S& s2) { return s1.i < s2.i; });

	output.precision(6);
	output.flags(ios_base::fixed);
	for (int i = 0; i < n; ++i)
	{
		if (!s[i].incl)
			output << "0.000000 ";
		else
			output << 100 * (dsum / nn - s[i].s) / sum << " ";
	}
}

int main()
{
	ifstream fin("A-large.in");
	int t;
	fin >> t;
	ofstream cout("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve(fin, cout);
		cout << "\n";
	}
}