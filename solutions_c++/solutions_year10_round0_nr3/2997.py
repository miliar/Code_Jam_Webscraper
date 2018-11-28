#include <iostream>

struct step
{
	int value;
	int end;
};


long long perform(int r, int k, int n, int* tab, struct step* steps)
{
	// Preprocess all possible rides
	for (int i = 0; i < n; ++i)
	{
		int in_train = 0;
		int cur = i;

		while (true)
		{
			if (in_train + tab[cur] > k)
				break;
			else
			{
				in_train += tab[cur];
				if (cur == n - 1)
					cur = 0;
				else
					cur++;
				if (cur == i)
					break;
			}
		}
		
		steps[i].value = in_train;
		steps[i].end = cur;
	}
	
	long long res = 0;
	int cur = 0;

	// Compute final result
	for (int it = 0; it < r; ++it)
	{
		res += steps[cur].value;
		cur = steps[cur].end;
	}
	return res;
}

int main()
{
	int nb_input;
	std::cin >> nb_input;

	int tab[1024];
	struct step steps[1024];
	
	for (int i = 1; i <= nb_input; ++i)
	{
		int r, k, n;
		std::cin >> r >> k >> n; 
		
		for (int j = 0; j < n; ++j)
			std::cin >> tab[j];
			
		long long amount = perform(r, k, n, tab, steps);
		
		std::cout << "Case #" << i << ": " << amount << std::endl;
	}
	return 0;
}