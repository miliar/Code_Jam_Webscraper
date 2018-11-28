#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main ()
{
	int testsCount, n, k, result;
	std::vector<int> aSource, aEtalon;

	scanf_s("%d", &testsCount); 
	for (int testNo = 1; testNo <= testsCount; ++testNo)
	{
		scanf_s("%d", &n);

		aSource.clear();
		aEtalon.clear();

		aSource.resize(n);
		for (int i = 0; i < n; i++)
		{
			scanf_s("%d ", &k);
			aSource[i] = k;
		}

		vector<int>::iterator iter;
		for ( iter = aSource.begin( ) ; iter != aSource.end( ) ; iter++ )
			aEtalon.push_back(*iter);
		sort(aEtalon.begin(), aEtalon.end());

		result = 0;
		for (int i = 0; i < n; i++)
		{
			if (aSource[i] != aEtalon[i])
				result++;
		}


		printf("Case #%d: %d", testNo, result);
		puts("");
	}

	return 0;
}
