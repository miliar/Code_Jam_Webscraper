#include <stdio.h>
#include <sstream>
using namespace std;


bool happy(int num, int base) 
{
	int sum = 0;
	int times = 0;

	while (num > 1)
	{
		sum = 0;
		while (num > 0)
		{
			int tmp = num % base;
			sum += tmp * tmp;
			num /= base;
		}
		num = sum;

		++times;
		if (times > 10000) break;
	}
	
	if (num == 1) 
	{
		return true;
	}

	return false;
}

int main()
{

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int numofbase;
	int base[10];
	int testcases;

	scanf("%d ", &testcases);

	for (int cases = 1; cases <= testcases; cases++)
	{
		char str[100];
		fgets(str, 100, stdin);

		istringstream scin(str);
		
		numofbase = 0;
		while (scin >> base[numofbase])
		{
			numofbase++;
		}

		int ans = -1;

		for (int num = 2; num <= 100000; ++num)
		{
			bool find = true;
			for (int i = 0; i < numofbase && find; i++)
			{
				if (!happy(num, base[i])) find = false;
			}
			if (find) 
			{
				ans = num;
				break;
			}
		}

		printf("Case #%d: %d\n", cases, ans);
	}

	return 0;
}
