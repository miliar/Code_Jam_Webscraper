

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int groups[1000], n=2, k=4, r=3, profit=0, t=0, gr_s=0, gr_e=0;

	FILE *fl = fopen("A-small-in.in", "r");
	fscanf(fl, "%d", &t);
	
	FILE *fl2 = fopen("A-small.out", "w");

	for (int p=0; p < t; p++)
	{
		profit=0;
		gr_s = gr_e = 0;
	
		fscanf(fl, "%d", &r);
		fscanf(fl, "%d", &k);
		fscanf(fl, "%d", &n);


		for (int u=0; u < n;u++)
			fscanf(fl, "%d", &groups[u]);

		for (int i=0; i < r; i++)			//rounds
		{
			gr_e = gr_s;
			int cur_set_cnt = 0;
			while ((cur_set_cnt + groups[gr_e]) <= k)
			{
				cur_set_cnt += groups[gr_e];
				gr_e = (gr_e + 1) % n;

				if (gr_e == gr_s)
					break;
			}


			profit += cur_set_cnt;
			
			gr_s = gr_e;
		}
			
		
//		printf("OUT: %d\n", profit);
		
		fprintf(fl2, "Case #%d: %d\n", p+1, profit);
	}


	return 0;
}
