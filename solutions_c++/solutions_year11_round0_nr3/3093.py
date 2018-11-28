#include <iostream>
#include <stdio.h>

using namespace std;

static int max = 0;

void computeValues(int output[], int level, int n, int values[])
{
	if (level + 1 == n)
		return;

	int res1 = 0, res1_1 = 0;

	for (int j=0; j <= level; j++)
	{
		res1 ^= values[output[j]];
		res1_1 += values[output[j]];
	}

	int idx = 0, res2 = 0, res2_1 =0;

	for (int i=0; i<n; i++)
	{
		if (idx <= level && i == output[idx])
		{
			idx += 1;
			continue;
		}
		res2 ^= values[i];
		res2_1 += values[i];
	}

	if (res1 == res2 && res1_1 > max)
	{
		max = res1_1;
	}
	if (res1 == res2 && res2_1 > max)
	{
		max = res2_1;
	}
}

void combination(int input[], int output[],int level,int start, int n, int values[])
{
	for (int i=start; i < n; i++)
	{
		output[level] = input[i];

		computeValues(output,level,n,values);

		combination(input,output,level+1,i+1,n,values);
	}
}

int main()
{
	int t = 0;

	cin >> t;

	for (int testcase = 1; testcase <= t; testcase++)
	{
		max = 0;

		int n = 5;
		cin >> n;

		int input[n];
		int output[n];
		int values[n];
		for (int k=0; k<n; k++)
		{
			cin >> values[k];
			input[k] = k;
		}

		int res = 0;
		for (int k=0; k<n; k++)
		{
			res ^= values[k];
		}
		if (0 != res)
		{
			cout << "Case #" << testcase << ": NO" << endl;
		}
		else
		{
			combination(input,output,0,0,n,values);
			cout << "Case #" << testcase << ": " << max << endl;
		}
	}
}