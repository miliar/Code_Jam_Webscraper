#include <iostream>

using namespace std;

int main()
{

	int testcase;

	cin >> testcase;

	int* result = new int[testcase];

	for (int t = 0; t < testcase; t++)
	{
		int a, b;
		int count = 0;

		cin >> a >> b;

		int k = 10;
		while (a/(k*10))
		{
			k *= 10;
		}

		for (int i = a; i <= b; i++)
		{
			int p = k;
			int num, rem;
			int j = 10;

			while (p >= 10)
			{
				num = i / j;
				rem = i % j;

				num = rem * p + num;

				if ((num <= b) && (num >= a) && (i < num))
				{
					count++;
					//cout << count << ":" << i << "\t" << num << endl;
				}

				p /= 10;
				j *= 10;
			}
		}

		//cout << "\nCount = " << count;
		result[t] = count;
	}

	for (int t = 0; t < testcase; t++)
	{
		cout << "Case #" << t+1 << ": " << result[t] << endl;
	}

	delete[] result;
}