#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/format.hpp>
#include <iterator>
#include <algorithm>

int main(int argc, char * argv[])
{
	std::string line;
	std::getline(std::cin, line);

	int T;
	T = boost::lexical_cast<int>(line);

	

	for(int t = 0; t < T; ++t)
	{
		std::getline(std::cin, line);
		
		int N = boost::lexical_cast<int>(line);

		std::vector<int> v;
		v.resize(N);

		
		std::getline(std::cin, line);
		std::stringstream buf(line);
		std::copy_n(std::istream_iterator<int>(buf), N, v.begin());

		int c = 0;

		for(int i = 0; i < N; ++i)
		{
			c ^= v[i];
		}
		
		if(c != 0)
		{
			std::cout<< boost::format("Case #%d: NO") % (t+1) << std::endl;
			continue;
		}

		std::sort(v.begin(), v.end());
		
		int sum = 0;
		c = 0;
		for(int i = 1; i < N; ++i)
		{
			sum += v[i];
			c ^= v[i];
		}

		assert(v[0] == c);

		std::cout << boost::format("Case #%d: %d") % (t+1) % sum << std::endl;
	}

	return 0;
}
