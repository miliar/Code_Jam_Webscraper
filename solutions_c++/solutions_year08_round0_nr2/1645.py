#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define nabmax 101

struct pair{
				int arr, dep;
				void ass(int a, int d) {arr=(a>d)?a:d; dep=(a<=d)?a:d; return;}
			};

void main(int argc, char **argv)
{
	if (argc<=1) {printf("test\n\n"); return;}

	FILE *input=fopen(argv[1], "rt");

	FILE *output=fopen("output", "wt");

	int N=0, T=0, NA=0, NB=0;

	int i,j,k,l,m,n;

	fscanf(input, "%d\n", &N);

	pair *A, *B, *Aq, *Bq;

	int max;

	for (i=0; i<N; i++)
	{
		fscanf(input, "%d\n", &T);
		fscanf(input, "%d", &NA);
		fscanf(input, "%d\n", &NB);

		if (NA>0) A=new pair[NA];
		if (NB>0) B=new pair[NB];

		for (j=0; j<NA+NB;j++)
		{
			fscanf(input, "%d",   &k); fgetc(input);
			fscanf(input, "%d",   &l); fgetc(input);
			fscanf(input, "%d",   &m); fgetc(input);
			fscanf(input, "%d\n", &n);

			((j<NA)?(A+j):(B+j-NA))->ass(k*60+l, m*60+n);
		}

		fprintf(output, "Case #%d:", i+1);

		for (j=0; j<=1;j++)
		{
			if (j==0) {Aq=A; Bq=B;} else {Aq=B; Bq=A;}

			max=0;

			for (k=0;k<NA;k++)
			{
				m=0;
				for (l=0;l<NA;l++)	m+=( ((Aq+l)->dep)<= ((Aq+k)->dep) )?1:0;

				for (l=0;l<NB;l++)  m+=(((Bq+l)->arr+T)<=(Aq+k)->dep)?(-1):0;

//				printf("%d %d %d\n",m, ((Aq+k)->dep)/60, ((Aq+k)->dep)%60);
				if (m>max) max=m;
			}

			fprintf(output, " %d", max);

			k=NA; NA=NB; NB=k;
		}
		fprintf(output, "\n");

		if (NA>0) delete [] A;
		if (NB>0) delete [] B;
	}


	fclose(output);
	fclose(input);

}

