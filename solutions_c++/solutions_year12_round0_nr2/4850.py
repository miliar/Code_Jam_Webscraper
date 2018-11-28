#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}
int main()
{
	int cases = 0;
	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		int count = 0;
		int number = 0;
		int surprise = 0;
		int value = 0;
		cin >> number >> surprise >> value;
		int *score;
		score = new int [number];
		int input;


		for (int j = 0; j < number; j++)
		{
			cin >> input;
			score[j] = input;			
		}
		qsort (score, number, sizeof(int), compare);

		for (int m = 0; m < number; m++)
		{
			if (surprise > 0)
			{
				if (score[m] == 0)
				{
					if (value == 0)
						count++;
				}
				else if (score[m] == 1)
				{
					if (value <= 1)
						count++;
				}
				else
				{
					if ((score[m] + 4) / 3 >= value)
					{
						count++;
						surprise--;
					}
				}
			}
			else
			{
				if (score[m] == 0)
				{
					if (value == 0)
						count++;
				}
				else
				{
					if ((score[m] + 2) / 3 >= value)
					{
						count = count + (number - m);
						break;
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
		delete [] score;
	}
	return 0;
}