#include<stdio.h>
#include<cstring>
#define MAX 1000
int main()
{
	int StartPoint[MAX];
	int EndPoint[MAX];
	FILE* input = fopen("A-large.in","r");
	FILE* output = fopen("output.txt","w");
	int test;
	fscanf(input,"%d",&test);
	for(int i = 1; i <= test;i++)
	{
		int answer = 0;
		memset(StartPoint,-1,sizeof(StartPoint));
		memset(EndPoint,-1,sizeof(EndPoint));
		int n;
		fscanf(input,"%d",&n);
		for(int j = 0; j< n;j++)
			fscanf(input,"%d %d",&StartPoint[j],&EndPoint[j]);
		for(int j = 0; j < n;j++)
		{
			for(int k = j+1;k < n;k++)
			{
				if(StartPoint[j] < StartPoint[k] && EndPoint[j] > EndPoint[k])
					answer++;
				else if(StartPoint[j] > StartPoint[k] && EndPoint[j] < EndPoint[k])
					answer++;
			}
		}
		fprintf(output,"Case #%d: %d\n",i,answer);
	}
	fclose(input);
	fclose(output);
	return 0;
}