// task.cpp: определяет точку входа для консольного приложения.
//
#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

int main()
{	
	#if 1
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	int tests;
	cin >> tests;
	int n, sum, cur = 0, min, sumXOR;
	for (int t = 0; t < tests; ++t)
	{
		cin >> n;		
		sum = 0;
		sumXOR = 0;
		for (int i = 0; i < n; ++i )
		{
			cin >> cur;
			if (i == 0)
			{
				min = cur;
			} else
			{
				if ( cur < min ) min = cur;
			}
			sum +=cur;
			sumXOR ^=cur;
		}	
		if (sumXOR == 0)
		{
			cout << "Case #" <<  t+1 << ": " << sum - min << endl;
		} else
		{
			cout << "Case #" << t+1 << ": " << "NO" << endl;
		}
	}
	return 0;
}