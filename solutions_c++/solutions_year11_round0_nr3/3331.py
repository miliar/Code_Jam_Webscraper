#include <iostream>
#include <vector>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int compare(const void *a, const void *b)
{
	return (*(int *)a - *(int *)b);
}

void sort(int n, int *values)
{
	qsort(values, n, sizeof(int), compare);
}

void pick(int n, int *values, int sean_svalue, int sean_pvalue, int patrick_svalue, int patrick_pvalue, int &best)
{
	if (patrick_svalue != 0 && sean_pvalue == patrick_pvalue)
	{
		if (sean_svalue > best)
		{
			best = sean_svalue;
		}
	}

	for (int i = 0; i < n; i++)
	{
		pick(n - i - 1, values + i + 1, sean_svalue - values[i], sean_pvalue ^ values[i], patrick_svalue + values[i], patrick_pvalue ^ values[i], best);
	}
}

void solve(int n, int *values)
{
	int sean_svalue = 0;
	int sean_pvalue = 0;
	
	int best = 0;

	//sort(n, values);

	for (int i = 0; i < n; i++)
	{
		sean_svalue += values[i];
		sean_pvalue ^= values[i];
	}
	
	pick(n, values, sean_svalue, sean_pvalue, 0, 0, best);
	
	if (best == 0)
	{
		cout << "NO" << endl;
	}
	else
	{
		cout << best << endl;
	}
}


int main()
{
	uint64_t t;
	cin >> t;
	if (!cin) return -1;
	
	for (uint64_t i = 0; i < t; i++)
	{
		
		int n;
		cin >> n;
		if (!cin) return -1;
		int *values = new int[n];

		for (int j = 0; j < n; j++)
		{
			cin >> values[j];
			if (!cin) return -1;
		}
		
		cout << "Case #" << (i + 1) << ": ";
		solve(n, values);
	}
	
}

