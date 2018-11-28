#include <stdio.h>
#include <stdlib.h>

void write_out(int num, char *status)
{
	FILE *file = fopen("A-large.out", "a");
	fprintf(file, "Case #%d: %s\n", num, status);
	fclose(file);
}

static char status[4][256] = {"X won","O won", "Draw", "Game has not completed"};

int main()
{
	char buffer[4][5] = {0};
	int case_num, i;
	FILE *file;

	file = fopen("A-large.in", "r");
	fscanf(file, "%d", &case_num);
	for(i=0;i<case_num;i++)
	{
		int sum[10] = {0};
		int not_over = 0;
		int j;

		for(j=0;j<4;j++)
		{
			fscanf(file, "%s", buffer[j]);
			int k;
			for(k=0;k<4;k++)
			{
				char ch = buffer[j][k];
				int value = 0;
				switch(ch)
				{
				case 'X':
					value = 100;
					break;
				case 'O':
					value = 10;
					break;
				case 'T':
					value = 1;
					break;
				case '.':
					not_over = 1;
					break;
				}
				sum[j]+=value;
				sum[4+k]+=value;
				if(j==k)
					sum[8]+=value;
				else if((j+k)==3)
					sum[9]+=value;
			}
		}
		int m, is_won = 0;
		for(m=0;m<10;m++)
		{
			switch(sum[m])
			{
				case 301:
				case 400:
					write_out(i+1, status[0]);
					//printf("Case# %d: %s\n", i+1, status[0]);
					is_won = 1;
					goto TAG;
					break;
				case 31:
				case 40:
					write_out(i+1, status[1]);
					//printf("Case# %d: %s\n", i+1, status[1]);
					is_won = 1;
					goto TAG;
					break;
			}
		}
	TAG:
		if(is_won)
			continue;
		if(not_over)
			write_out(i+1, status[3]);
			//printf("Case# %d: %s\n", i+1, status[3]);
		else
			write_out(i+1, status[2]);
			//printf("Case# %d: %s\n", i+1, status[2]);
	}
	fclose(file);

	return 0;
}