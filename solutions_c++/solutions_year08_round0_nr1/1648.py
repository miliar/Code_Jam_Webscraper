#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define line_len 101

char read_line [line_len];

#define s_max 101

char s_flag[s_max];

void zero_s(void) {for (int a=0; a<s_max; a++) s_flag[a]=0;}
int  sum_s (void) {for (int a=0, b=0; a<s_max; a++) b+= s_flag[a]; return b;}


void main(int argc, char **argv)
{
	if (argc<=1) {printf("test\n\n"); return;}

	FILE *input=fopen(argv[1], "rt");

	FILE *output=fopen("output", "wt");

	int N=0, S=0, Q=0;

	fscanf(input, "%d\n", &N);
	printf("%d", N);

	int i, j, k;

	char *s_names=(char *)malloc(line_len*s_max);

	for (i=0;i<N; i++)
	{
		fscanf(input, "%d\n", &S);
		for (j=0;j<S;j++)
			fgets (s_names+j*line_len, line_len-1, input);

		fscanf(input, "%d\n", &Q);

		k=0; j=0;

		zero_s();

		do
		{
			fgets (read_line, line_len-1, input);

			for (j=0;j<S;j++)	if (strcmp(s_names+j*line_len, read_line)==0) break;

			s_flag[j]=1;

			if (sum_s()==S) {k++; zero_s(); s_flag[j]=1;}
		}
		while(--Q>0);

		fprintf(output, "Case #%d: %d\n", i+1, k);
	}


	free(s_names);
	fclose(output);
	fclose(input);

}

