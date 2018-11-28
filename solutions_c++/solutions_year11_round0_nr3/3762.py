#include <stdio.h>

void main()
{
	FILE * input = fopen("input","r");
	FILE * output = fopen("output","w");
	unsigned int *a;
	unsigned int n;
	fscanf(input,"%d", &n);
	for(int i=0;i<n;i++)
	{
		unsigned int k;
		fscanf(input, "%d",&k);
		a = new unsigned int[k];
		for(int j=0;j<k;j++)
		{
			fscanf(input, "%d",&a[j]);
		}
		unsigned long sum;
		unsigned long pseudoSum = 0;
		//select minimal
		int min=a[0];
		for(int j=0;j<k;j++)
		{
			if(min>a[j])
			{
				min=a[j];
			}
		}
		sum=0;
		pseudoSum = 0;
		for(int j=0;j<k;j++)
		{
			pseudoSum^=a[j];
			sum+=a[j];
		}
		if(pseudoSum==0)
			fprintf(output,"Case #%d: %d\n",i+1,sum-min);
		else
			fprintf(output,"Case #%d: NO\n",i+1);
		delete[] a;
	}
	fclose(output);
	fclose(input);
}