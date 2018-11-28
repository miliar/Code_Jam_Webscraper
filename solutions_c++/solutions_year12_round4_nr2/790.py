#include <queue>
#include <cmath>
#include <random>
#include <vector>
#include <string>
#include <cstdlib>
#include <numeric>
#include <iterator>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
double w;
double l;
std::vector<double> x;
std::vector<double> y;
std::vector<double> rad;

const int TRY = 100;

std::default_random_engine re;

bool Solve(int now)
{
	if(now >= n)
	{
		return true;
	}

	for(int step = 0; step < TRY; step++)
	{
		std::uniform_real_distribution<double> xr(0, w);
		std::uniform_real_distribution<double> yr(0, l);
		x[now] = xr(re);
		y[now] = yr(re);

		bool suit = true;
		for(int i = 0; i < now; i++)
		{
			double dx = x[i] - x[now];
			double dy = y[i] - y[now];
			if(sqrt(dx * dx + dy * dy) < rad[i] + rad[now])
			{
				suit = false;
				break;
			}
		}

		if(suit && Solve(now + 1))
		{
			return true;
		}
	}

	return false;
}

int main(int argc, char * argv[])
{
	int testCount;
	freopen("in.txt", "r", stdin);
	std::cin >> testCount;
	for(int test = 1; test <= testCount; test++)
	{
		std::cin >> n >> w >> l;
		rad.clear();
		x.resize(n);
		y.resize(n);
		std::copy_n(std::istream_iterator<double>(std::cin), n, std::back_inserter(rad));
		if(Solve(0))
		{
			std::cout << "Case #" << test << ": ";
			for(int i = 0; i < n; i++)
			{
				std::cout << x[i] << ' ' << y[i] << ' ';
			}

			std::cout << std::endl;
		}
	}

	return 0;
}