#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int T,N;
int WP[500][2];
double OWP[500];
double OOWP[500];

char vs[200][200];

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fscanf(fin, "%d", &N);

		for(int i = 0; i < N; i++)
			fscanf(fin,"%s", vs[i]);

		for(int i = 0; i < N; i++)
		{
			WP[i][0]=WP[i][1]=0;
			for(int j = 0; j < N; j++)
			{
				if(vs[i][j] == '1') 
				{
					WP[i][0]++;
					WP[i][1]++;
				}
				else if(vs[i][j] == '0') 
				{
					WP[i][1]++;
				}
			}
		}

		for(int i = 0; i < N; i++)
		{
			int count = 0;
			double sum = 0.0;
			for(int j = 0; j < N; j++)
			{
				if(vs[i][j] == '1') 
				{
					count++;
					sum+=((double)(WP[j][0]-0))/(WP[j][1]-1);
				}
				else if(vs[i][j] == '0') 
				{
					count++;
					sum+=((double)(WP[j][0]-1))/(WP[j][1]-1);
				}
			}
			OWP[i] = sum / count;
		}

		for(int i = 0; i < N; i++)
		{
			int count = 0;
			double sum = 0.0;
			for(int j = 0; j < N; j++)
			{
				if(vs[i][j] == '1' || vs[i][j] == '0') 
				{
					count++;
					sum+=OWP[j];
				}
			}
			OOWP[i] = sum / count;
		}

		fprintf(fout,"Case #%d:\n", aaa);

		for(int i = 0; i < N; i++)
		{
			fprintf(fout,"%.9f\n",((double)WP[i][0])/WP[i][1] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25);
		}
	}

	return 0;
}
