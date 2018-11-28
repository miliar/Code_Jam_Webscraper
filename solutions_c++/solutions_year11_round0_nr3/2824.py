#include <iostream>
#include <vector>
#include <algorithm>

bool next_permutation(std::vector<bool>& perm)
{	
	for (int i = 0; i < perm.size(); i++)
	{
		perm[i] = !perm[i];
		
		if(i == perm.size() - 1) {return false;}
	    if(perm[i]) {return true;}
	}
	
	return false;
}

unsigned int test_candy_with_permutation(std::vector<unsigned int>& candy, std::vector<bool>& permutation)
{
	unsigned int p1_add = 0;
	unsigned int p1_xor = 0;
	
	unsigned int p2_add = 0;
	unsigned int p2_xor = 0;
	
	for (int i = 0; i < candy.size(); i++)
	{
		if (permutation[i])
		{
			p1_add += candy[i];
			p1_xor ^= candy[i];
		}
		else
		{
			p2_add += candy[i];
			p2_xor ^= candy[i];
		}
	}
	
	if (p1_xor == p2_xor)
	{
		return std::max(p1_add, p2_add);
	}
	
	return 0;
}

unsigned int test_candy(std::vector<unsigned int>& candy)
{
	std::vector<bool> permutation(candy.size());
	std::fill(permutation.begin(), permutation.end(), false);
	
	permutation[0] = true;
	
	unsigned int best = 0;
	do
	{		
		best = std::max(test_candy_with_permutation(candy, permutation), best);
	} while(next_permutation(permutation));
	
	return best;
}

void get_candy()
{
	std::vector<unsigned int> candy;
	
	int num_candy = 0;
	std::cin >> num_candy;
	
	for (num_candy; num_candy > 0; num_candy--)
	{
		int c;
		std::cin >> c;
		candy.push_back(c);
	}
	
	sort(candy.begin(), candy.end());
	
	unsigned int value = test_candy(candy);
	
	if (value == 0) {std::cout << "NO";}
	else {std::cout << value;}	
}

int main()
{
	int num_cases = 0;
	std::cin >> num_cases;
	
	for (int i = 1; i <= num_cases; i++)
	{
		std::cout << "Case #" << i << ": ";
		get_candy();
		std::cout << std::endl;
	}
	
	return 0;
};
