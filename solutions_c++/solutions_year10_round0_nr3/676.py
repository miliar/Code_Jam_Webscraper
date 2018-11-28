
#include <vector>
#include <cstdlib>
#include <numeric>
#include <fstream>
#include <iostream>

using namespace std;

std::vector<int64_t> circle;

int64_t roller(int64_t r, int64_t k, size_t g[], size_t n)
{
	size_t start = 0;
	int64_t total_gain = 0, per_gain = 0;

	// First round
	for ( ; start < n; ++start)
	{
		if ((total_gain + g[start]) <= k)	
		{
			total_gain += g[start];
		}
		else
		{
			break ;	
		}
	}

	// and that's enough
	if (start == n) return r * total_gain;

	// Full circle
	circle.clear();
	size_t i = start;
	while (true)
	{
		per_gain = 0;

		while (true)
		{
			if ((per_gain + g[i]) <= k)	
			{
				per_gain += g[i];
			}
			else
			{
				break ;	
			}

			++i;
			if (i == n) i = 0;
		}

		//
		circle.push_back(per_gain);

		//
		if (circle.size() == (r - 1))
		{
			return std::accumulate(circle.begin(), circle.end(), total_gain);
		}

		//
		if (i == start) break;
	}

	// Final
	int64_t quo = (r - 1) / circle.size();
	int64_t rem = (r - 1) % circle.size();

	total_gain += std::accumulate(circle.begin(), circle.end(), int64_t(0)) * quo;
	total_gain += std::accumulate(circle.begin(), circle.begin() + rem, int64_t(0));
	return total_gain;
}

int main(int argc, char** argv) 
{
	size_t t, n;
	int64_t r, k;
	size_t g[2000];
	
	std::ifstream fin("C-large.in");
	std::ofstream fout("C-large.out");
	
	fin >> t;
	for (size_t i = 0; i < t; ++i)
	{
		fin >> r >> k >> n;

		for (size_t j = 0; j < n; ++j)
		{
			fin >> g[j];
		}

		fout << "Case #" << i + 1 << ": " << roller(r, k, g, n) << std::endl;
	}

	fin.close();
	fout.close();

    return (0);
}

