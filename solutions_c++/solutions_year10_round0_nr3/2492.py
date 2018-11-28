#include "stdio.h"
#include "stdlib.h" 

int main()
{
	FILE* f;
	f=fopen("C-small-attempt1 (1).in","r");
	//f=fopen("A-large-practice.in","r");
	if(f==NULL)
	{
		printf("file read error£¡");
		exit(1); 
	}

	FILE *w;
	w=fopen("C-small-attempt1 (1).out","w");
	//w=fopen("A-large-practice.out","w");
	if (w==NULL)
	{
		printf("file write error£¡");
		exit(1); 
	}
	int count=0;
	int count_p=0;
	int r,k,n;
	int mem[1002];
	int point=0;
	fscanf(f,"%d",&count);

	for (int i=0;i<count;i++)
	{
		fscanf(f,"%d",&r);
		fscanf(f,"%d",&k);
		fscanf(f,"%d",&n);
		point=0;
		int point_start=0;
		int sum=0;
		int sum_temp=0;
		int profit=0;
		for (int i=0;i<n;i++)
		{
			fscanf(f,"%d",&mem[i]);
			
		//	printf("%d\n",mem[i]);
		}
		for (int i=0;i<r;i++)
		{
			sum=0;
			sum_temp=0;
			point_start=point;
			while (sum_temp<=k)
			{
				
				sum_temp=sum_temp+mem[point];
				if(sum_temp<=k)
				{
					sum=sum+mem[point];
					profit=profit+mem[point];
					point++;
				}
				if (point>=n)
				{
					point=point%n;
					if (point==point_start)
					{
						break;
					}
				}			
			}
		}

		fprintf(w,"Case #%d: ",i+1);
		fprintf(w,"%d",profit);
		fprintf(w,"\n");
	}
	fclose(f);
	fclose(w);

}
