#include <stdio.h>
#include <string.h>
#include <math.h>
#define MAXSIZE 110
#define C 40
#define D 40
void main (void)
{
	int T, I;
	FILE* out;
	scanf("%d", &T);
	if(!( out=fopen("123.out", "w") ))
	{
		printf("open error\n");
	}
	for(I=1; I<=T; I++)
	{
//in
		int i, j, k, c, d, n;
		char comb[C][5], oppos[D][4], invoke[MAXSIZE];
		scanf("%d ", &c);
		for(i=0; i<c; i++)
		{
			scanf("%s", comb[i]);
		}
		scanf("%d ", &d);
		for(i=0; i<d; i++)
		{
			scanf("%s", oppos[i]);
		}
		scanf("%d ", &n);
		scanf("%s", invoke);

		for(i=1; i<n; i++)
		{
		//combine
			for(j=0; j<c; j++)
			{
				if((comb[j][0]==invoke[i] && comb[j][1]==invoke[i-1]) ||\
					(comb[j][1]==invoke[i] && comb[j][0]==invoke[i-1]))
				{
					invoke[i] = comb[j][2];
					invoke[i-1] = -1;
					break;
				}
			}
			if (j<c) continue;
		//opposed
			for(k=0; k<=i; k++)
			{
				for(j=0; j<d; j++)
				{
					if((oppos[j][0]==invoke[i] && oppos[j][1]==invoke[k]) ||\
						(oppos[j][1]==invoke[i] && oppos[j][0]==invoke[k]))
					{
						for(k=0; k<=i; k++)
						{
							invoke[k] = -1;
						}
						break;
					}

				}
			}
		}
//out
		int flag = 0;
		fprintf(out, "Case #%d: [", I);
		printf("Case #%d: [", I);
		for(i=0; invoke[i]; i++)
		{
				printf(", ");
			if( invoke[i]>0 && flag )
			{
				fprintf(out,", ");
			}
				printf("%c", invoke[i]);
			if(invoke[i]>0)
			{
				flag = 1;
				fprintf(out, "%c", invoke[i]);
			}
		}
		fprintf(out, "]\n");
		printf("]\n\n");
	}
}