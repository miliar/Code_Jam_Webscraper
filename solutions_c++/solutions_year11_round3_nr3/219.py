#include <vector>
#include <iostream>

using std::vector;

inline bool divides(const long long& a, const long long& b)
{
	return (a > b ? !(a % b) : !(b % a));
}

int main()
{
	int tests;
	std::cin >> tests;
	for (int currtest = 1; currtest <= tests; currtest++)
	{
		int n;
		long long min, max;
		std::cin >> n >> min >> max;
		
		vector<long long> freqs(n);
		for (int i = 0; i < n; i++)
			std::cin >> freqs[i];
			
		long long ans = 0;
		for (long long cf = min; cf <= max; cf++)
		{
			bool ok = true;
			for (int i = 0; i < n; i++)
				if (!divides(cf, freqs[i]))
				{
					ok = false;
					break;
				}
				
			if (ok)
			{
				ans = cf;
				break;
			}
		}
	
		if (ans != 0)
			std::cout << "Case #" << currtest << ": " << ans << '\n';
		else std::cout << "Case #" << currtest << ": " << "NO" << '\n';
	}

	return 0;
}
