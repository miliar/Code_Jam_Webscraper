#include<stdio.h>
using namespace std;

int main()
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1 ; test_case <= num_test_cases; test_case++)
	{
		int num_numbers;
		int parity[30] = {0};
		scanf("%d",&num_numbers);
		int minimum;
		unsigned long sum=0;
		for (int i=0 ; i<num_numbers; i++)
		{
			unsigned int num;
			scanf("%d",&num);
			for (int j=0; j < 31 ; j++)
			{
				if(((1 << j) & num ) > 0)
					parity[j]++;
			}
			if (i==0)
			{
				minimum = num;
			}
			else
			{
				if (num < minimum)
				{
					minimum = num;
				}
			}
			sum+=num;
		}
		bool parityCheck = true;
		for (int i=0; i < 31; i++)
		{
			if(parity[i]%2 != 0)
				parityCheck = false;
		}
		if (!parityCheck)
		{
			printf("Case #%d: NO\n",test_case);
		}
		else
		{
			printf("Case #%d: %ld\n",test_case, sum - minimum);
		}
	}
}
