#include <math.h>
#include <iostream>

using namespace std;

long long nthpower(long long i)
{
	int temp  = i, flag = 1;;
	for (int j = 2; j <= sqrt(i); j++)
	{
		
		temp = i;
		if(temp%j == 0)
		{
			flag = 1;
			while(temp > 1)
			{
				if(temp%j)
				{	flag = 0;
					break;
				}
				else
					temp =  temp/j;
			}
			return flag;
		}
	}
	return flag;
}

bool prime(long long i)
{
	bool flag = 1;
	for (long long j = 2; j <= sqrt(i); j++)
	{
		if(i%j == 0)
		{	flag = 0;
			break;
		}
	}
	return flag;
}

long long count_primes(long long  N)
{
	long long count = 0;
	for (long long i = 1; i <=N; i++)
	{
		if (prime(i))
			count++;
	}
	return count - 1;
}
int main()
{
	long long T,N, max_wcall = 0, min_wcall = 0, lcm = 1,spread, temp =  1;
	cin>>T;
	while(temp <= T)
	{
		
		cin>>N;
		lcm  = 1,max_wcall = 0, min_wcall =0, spread =0;
		for (long long i = 1; i <= N; i++)
		{
			if (i == 1)
				max_wcall++;
			else if (prime(i))
				max_wcall++;
			else if (nthpower(i))
				max_wcall++;
		}
		if (N == 1)
			min_wcall  = 1;
		else
			min_wcall = count_primes(N);
		spread = max_wcall - min_wcall;
		cout<<"Case #"<<temp<<": "<<spread<<endl;
		temp++;
	}
}
