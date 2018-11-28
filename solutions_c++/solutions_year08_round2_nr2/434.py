#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int findParent(vector<int> &arr, int pos)
{
	while(arr[pos] != -1)
	{
		pos = arr[pos];
	}

	return pos;
}

int main()
{
	int C;
	cin >> C;

	int caseNum = 1;

	vector<int> primes;
	primes.push_back(2);

	long long k = 1000;
	for(long long i = 3; i <= k; ++i)   
	{   
		bool flag = false;
		int sk = sqrt(double(i)); 
		for(int j = 2; j <= sk; ++j)   
		{   
			if(i % j == 0)   
			{   
				flag = true;
				break;
			}   
		}   
		if(!flag)
		{   
			primes.push_back(i); 
		}   
	}

	do
	{
		long A, B, P;
		cin >> A >> B >> P;

		int a = 0;
		int end;
		int sz = (int)primes.size();
		for (; a < sz; ++a)
		{
			if (primes[a] >= P)
			{
				break;
			}
		}
		for (end = sz - 1; end >= a; --end)
		{
			if (primes[end] > B / 2)
			{
				break;
			}
		}

		vector<int> parent(B - A + 1, -1);

		for (int i = A; i <= B; ++i)
		{
			for (int j = A + 1; j <= B; ++j)
			{
				for (int k = a; k <= end; ++k)
				{
					if (i % primes[k] == 0 && j % primes[k] == 0 && findParent(parent, i - A) != findParent(parent, j - A))
					{
						parent[findParent(parent, j - A)] = findParent(parent, i - A);
					}
				}
			}
		}

		int result = 0;
		for (int i = 0; i < (int)parent.size(); ++i)
		{
			if (parent[i] == -1)
			{
				++result;
			}
		}
		printf("Case #%d: %ld\n", caseNum++, result);
	} while (caseNum <= C);

	return 0;
}

