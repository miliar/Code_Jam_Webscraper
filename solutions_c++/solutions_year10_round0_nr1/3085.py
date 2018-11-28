#include <iostream>
#include <limits>
#include <algorithm>

bool perform(int n, int k)
{
	bool* state = new bool[n];
	bool* power = new bool[n];

	memset((void*)state, false, n * sizeof(bool));
	memset((void*)power, false, n * sizeof(bool));
	
	power[0] = true;
	
	for (int i = 0; i < k; ++i)
	{
		// First update state after snapping : if power -> switch it
		state[0] = ! state[0];
		for (int j = 1; j < n; ++j)
		{
			if (power[j])
				state[j] = ! state[j];
			else
				break;
		}
		
		// Second update power depending on the state of the previous one
		int j;
		for (j = 1; j < n; ++j)
		{
			if (power[j - 1] && state[j - 1])
				power[j] = true;
			else
				break;
		}
		
		for (; j < n; ++j)
			power[j] = false;
	}
	return power[n - 1] && state[n - 1];
}

int main()
{
	int nb_input = 0;
	std::cin >> nb_input;
	
	for (int i = 1; i <= nb_input; ++i)
	{
		int n, k;
		std::cin >> n >> k;
		
		bool b = perform(n, k);
		std::cout << "Case #" << i << ": ";
		if (b)
			std::cout << "ON" << std::endl;
		else
			std::cout << "OFF" << std::endl;
	}
	
	return 0;	
}