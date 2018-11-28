#include <iostream>
#include <cstdlib>

int main()
{
	int T;
	std::cin >> T;
	for(int i = 0; i < T; ++i)
	{
		std::cout << "Case #" << i+1 << ": ";
		int N;
		std::cin >> N;
		int S;
		std::cin >> S;
		int p;
		std::cin >> p;
		int sumP = 0;
		int sumS = 0;
		for(int j = 0; j < N; ++j)
		{
			int ti;
			std::cin >> ti;
			if(ti == 0 && p != 0)
			{
				continue;
			}
			int surprise = 0;
			for(int k = 10; k >= p; --k)
			{
				int k3 = 3*k;
				if(k3 == ti || k3-1 == ti || k3-2 == ti)
				{
					++sumP;
					surprise = 0;
					break;
				}
				if(k3-3 == ti || k3-4 == ti)
				{
					surprise = 1;
				}			
			}
			sumS += surprise;
		}
		std::cout << (sumP + std::min(S, sumS)) << std::endl;
	} 
	return 0;
}
