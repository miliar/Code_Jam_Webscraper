#include <stdio.h>
#include <stdlib.h>
main ()
{
	FILE *input = fopen("input.txt", "r");
	FILE *output = fopen("output.txt", "w+");
	int n, k, m = 1;
	while(fscanf(input,"%d %d\n", &n, &k) == 2)
	{
		bool table[n];
		for(int n_c  = 0; n_c < n; n_c++)
			table[n_c ] = false;
		
		for(int  k_c = 0; k_c < k; k_c++)
		{
			for(int n_c  = 0; n_c < n; n_c++)
			{
				if(table[n_c] == false)
				{
					table[n_c] = (table[n_c]+1)%2;
					break;
				}
				else
				{
					table[n_c] = (table[n_c]+1)%2;
				}
			}
		}
		bool tag = true;
		
		for(int n_c  = 0; n_c < n; n_c++)
		{
			if(table[n_c] == false)
			{
				tag = false;
				break;
			}
		}
		
		if(!tag)
			fprintf(output,"Case #%d: OFF\n", m);
		else
			fprintf(output,"Case #%d: ON\n", m);
		m++;
	}
	fclose(output);
	fclose(input);
}