#include <iostream>
#include <boost/format.hpp>
#include <cmath>

int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;

	for(int t = 0; t < T; ++t)
	{
		int L, P, C;

		std::cin >> L >> P >> C;

		double val = ceil(log(log(double(P)/double(L))/log(double(C)))/log(2.));

		std::cout << boost::format("Case #%d: %d\n") % (t+1) % int(val > 0 ? val : 0);
	}
}