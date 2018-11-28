#include <cmath>
#include <iostream>

inline int max(const int& a, const int& b) {return a > b ? a : b;}

int main()
{
	int t;
	std::cin >> t;
	for (int currtest = 1; currtest <= t; currtest++)
	{
		int n;
		std::cin >> n;
		int lposo = 1, lposb = 1, ltmo = 0, ltmb = 0;
		int time = 0;
		for (int i = 0; i < n; i++)
		{
			char c; int cp;
			std::cin >> c >> cp;
			
			if (c == 'O')
			{
				time += max(0, std::abs(lposo - cp) - (time-ltmo)) + 1;
				ltmo = time;
				lposo = cp;
			} else
			{
				time += max(0, std::abs(lposb - cp) - (time-ltmb)) + 1;
				ltmb = time;
				lposb = cp;
			}
		}
		
		std::cout << "Case #" << currtest << ": " << time << '\n';
	}

	return 0;
}
