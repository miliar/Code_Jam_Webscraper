#include <cstdio>
#include <cmath>
#include <stdlib.h>

int sgn(int n)
{
	if (n > 0) 
	{
		return 1;
	} 
	else if (n < 0)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	int n;
	FILE* fp = fopen("A-large.in", "r");
	FILE* fout = fopen("A-large.out", "w");
	fscanf(fp,"%d", &n);
	for(int i = 0; i < n; ++i)
	{
		int op_count = 0;
		char color[255];
		int button[255];
		fscanf(fp,"%d", &op_count);
		for(int j = 0; j < op_count; ++j)
		{
			fscanf(fp," %c %d", &color[j], &button[j]);
		}
		//////////////orange(0) blue(1)
		int prev[2] = {   1,      1};
		int step = 0;
		for(int j = 0; j < op_count; ++j)
		{
			int k = j + 1;

			switch(color[j])
			{
			case 'O':
				step += abs(button[j]-prev[0]);
				while(k < op_count && color[k] != 'B') ++k;
				if (k < op_count && color[k] == 'B')
				{
					if (abs(button[j]-prev[0])+1 < abs(button[k]-prev[1]))
					{
						prev[1] += ((abs(button[j]-prev[0])+1) * sgn(button[k]-prev[1]));
					}
					else
					{
						prev[1] = button[k];
					}
				}
				prev[0] = button[j];				
				++step;
				break;
			case 'B':
				step += abs(button[j]-prev[1]);
				while(k < op_count && color[k] != 'O') ++k;
				if (k < op_count && color[k] == 'O')
				{
					if (abs(button[j]-prev[1])+1 < abs(button[k]-prev[0]))
					{
						prev[0] += ((abs(button[j]-prev[1])+1) * sgn(button[k]-prev[0]));
					}
					else
					{
						prev[0] = button[k];
					}
				}
				prev[1] = button[j];				
				++step;
				break;
			default:
				break;
			}
		}

		fprintf(fout,"Case #%d: %d\n", i+1, step);
	}
	return 0;
}
		