#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>

std::vector<int> primes;

void find_all_prime()
{
	for(int i =2; i < 1001;++i)
	{
		int count=0;
		for(int x = 0; x < primes.size() ; ++x)
		{
			if(i % primes[x] !=0)
			{
				count++;
			}
			else
			{
				break;
			}
		}
		if(count == primes.size())
		{
			primes.push_back(i);
		}
	}
}

void solve(int q_no)
{
	int result =0;
	
	long long v;
	std::cin >> v;

	if(v ==1)
	{
		result =0;
	}
	else
		result =1;
	
	for(int i =0; i < primes.size();++i)
	{
		if(primes[i] >= v)
		{
			break;
		}
		long long cmp = primes[i] * primes[i];
		while(cmp <= v)
		{
			result +=1;
			cmp = cmp * primes[i];
		}
	}

	std::cout << "Case #" << q_no << ": " << result << "\n";
}

int main(void)
{
	find_all_prime();
	int count;
	std::cin >> count;
	for(int i =0; i < count;++i)
	{
		solve(i+1);
	}
	return 0;
}
