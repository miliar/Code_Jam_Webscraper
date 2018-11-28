#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX_R 505
#define MAX_C 505

using namespace std;

int t,r,c,i,j,k;
int iii;
int answer;
double d,cx,cy;
pair<double,double> sum1[MAX_R][MAX_C],tmp1[MAX_R][MAX_C],sumtmp2;
double sum2[MAX_R][MAX_C],tmp2[MAX_R][MAX_C],sumtmp1;
char in[MAX_R][MAX_C];

int main()
{
	FILE *fin=fopen("B-large.in","r");
	FILE *fout=fopen("B-large.out","w");
	fscanf(fin,"%d",&t);
	for(iii=0;iii<t;iii++)
	{
		fscanf(fin,"%d %d %lf",&r,&c,&d);
		answer=1;
		for(i=0;i<r;i++)
		{
			fscanf(fin,"%s",in[i+1]+1);
		}
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
				sum1[i][j].first=0;
				sum1[i][j].second=0;
				sum2[i][j]=0;
			}
		}
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
				sum1[i][j].first=(d+in[i][j]-'9')*(i);
				sum1[i][j].second=(d+in[i][j]-'9')*(j);
				tmp1[i][j]=sum1[i][j];
				sum2[i][j]=(d+in[i][j]-'9');
				tmp2[i][j]=sum2[i][j];
			}
		}
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
				sum1[i][j].first+=(sum1[i-1][j].first+sum1[i][j-1].first-sum1[i-1][j-1].first);
				sum1[i][j].second+=(sum1[i-1][j].second+sum1[i][j-1].second-sum1[i-1][j-1].second);
				sum2[i][j]+=(sum2[i-1][j]+sum2[i][j-1]-sum2[i-1][j-1]);
			}
		}
		answer=-1;
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
				for(k=2;k+i<=r&&k+j<=c;k++)
				{
					cx=(i+i+k)/2.0;
					cy=(j+j+k)/2.0;
					sumtmp1=(sum2[i+k][j+k]-sum2[i-1][j+k]-sum2[i+k][j-1]+sum2[i-1][j-1]
							 -tmp2[i][j]-tmp2[i+k][j]-tmp2[i][j+k]-tmp2[i+k][j+k]);
					sumtmp2.first=(sum1[i+k][j+k].first-sum1[i-1][j+k].first-sum1[i+k][j-1].first+sum1[i-1][j-1].first
								   -tmp1[i][j].first-tmp1[i+k][j].first-tmp1[i][j+k].first-tmp1[i+k][j+k].first);
					sumtmp2.second=(sum1[i+k][j+k].second-sum1[i-1][j+k].second-sum1[i+k][j-1].second+sum1[i-1][j-1].second
								   -tmp1[i][j].second-tmp1[i+k][j].second-tmp1[i][j+k].second-tmp1[i+k][j+k].second);
					if(cx*(sumtmp1)==sumtmp2.first&&cy*sumtmp1==sumtmp2.second&&k>answer)
					{
						answer=k;
					}
				}
			}
		}
		fprintf(fout,"Case #%d: ",iii+1);
		if(answer!=-1)
		{
			fprintf(fout,"%d\n",answer+1);
		}
		else
		{
			fprintf(fout,"IMPOSSIBLE\n");
		}
	}
	return 0;
}