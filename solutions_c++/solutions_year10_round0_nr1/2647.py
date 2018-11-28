#include <iostream>
#include <boost/format.hpp>
#include <cstdint>

int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;

	bool f[10];
	bool f2[10];
	for(int c = 0; c < T; ++c)
	{
		memset(f, 0, sizeof(f));
		memset(f2, 0, sizeof(f2));
		int N, K;

		std::cin >> N >> K;

		int mask = 0;
		for(int i = 0; i < N; ++i)
		{
			mask |= 1 << i;
		}

		std::string a1 = (K & mask) == mask ? "ON" : "OFF";
			
		std::cout << boost::format("Case #%d: %s\n") % (c+1) % a1;
	}

	return 0;
}