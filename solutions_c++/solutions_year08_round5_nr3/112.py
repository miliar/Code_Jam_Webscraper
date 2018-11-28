#include <stdlib.h>
#include <stdio.h>

int table[100][100];
char aline[100];
int states[2000];
int states2[2000];
bool arr1[100];
bool arr2[100];

int main()
{
	int numCase;
	scanf("%d", &numCase);
	int i, j, k, l, m, n;
	for (i = 0; i < numCase; i++)
	{
		int row, col;
		scanf("%d %d", &row, &col);
		for (j = 0; j < row; j++)
		{
			scanf("%s", aline);
			for (k = 0; k < col; k++)
			{
				if (aline[k] == '.')
					table[j][k] = 0;
				else
					table[j][k] = 1;
			}
		}
		int max = (1 << col);
		for (j = 0; j < max; j++)
			states[j] = 0;
		for (j = 0; j < row; j++)
		{
			for (k = 0; k < max; k++)
			{
				states2[k] = 0;
				int count2 = 0, count1 = 0;
				for (l = 0; l < col; l++)
				{
					if ((k & (1 << l)) == 0)
						arr2[l] = false;
					else
					{
						arr2[l] = true;
						count2++;
					}
				}
				bool valid = true;
				for (l = 1; l < col; l++)
				{
					if (arr2[l] && arr2[l-1])
					{
						valid = false;
						break;
					}
				}
				for (l = 0; l < col; l++)
				{
					if (arr2[l] && table[j][l] == 1)
					{
						valid = false;
						break;
					}
				}
				if (valid)
				{
					for (l = 0; l < max; l++)
					{
						valid = true;
						for (m = 0; m < col; m++)
						{
							if ((l & (1 << m)) == 0)
								arr1[m] = false;
							else
							{
								arr1[m] = true;
								count1++;
							}
						}
//						printf("Passed first %d from %d\n", k, l);
						for (m = 0; m < col; m++)
						{
//							printf("Testing %d\n", m);
							if (arr2[m])
							{
								if (m > 0 && arr1[m-1])
								{
									valid = false;
									break;
								}
								if (m < col-1 && arr1[m+1])
								{
									valid = false;
									break;
								}
							}
//							printf("Finished %d\n", m);
						}
						if (valid)
						{
//							printf("Passed %d from %d\n", k, l);
							if (states2[k] < states[l] + count2)
							{
//								printf("Updating %d from %d\n", k, l);
								states2[k] = states[l] + count2;
							}
						}
					}
				}
			}
			for (k = 0; k < max; k++)
			{
				states[k] = states2[k];
//				printf("%d %d %d\n", j, k, states[k]);
			}
		}
		int result = 0;
		for (j = 0; j < max; j++)
		{
			if (states[j] > result)
				result = states[j];
		}
		printf("Case #%d: %d\n", i+1, result);
//		exit(0);
	}
	return 0;
}
