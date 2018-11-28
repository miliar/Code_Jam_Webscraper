#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <algorithm>
using namespace std;

//---------------------------------------------
int xor_sum(std::vector<int> &a)
{
	int result = 0;
	vector<int>::iterator iter;
	for ( iter = a.begin( ) ; iter != a.end( ) ; iter++ )
		result = result ^ *iter;
	return result;
}

int sum(std::vector<int> &a)
{
	int result = 0;
	vector<int>::iterator iter;
	for ( iter = a.begin( ) ; iter != a.end( ) ; iter++ )
		result = result + *iter;
	return result;
}

int main ()
{
	int testsCount, n, k, result;
	std::vector<int> a1, a2;

	scanf_s("%d", &testsCount); 
	for (int testNo = 1; testNo <= testsCount; ++testNo)
	{
		scanf_s("%d", &n);

		a1.clear();
		a2.clear();

		a1.resize(n);
		result = 0;
		for (int i = 0; i < n; i++)
		{
			scanf_s("%d ", &k);
			result = result ^ k;
			a1[i] = k;
		}

		if (result != 0)
		{ 
			printf("Case #%d: NO", testNo);
			puts("");
			continue;
		}

		sort(a1.begin(), a1.end());
		for (int i = 1; i < n; i++)
		{
			a2.push_back(*a1.begin());
			a1.erase(a1.begin());
			if (xor_sum(a1) == xor_sum(a2))
				break;
		}


		printf("Case #%d: %d", testNo, std::max(sum(a1), sum(a2)));
		puts("");
	}

	return 0;
}
