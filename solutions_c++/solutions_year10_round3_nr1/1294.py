
#include <cmath>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef std::pair<int, int> loc;

std::vector<loc> wires;

int max_inter(int n)
{
	if (n == 1)
	{
		return 0; 
	}
	else
	{
		return max_inter(n - 1) + n - 1;
	}
}

int calc()
{
	int r = max_inter(wires.size());

	for(int i = 0; i < wires.size(); ++i)
	{
		for (int j = (i + 1); j < wires.size(); ++j)
		{
			if ((wires[j].first < wires[i].first) && (wires[j].second < wires[i].second))
			{
				--r;
			}
			else if ((wires[j].first > wires[i].first) && (wires[j].second > wires[i].second))
			{
				--r;
			}
			else if ((wires[j].first - wires[i].first) == (wires[j].second - wires[i].second))
			{
				--r;
			}
		}
	}

	return r;
}

int main(int argc, char** argv) 
{
	std::ifstream fin("A-small.in");
	std::ofstream fout("A-small.out");

	size_t t;
	fin >> t;

	size_t n;
	for (size_t i = 0; i < t; ++i)
	{
		wires.clear();

		fin >> n;
		for (size_t j = 0; j < n; ++j)
		{
			loc x;
			fin >> x.first >> x.second;
			wires.push_back(x);
		}

                fout << "Case #" << i + 1 << ": " << calc() << std::endl;
	}

	fin.close();
	fout.close();

    return (EXIT_SUCCESS);
}

