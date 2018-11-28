#include <iostream>
#include <fstream>

int rollercoaster(int r, int k, int n, int g[])
{
	int sum = 0, j = 0;
	for(int i = 0; i < r; i++)
	{
		int startj = j;
		int currnum = 0;
		for(;;)
		{
			if((j == startj || (j%n != startj%n)) && ((currnum + g[j%n]) <= k))
			{
				currnum += g[j%n];
			}
			else
				break;
		
			j++;
		}
		
		sum += currnum;
	}
	return sum;
}

int main(int argc, char* argv[])
{
	std::ifstream input;
	input.open(argv[1]);

	int num_cases;
	input >> num_cases;

	int i = 1;
	while(num_cases--)
	{
		int r,k,n;
		input >> r;
		input >> k;
		input >> n;

		int* g = new int[n];

		for (int j = 0; j < n; j++)
			input >> g[j];

		std::cout << 
			"Case #" << 
			i++ << ": ";
			
		std::cout << rollercoaster (r,k,n,g);

		std::cout << std::endl;
	}
	return 0;
}
