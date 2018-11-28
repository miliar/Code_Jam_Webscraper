#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int intComp(const void* a, const void* b)
{
	return *(int*)a - *(int*)b;
}

int main()
{
	char* buffer = new char[1000];
	std::cin.getline(buffer, 1000);
	int numTests = strtol(buffer, NULL, 10);
	for (int test = 1; test <= numTests; test++)
	{
		std::cin.getline(buffer, 1000);
		char* tmpBuf = buffer;
		int numCandies = strtol(tmpBuf, &tmpBuf, 10);
		int* candies = new int[numCandies];
		int sum = 0, x = 0;

		std::cin.getline(buffer, 1000);
		tmpBuf = buffer;
		for (int i = 0; i < numCandies; i++)
		{
			candies[i] = strtol(tmpBuf, &tmpBuf, 10);
			sum += candies[i];
			x ^= candies[i];
			tmpBuf++;
		}
		if (x)
		{
			printf("Case #%d: NO\n", test);
			continue;
		}
		qsort(candies, numCandies, sizeof(int), intComp);
		printf("Case #%d: %d\n", test, sum-candies[0]);

		delete[] candies;
	}
	delete[] buffer;
}
