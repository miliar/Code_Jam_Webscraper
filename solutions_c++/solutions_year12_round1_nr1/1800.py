#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int T, A, B;

	int i, j, k, l;
	float p;

	char buf[1001];
	float pi[99999];
	float keys[100001];
	float y;

	FILE *fp, *fpout;



	fp = fopen(argv[1], "r");
	fpout = fopen("a.out", "wb");

	fgets(buf, 1000, fp);
	T = atoi(buf);

	for(i = 0; i < T;i++)
	{
		fscanf(fp, "%d %d", &A, &B);	
		
		// init keystrokes
		memset(keys, 0, 100001);

		// input pi
		memset(pi, 0, 99999);

		for(j = 0;j < A;j++)
		{
			fscanf(fp, "%f", &(pi[j]));
		}

		// backspace j-times
		for(j = 0;j <= A;j++)
		{
			p = 1.0;
			for(k = 0;k < (A - j);k++)
			{
				p *= pi[k];
			}
			
			keys[j] += (p * ((j + j) + (B - A) + 1)) + ((1.0 - p) * ((j + j) + (B - A) + 1 + (B + 1)));
		}

		// enter right away
		keys[j] = (float)(1 + B + 1);

		
		y = keys[0];
		for(j = 1;j < A + 2;j++)
		{
			if(keys[j] < y) y = keys[j];
		}

		fprintf(fpout, "Case #%d: %.6f\n", i + 1, y);

	}
	
	fclose(fp);
	fclose(fpout);
}
	