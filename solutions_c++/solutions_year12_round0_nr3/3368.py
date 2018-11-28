#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	int nCase = 0;
	scanf("%d\n", &nCase);

	vector<int> numlist;
	for (int i=0; i<nCase; i++)
	{
		int count = 0;
		int A, B;
		scanf("%d %d\n", &A, &B);

		for (int j=A; j<=B; j++)
		{
			numlist.clear();
			int totoaldigit = 1;
			while(totoaldigit * 10 <= j)
			{
				totoaldigit *= 10;
			}

			int digit = 10;
			while(j / digit > 0)
			{
				int x = j/digit;
				int y = j - x*digit;
				if (y * digit < digit)
				{
					digit *= 10;
					continue;
				}

				int z = y * (totoaldigit * 10 /digit) + x;			

				if (z > j && z <= B)
				{
					bool isdup = false;
					for (int n=0; n<numlist.size(); n++)
					{						
						if (numlist[n] == z)
						{
							isdup = true;
						}
					}
					if (!isdup)
					{												
						numlist.push_back(z);
						count++;
					}
				}
				digit *= 10;
			}

		}

		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}