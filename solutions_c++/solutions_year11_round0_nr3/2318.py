#include<iostream>

int main()
{
	std::ios::sync_with_stdio(0);
	short T; std::cin >> T;
	for(short i = 0; i < T; i++)
	{
		long sum_p = 0, sum_s = 0, min = 1000001;
		short N; std::cin >> N;
		for(short i = 0; i < N; i++)
		{
			long x; std::cin >> x;
			if(min > x) min = x;
			sum_s += x;
			sum_p ^= x;
		}
		std::cout << "Case #" << i+1 << ": ";
		if(sum_p)
			std::cout << "NO\n";
		else
			std::cout << sum_s-min << '\n';
	}
	return 0;
}
