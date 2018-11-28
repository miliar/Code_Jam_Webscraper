#include <cstdio>
#include <algorithm>

using namespace std;

int n;

int main()
{
	FILE* input = fopen("input1.txt", "r");
	FILE* output = fopen("output1.txt", "w");
	int T;
	fscanf(input, "%d", &T);
	int i;
	for (i = 0; i < T; i++)
	{
		fscanf(input, "%d\n", &n);
		int j, k;
		int row[40];
		char temp;
		for (j = 0; j < n; j++)
		{
			int max = 0;
			for (k = 0; k < n; k++)
			{
				fscanf(input, "%c", &temp);
				if (temp == '1')
					max = k;
			}
			row[j] = max;
			fscanf(input, "%*c");
		}
		int swaps = 0;
		for (j = 0; j < n; j++)
		{
			for (k = j; k < n; k++)
				if (row[k] <= j)
					break;
			for (k = k; k > j; k--)
			{
				swaps++;
				swap(row[k], row[k-1]);
			}
		}
		fflush(stdout);
		fprintf(output, "Case #%d: %d\n", i+1, swaps);
	}	
}