#include <stdio.h>
#include <math.h>

int main()
{
//	freopen("in.in","r",stdin);freopen("out.out","w",stdout);
//	freopen("C-small-attempt3.in","r",stdin);freopen("C-small-attempt3.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase = 0;
	scanf("%d",&testcase);
	for (int caseId=1; caseId<=testcase; caseId++)
	{
		int candyNumber = 0;
		scanf("%d", &candyNumber);

		int* candies = new int[candyNumber];

		for (int i = 0; i < candyNumber; i++)
		{
			scanf("%d", &candies[i]);
		}

		for (int i = 0; i < candyNumber-1; i++)
		{
			for (int j = i; j < candyNumber; j++)
			{
				if (candies[i] > candies[j])
				{
					int temp = candies[i];
					candies[i] = candies[j];
					candies[j] = temp;
				}
			}
		}

		{
			int s1 = 0;
			int s2 = 0;
			unsigned long long maxSum = 0;

			unsigned long long s1dec = 0;
			unsigned long long s2dec = 0;

			// mowem
			for (int i = 0; i < (candyNumber-1); i++)
			{
				s1 = 0;
				s2 = 0;
				s1dec = 0;
				s2dec = 0;

				for (int i1 = 0; i1 <= i; i1++)
				{
					s1 = s1 ^ candies[i1];
					s1dec += (unsigned long long)candies[i1];
				}

				for (int i2 = (i+1); i2 < candyNumber; i2++)
				{
					s2 = s2 ^ candies[i2];
					s2dec += (unsigned long long) candies[i2];
				}

				if ((s1 == s2) && (s1 != 0) && (s2 != 0))
				{
					if (s1dec > maxSum)
						maxSum = s1dec;

					if (s2dec > maxSum)
						maxSum = s2dec;
				}
			}

			if (maxSum == 0)
			{
				printf("Case #%d: NO\n", caseId);
			}
			else 
			{
				printf("Case #%d: %llu\n", caseId, maxSum);
			}
		}

		delete [] candies;
	}

	return 0;
}