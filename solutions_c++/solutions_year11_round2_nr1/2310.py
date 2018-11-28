#include<iostream>
#include<fstream>
#include<cstring>
#include<stdio.h>

using namespace std;
int main()
{
	ifstream fin("A-large.in");
	FILE *fout = fopen("A-large-out.in","w");
	char arr[100][100];
	int N;
	int testcases;
	int i,j,k,z,win;
	double temp, count, count2;
	
	double WP[100];
	double OWP[100];
	double OOWP[100];
	
	fin>>testcases;
	for(z=1; z<=testcases; z++)
	{
		fin>>N;
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
			{
				fin>>arr[i][j];
			}
		}
		for(i=0;i<N;i++)
		{
			win = 0;
			count = 0;
			for(j=0;j<N;j++)
			{
				if(arr[i][j]=='.')
					continue;
					
				count++;
				win+=arr[i][j]-48;
			}
			WP[i] = win/count;
		}
		for(j=0;j<N;j++)
		{
			count2=0;
			temp = 0;
			for(i=0;i<N;i++)
			{
				count = 0;
				win = 0;
				for(k=0;k<N;k++)
				{
					if(i==j||arr[j][i]=='.')
						break;
					if(j==k || arr[i][k] == '.')
						continue;
					
					count++;
					win+=arr[i][k]-48;
					
				}
				if(count!=0)
				{
					count2++;
					temp+=win/count;
				}
			}
			OWP[j] = temp/count2;
		}
		
		for(i=0;i<N;i++)
		{
			count=0;
			temp=0;
			for(j=0;j<N;j++)		
			{
				if(arr[i][j]=='.')
					continue;
				count++;
				temp+=OWP[j];
			}
			OOWP[i]=temp/count;
		}
		
		fprintf(fout,"Case #%d:\n", z);
		for(i=0;i<N;i++)
			fprintf(fout,"%3.12lf\n",((0.25*WP[i])+(0.5*OWP[i])+(0.25*OOWP[i])));
	}
}
	
	
