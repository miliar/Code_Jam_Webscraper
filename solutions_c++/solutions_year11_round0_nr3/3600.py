#include <iostream>
#include <fstream>
#include <iterator>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int N = 0;
std::vector<int> * C = NULL;

void LoadData()
{
	fstream is("data.in", ios_base::in);
	is >> N;
	C = new vector<int>[N];

	for (int i = 0; i < N; ++i)
	{
		int T = 0;
		is >> T;
		for (int j = 0; j < T; ++j)
		{
			int v = 0;
			is >> v;
			C[i].push_back(v);
		}			
	}
}

int SolveCase(const int & c)
{
	vector<int> & v = C[c];
	int lMax = -1;
	sort (v.begin(), v.end());
	{ 
		for (int k = 1; k < v.size(); ++k)
		{
			int xs = 0; // sean
			int ys = 0; // sean
			int xp = 0; // patrick
			int yp = 0; // patrick
			for (int i = 0; i < k; ++i)
			{
				xs += v[i];
				xp ^= v[i];
			}

			for (int i = v.size() - 1; i >= k; --i)
			{
				ys += v[i];
				yp ^= v[i];
			}

			if (xp == yp)
			{
				lMax = max(max(xs, ys), lMax);
			}
		}
	}
	return lMax;
}

int main()
{
	LoadData();
	fstream os("data.out", ios_base::out);
	for (int i = 0; i < N; ++i)
	{
		int r = SolveCase(i);
		os << "Case #" << i + 1 << ": ";
		if (r == -1)
			os << "NO";
		else
			os << r;
		os << endl;
	}

}