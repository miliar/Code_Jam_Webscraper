// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

bool SortGreater(int a, int b)
{
	return a > b;
}

bool SortLesser(int a, int b)
{
	return a < b;
}

int main(void)
{
	ifstream       input;
	int            caseCount = 0;
	int            i         = 0;
	int            j         = 0;
	int            k         = 0;
	int            n         = 0;
	_int64         as        = 0;
	_int64         s         = 0;
	_int64         r         = 0;
	_int64         x         = 0;
	ofstream       output;
	string         outputString;
	vector < int > v1;
	vector < int > v2;

	input.open("Minimum Scalar Product.in", ios_base::in);
	output.open("Minimum Scalar Product.out", ios_base::out);

	input >> caseCount;
	for (i = 0; i < caseCount; i++)
	{
		v1.erase(v1.begin(), v1.end());
		v2.erase(v2.begin(), v2.end());

		input >> n;
		for (j = 0; j < n; j++)
		{
			input >> k;
			v1.push_back(k);
		}

		for (j = 0; j < n; j++)
		{
			input >> k;
			v2.push_back(k);
		}

		sort(v2.begin(), v2.end(), SortGreater);
		sort(v1.begin(), v1.end(), SortLesser);

		r = 0;
		for (j = 0; j < n; j++)
		{
			r += v1[j] * v2[j];
		}

		sort(v2.begin(), v2.end(), SortLesser);
		sort(v1.begin(), v1.end(), SortGreater);

		s = 0;
		for (j = 0; j < n; j++)
		{
			s += v1[j] * v2[j];
		}

		s = s < r ? s : r;
		as = s < 0 ? -s : s;

		for (x = 1; x < as; x *= 10);
		x /= 10;

		if (s < 0)
			outputString = "-";
		else
			outputString = "";

		if (x)
		{
			for (x = x; x > 0; x /= 10)
			{
				outputString += as / x + '0';
				as %= x;
			}
		}

		output << "Case #" << i + 1 << ": " << outputString.c_str() << endl;
	}

	input.close();
	output.close();

	return 0;
}

