#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
	int nonsur_max[] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
	int sur_max[] = {0,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,0,0};
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i++)
	{
		int r = 0;
		int N = 0,s,p,slack = 0;
		scanf("%d %d %d",&N,&s,&p);
		int scores[N];

		for (int j = 0; j < N; j++)
		{
			scanf("%d",&scores[j]);
		}

		sort(scores,scores+N);

		for (int j = N - 1; j >= 0; j--)
		{
			int scr = scores[j];
			//printf("\nScore %d",scr);

			if (s > 0)
			{
				if (sur_max[scr] >= p && nonsur_max[scr] < p)
				{
					r += 1;
					s -= 1;
					//printf(" Surprised\n");
				}
				else if (sur_max[scr] >= p && nonsur_max[scr] >= p)
				{
					r += 1;
					slack += 1;
				}
				else if (sur_max[scr] < p && nonsur_max[scr] >= p)
				{
					r += 1;
					//printf(" No surprise\n");
				}
				else if (sur_max[scr] > 0)
				{
					//printf(" Sur %d\n",s);
					s -= 1;
				}
			}
			else
			{
				if (nonsur_max[scr] >= p)
				{
					r += 1;
				}
			}
		}

		printf("Case #%d: %d\n",i,r);
	}
	return 0;
}