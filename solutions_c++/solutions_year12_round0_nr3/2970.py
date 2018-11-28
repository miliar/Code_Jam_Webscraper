#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	FILE *fp, *fpout;
	int t, a, b;
	int x, y;
	int i, j, k;
	int n, m;
	char buf[1001];
	char nbuf[100], mbuf[100];

	fp = fopen(argv[1], "r");
	fpout = fopen("a.out", "wb");

	fgets(buf, 1000, fp);
	t = atoi(buf);

	for(i = 0;i < t;i++)
	{
		x = i + 1;
		y = 0;

		fscanf(fp, "%d %d", &a, &b);

		//printf("A = %d   B = %d\n", a, b);

		for(j = a;j <= b;j++)
		{
			itoa(j, nbuf, 10);
			mbuf[0] = '\0';

			for(k = 1;k < strlen(nbuf);k++)
			{
				// 1234 -> 4123
				// 1234 -> 3412
				// 1234 -> 2341
				strncpy(mbuf, &(nbuf[strlen(nbuf) - k]), k);
				mbuf[k] = '\0';
				strncat(mbuf, nbuf, strlen(nbuf) - k);
				//printf("n = %s  m = %s\n", nbuf, mbuf);

				n = atoi(nbuf);
				m = atoi(mbuf);

				if(a <= n && n < m && m <= b)
				{
					y++;
					//printf("a = %d  n = %d  m = %d  b = %d\n", a, n, m, b);
				}
			}
		}
				
		fprintf(fpout, "Case #%d: %d\n", x, y);
	}

	
	fclose(fp);
	fclose(fpout);
}
