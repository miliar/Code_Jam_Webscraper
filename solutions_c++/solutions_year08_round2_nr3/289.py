#include <stdio.h>
#include <string.h>

#define MAX 30

int ab[205][2], ba[205][2];//caile initiala si reverse
char line[105];


int n, na, nb, t, trenuria, trenurib, nv;

int h1, m1, h2, m2;//timp temp

long long T,K;
long long deck[1000000];

long long indice;

FILE *f_in, *f_out;

int print_solutie(int id)
{
	fprintf(f_out,"Case #%d: %d %d\n",id+1,trenuria,trenurib);
	return 0;
}

int rezolva()
{
	f_in = fopen("C-small-attempt0.in","r");
	f_out = fopen("output.txt","w");
	fscanf(f_in,"%lld",&T);

	for(int i=0; i < T; i++)
	{

		memset(deck, -1, sizeof(deck));
		indice = 0;
		
		long long nrcurent = 0;
		fscanf(f_in,"%lld",&K);
		long long indice_local = 0;
		
		int indice_vector = 0;
		
	
		//ii gasesc locul in deck lui nrcurent;
		bool gasit = false;
		
		
		while (!gasit)
		{
			if(indice_local == nrcurent && deck[indice_vector] == -1)
			{
				deck[indice_vector] = nrcurent;
				nrcurent++;
				if(nrcurent == K)
				{
					gasit = true;
				}
				indice_local = -1;
				indice_vector++;
				if(indice_vector == K)
					indice_vector = 0;
				if(deck[indice_vector] == -1)
					indice_local = 0;
			}else
			{
				indice_vector++;
				if(indice_vector == K)
					indice_vector = 0;
				if(deck[indice_vector] == -1)
					indice_local++;
			}

			
		}
		fprintf(f_out,"Case #%d: ",i+1);
		fscanf(f_in,"%lld",&n);
		long long temp;
		for(int i=0; i<n; i++)
		{
			fscanf(f_in,"%lld",&temp);
			fprintf(f_out,"%lld ", deck[temp-1]+1);
		}
		fprintf(f_out,"\n");

		
		//print_solutie(i);
	}
	
	fclose(f_in);
	fclose(f_out);
	return 0;
}
int main()
{
	rezolva();
	printf("aaaa");
}
