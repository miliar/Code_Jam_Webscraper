#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

int main()
{
	set<int> num;
	int A,B;
	int T, r;
	scanf("%d",&T);
	set<int>::iterator it;

	for (int i = 1; i <= T; i++)
	{
		r = 0;
		scanf("%d %d",&A,&B);
		for (int j = A; j <= B; j++)
		{
			num.insert(j);
		}

		for (int j = A; j <= B; j++)
		{
			int k = j;
			it = num.begin();
			it = num.find (k);
			if (it == num.end()) continue;

			num.erase(k);

			if (k/100)
			{
				int u = k%10;
				int t = (k/10)%10;
				int h = k/100;

				int c = 100*t + 10*u + h;
				//printf("Num %d Can %d \n",k,c);
				it = num.begin();
				it = num.find (c);
				if (it != num.end())
				{
					r += 1;
				}

				c = 100*u + 10*h + t;
				//printf("Num %d Can %d \n",k,c);
				it = num.begin();
				it = num.find (c);
				if (it != num.end())
				{
					r += 1;
				}
			}
			else
			{
				int u = k%10;
				int t = k/10;
				int c = 10*u + t;
				it = num.begin();
				it = num.find (c);
				if (it != num.end())
				{
					r += 1;
				}
			}
		}
		printf("Case #%d: %d\n",i,r);
	}
	return 0;
}