#include <stdio.h>
#include <stdlib.h>

int main()
{
	int noOfTestCases;
	int noOfPeople;
	int noOfSurprises;
	int minScore;
	int indScore;
	int canSurpriseCounted = 0;
	int surpriseOnly = 0;
	int cannotSurpriseCounted = 0;
	int cannotSurpriseUncounted = 0;
	int total;
	
	scanf("%d", &noOfTestCases);
	
	for(int i=0; i<noOfTestCases; i++)
	{
		canSurpriseCounted = 0;
		surpriseOnly = 0;
		cannotSurpriseCounted = 0;
		cannotSurpriseUncounted = 0;
		
		scanf("%d", &noOfPeople);
		scanf("%d", &noOfSurprises);
		scanf("%d", &minScore);

		for(int j=0; j<noOfPeople; j++)
		{			
			scanf("%d", &total);
			if(total == 0)
				continue;
			indScore = total/3;
			int rem = total % 3;
			if(rem == 0)
			{
				if(indScore >= minScore)
				{					
					if(total == 0 || total == 30)
						cannotSurpriseCounted++;
					else
						canSurpriseCounted++;
					continue;
				}
				if(indScore == (minScore - 1))
				{
					//count++;
					surpriseOnly++;
					continue;
				}				
			}
			if(rem == 1)
			{
				if(indScore >= (minScore-1))
				{
					if(total == 1)
						cannotSurpriseCounted++;
					else
						canSurpriseCounted++;
					continue;
				}
			}
			if(rem == 2)
			{
				if(indScore >= (minScore-1))
				{
					if(total == 29)
						cannotSurpriseCounted++;
					else
						canSurpriseCounted++;
					continue;
				}
				if(indScore == (minScore-2))
				{
					//count++;
					surpriseOnly++;
					continue;
				}
			}
			if(total <= 1 || total >= 29)
				cannotSurpriseUncounted++;
		}

		if(minScore == 0)
		{
			printf("Case #%d: %d\n", i+1, noOfPeople);
			continue;
		}
		int total = cannotSurpriseCounted;
		if(surpriseOnly >= noOfSurprises)
		{
			total += noOfSurprises;
			total += canSurpriseCounted;
			printf("Case #%d: %d\n", i+1, total);
			continue;
		}
		total += canSurpriseCounted;
		total += surpriseOnly;
		printf("Case #%d: %d\n", i+1, total);
			continue;
	}
	return 0;
}