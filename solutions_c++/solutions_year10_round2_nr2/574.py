
#include <vector>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef std::pair<size_t, double> mychick;

size_t n, k, b, t;
std::vector<size_t> chick_loc;
std::vector<size_t> chick_spd;
std::vector<mychick> chick_tim;

class pred : public std::unary_function<mychick const &, bool>
{
public:
	bool operator()(mychick const & a) const
	{
		return (a.second <= (double)(t)) ? false : true;
	}
};

int calc()
{
	for (size_t i = 0; i < n; ++i)
	{
		double time_require = ((double)(b - chick_loc[i])) / chick_spd[i];
		chick_tim.push_back(std::make_pair(i, time_require));	
	}

	std::stable_partition(chick_tim.begin(), chick_tim.end(), pred());

	size_t total = 0;
	size_t number = 0;
	for (size_t i = chick_tim.size() - 1; i >= 0, number < k; --i)
	{
		if (chick_tim[i].second <= (double)(t))
		{
			total += i - chick_tim[i].first;
			++number;
		}
		else
		{
			break;
		}
	}
	
	return (number != k) ? (-1) : total;
}

int main(int argc, char** argv) 
{
	std::ifstream fin("B-large.in");
	std::ofstream fout("B-large.out");

	size_t c;
	fin >> c;

	for (size_t i = 0; i < c; ++i)
	{
		chick_loc.clear();
		chick_spd.clear();
		chick_tim.clear();

		fin >> n >> k >> b >> t;

		size_t loc, spd;
		for (size_t j = 0; j < n; ++j)
		{
			fin >> loc;
			chick_loc.push_back(loc);
		}

		for (size_t j = 0; j < n; ++j)
		{
			fin >> spd;
			chick_spd.push_back(spd);
		}
		
		int r = calc();
		if (r == (-1))
		{
			fout << "Case #" << i + 1 << ": IMPOSSIBLE" << std::endl;
		}
		else
		{
			fout << "Case #" << i + 1 << ": " << r << std::endl;
		}
	}

	fin.close();
	fout.close();

    return (EXIT_SUCCESS);
}

