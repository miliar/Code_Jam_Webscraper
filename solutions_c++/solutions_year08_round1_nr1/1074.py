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

	int *v1, *v2;
	int n;	
		
	int i,j;
	
	int min_product = 0;

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
			min_product = 0;
			fscanf(fin,"%d",&n);

			v1 = (int*)malloc(sizeof(int)*n);
			v2 = (int*)malloc(sizeof(int)*n);
			
			for(i=0;i<n;i++)
			{
				fscanf(fin, "%d", &v1[i]);
				fgetc(fin);
			}
			
			for(i=0;i<n;i++)
			{
				fscanf(fin, "%d", &v2[i]);
				fgetc(fin);
			}

			/*for(i=0;i<n;i++)
			{
			//	fscanf(fin, "%d", &v1[i]);
			//	fgetc(fin);
				printf("\n v1: %d v2: %d", v1[i],v2[i]);
			}
			*/
			qsort(v1,n);
			qsort(v2,n);
			/*for(i=0;i<n;i++)
			{
			//	fscanf(fin, "%d", &v1[i]);
			//	fgetc(fin);
				printf("\n v1: %d v2: %d", v1[i],v2[i]);
			}*/
			for(i=0,j=n-1;i<n && j>=0;i++,j--)
				min_product += v1[i]*v2[j];
			//printf("\n Minimum product: %d\n",min_product);

			if(fout)
			{
				fprintf(fout,"\nCase #%d: %d ",cases + 1,min_product);
			}
			else
				printf("\nCase #%d: %d ",cases + 1, min_product);

			free(v1);
			free(v2);
		}
		fclose(fin);
		if(fout)
			fclose(fout);
	}
	else
		printf("\n Error Opening file");
}

