#include <iostream>
#include <vector>
#include <algorithm>


int share(unsigned int n, unsigned int* candies, unsigned int me, unsigned int him, unsigned int taken, unsigned int score)
{
	if(n == 0)
	{
		if(me == him && taken)
			return score;
		else
			return -1;
	}

	return std::max(share(n-1, candies + 1, me ^ *candies, him, taken - 1, score + *candies),
			share(n-1, candies + 1, me, him ^ *candies, taken, score));

}

void solve()
{
	unsigned int n;
	std::cin >> n;

	unsigned int l[n];
	for(unsigned int i=0; i < n; i++)
		std::cin >> l[i];

	unsigned int poorcandy = (unsigned int)-1;

	for(unsigned int i=0; i < n; i++)
	{

		unsigned int x = 0;

		for(unsigned int j=0; j != n; j++)
			if(j != i)
				x ^= l[j];

		if(x == l[i] && x < poorcandy)
			poorcandy = x;
	}

	if(poorcandy == (unsigned int)-1)
	{
		std::cout << "NO";
		return;
	}

	unsigned int sum = 0;
	for(unsigned int i=0; i < n; i++)
		sum += l[i];
	sum -= poorcandy;
	std::cout << sum;
}

int main()
{
	unsigned int n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(unsigned int i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}

