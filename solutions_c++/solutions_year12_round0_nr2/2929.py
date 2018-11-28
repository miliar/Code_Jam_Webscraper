#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	FILE *fp, *fpout;
	int t, n, s, p;
	int ti;
	int i, j;
	int x, y;
	char buf[1001];

	fp = fopen(argv[1], "r");
	fpout = fopen("a.out", "wb");

	fgets(buf, 1000, fp);
	t = atoi(buf);

	for(i = 0;i < t;i++)
	{
		x = i + 1;
		y = 0;

		fscanf(fp, "%d %d %d", &n, &s, &p);

		for(j = 0;j < n;j++)
		{
			fscanf(fp, "%d", &ti);
			
			if(p == 0)
			{
				y++;
				continue;
			}
			else if(p == 1)
			{
				if(ti >= 1)
				{
					y++;
					continue;
				}
			}
			else if(ti >= (p-1) + (p-1) + p)
			{
				y++;
				continue;
			}
			else if(s > 0) // try suprise
			{
				if(ti >= (p-2) + (p-2) + p)
				{
					y++;
					s--;
					continue;
				}
				
				// not matched
			}
		}

		fprintf(fpout, "Case #%d: %d\n", x, y);
	}

	
	fclose(fp);
	fclose(fpout);
}
