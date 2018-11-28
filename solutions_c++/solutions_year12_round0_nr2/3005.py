#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int maxSum[101];
int maxi[101][2];
int main()
{
	int cases=0;
	int count =1;
	FILE* input = fopen("abc.in","r");
	FILE* output = fopen("output.txt","w+");
	fscanf(input,"%d",&cases);
	
	while(cases>0)
	{
		int nor=0;
		int sp=0;
		int num =0;
		int sep =0;
		int p =0;
		fscanf(input,"%d %d %d",&num,&sep,&p);
		for(int i=0;i<num;i++)
		{
			fscanf(input,"%d",&maxSum[i]);
			if(maxSum[i]==0)
			{
				maxi[i][0] =0;
				maxi[i][1] =0;
			}
			else if(maxSum[i]==1)
			{
				maxi[i][0] =1;
				maxi[i][1] =0;
			}
			else if(maxSum[i]==2)
			{
				maxi[i][0] =1;
				maxi[i][1] =2;
			}
			else if(maxSum[i]%3==0)
			{
				maxi[i][0]=maxSum[i]/3;
				maxi[i][1]=(maxSum[i]/3) +1;

			}
			else if(maxSum[i]%3==1)
			{
				maxi[i][0]= (maxSum[i]/3) +1;
				maxi[i][1]= -1;
			}
			else if(maxSum[i]%3==2)
			{
				maxi[i][0]= (maxSum[i]/3)+1;
				maxi[i][1]=(maxSum[i]/3) +2;
			}
			
			if(maxi[i][0]>=p && maxi[i][1]>=p)
			{
				nor++;
			}
			else if(maxi[i][0]>=p && maxi[i][1] < p)
			{
				nor++;
			}
			else if(maxi[i][0]< p && maxi[i][1] >= p)
			{
				sp++;
			}
		}
		if(sp>sep){
			sp = sep;
		}
		int ans=nor+sp;
		fprintf(output,"Case #%d: %d\n",count,ans);
		count++;
		cases--;
	}
	fclose(output);
}