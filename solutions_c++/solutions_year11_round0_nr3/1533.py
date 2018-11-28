#include <iostream>
#include <stdio.h>
using namespace std;
int array[1000];
int n;
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> n;
		int value = 0, total = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> array[i];
			value ^= array[i];
			total += array[i];
		}
		printf("Case #%d: ", cases);
		if (value != 0) puts("NO");
		else {
			value = array[0];
			for (int i = 1; i < n; i++)
				if (value > array[i]) value = array[i];
			printf("%d\n", total - value);
		}
	}
}