// C.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

std::ifstream in("c.in");
std::ofstream out("c.out");
int T;
int N, P;
std::vector< int > prisoners;

long long res(int b, int e)
{
	long long result = 0;
	for (int i = 0; i < (int)prisoners.size(); i++)
	{
		if (prisoners[i] > b && prisoners[i] < e)
		{
			long long r = e - b - 2 + res(b, prisoners[i]) + res(prisoners[i], e);
			if (r < result || result == 0)
			{
				result = r;
			}
		}
	}
	return result;
}

int main()
{
	in >> T;
	for (int t = 0; t < T; t++)
	{
		in >> P >> N;
		prisoners.clear();
		prisoners.resize(N);
		for (int i = 0; i < N; i++)
		{
			in >> prisoners[i];
		}
		out << "Case #" << t + 1 << ": " << res(0, P + 1) << std::endl;
	}
	return 0;
}

