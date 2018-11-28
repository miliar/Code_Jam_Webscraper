
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int best = -1;
vector<int> v;
vector<int> a, b;
int N;

void split(int n, bool inA)
{
	if (inA)
	{
		a.push_back(v[n]);
	}
	else
	{
		b.push_back(v[n]);
	}

	if (n == N-1)
	{
		if (!a.empty() && !b.empty())
		{
			int sumA = 0;
			int realSumA = 0;
			for (size_t i=0; i<a.size(); ++i)
			{
				sumA ^= a[i];
				realSumA += a[i];
			}

			int sumB = 0;
			int realSumB = 0;
			for (size_t i=0; i<b.size(); ++i)
			{
				sumB ^= b[i];
				realSumB += b[i];
			}

			if (sumA == sumB)
			{
				int result = max(realSumA, realSumB);
				best = max(best, result);
			}
		}
	}
	else
	{
		split(n+1, true);
		split(n+1, false);
	}

	if (inA)
	{
		a.pop_back();
	}
	else
	{
		b.pop_back();
	}
}

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("C_small.txt");

	int T;
	in >> T;

	for (int i=0; i<T; ++i)
	{
		v.clear();
		a.clear();
		b.clear();
		best = -1;

		in >> N;

		for (int j=0; j<N; ++j)
		{
			int c;
			in >> c;
			v.push_back(c);
		}

		split(0, true);
		split(0, false);

		if (best == -1)
		{
			cout << "Case #" << i+1 << ": NO" << endl;
			out << "Case #" << i+1 << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << best << endl;
			out << "Case #" << i+1 << ": " << best << endl;
		}
	}

	return 0;
}
