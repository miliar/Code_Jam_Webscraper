#include<iostream.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void qsort(int a[],int n)
{
	int temp;
	bool switched = true;
	for(int i=0;i<n-1 && switched==true;i++)
	{
		switched = false;
		for(int j=0;j<n-i-1;j++)
		{
			if(a[j]>a[j+1])
			{
				switched = true;
				temp = a[j];
				a[j]= a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

void main()
{

	int *alphabets;
	
	int n;	
		
	int i,j,m;
	
	int P,K,L;

	long frequency;

	FILE *fin, *fout;
	
	char name[100];
	
	int num_cases = 0 ,cases;

	printf("\n Enter the input file name: ");
	scanf("%s",name);
	
	fin = fopen(name,"r");
	
	if(fin)
	{
		fout = fopen("out.txt","w");

		fscanf(fin,"%d",&num_cases);
	
		for(cases=0; cases<num_cases; cases++)
		{
					
			P=0,K=0,L=0;

			frequency = 0;

			fscanf(fin,"%d %d %d",&P, &K, &L);
			
			if(P*K>=L)
			{
				alphabets = (int*)malloc(sizeof(int)*L);

				for(i=0;i<L;i++)
				{
					fscanf(fin, "%d", &alphabets[i]);
					fgetc(fin);
				}
			
				qsort(alphabets,L);
			
				printf("\n");
	
				for(i=0;i<L;i++)
					printf("%d ",alphabets[i]);
				
				j = K, m = 1;

				for(i=L-1;i>=0;i--)
				{
					if(j==0)
					{
						j = K;
						m++;
					}
					j--;
					frequency += alphabets[i]*m;

				}

				if(fout)
				{
					fprintf(fout,"\nCase #%d: %ld ",cases + 1, frequency);
				}
				else
					printf("\nCase #%d: %ld ",cases + 1, frequency);
				
				free(alphabets);
			}
			else
			{
				if(fout)
					fprintf(fout,"\nCase #%d: Impossible ",cases + 1);
				else
					printf("\nCase #%d: Impossible ",cases + 1);
			}
		}
		fclose(fin);
			
		if(fout)
			fclose(fout);
	}
	else
		printf("\n Error Opening file");
}

