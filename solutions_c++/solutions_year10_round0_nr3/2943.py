

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int groups[1000], groups_next[1000], n=1, k=1, r=1, t=0, gr_s=0, gr_e=0;
	unsigned long profit=0, groups_profit[1000];

	FILE *file = fopen("C-small.in", "r");
	fscanf(file, "%d", &t);
	
	FILE *file2 = fopen("C.out", "w");

	for (int p=0; p < t; p++)
	{
		profit=0;
		gr_s = gr_e = 0;
	
		fscanf(file, "%d", &r);
		fscanf(file, "%d", &k);
		fscanf(file, "%d", &n);


		for (int u=0; u < n;u++)
			fscanf(file, "%d", &groups[u]);

		for (int i=0; i < n; i++)			//for each group
		{
			gr_e = gr_s = i;
			unsigned long cur_set_cnt = 0;
			while ((cur_set_cnt + groups[gr_e]) <= k)
			{
				cur_set_cnt += groups[gr_e];
				gr_e = (gr_e + 1) % n;

				if (gr_e == gr_s)
					break;
			}

			groups_profit[i] = cur_set_cnt;
			groups_next[i] = gr_e;
		}
			
		gr_e = gr_s = 0;
		profit = 0;
		for (int q=0; q < r; q++)			//by rounds
		{
			profit += groups_profit[gr_s];
			gr_s = groups_next[gr_s];
		}

		fprintf(file2, "Case #%d: %u\n", p+1, profit);
	}


	return 0;
}
