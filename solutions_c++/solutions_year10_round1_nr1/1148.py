#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include <stdio.h>
#include <iostream.h>
using namespace std;

#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define D "%d"


void main()
{
	int testNum,N,KN;
	int start[50][50],rotate[50][50];
	FILE *fp = fopen("A-large.in.txt","r");
	FILE *fp2 = fopen("A-large.out.txt","w");

	if(!fp)
	{
		printf("cannot open file\n");
		exit(0);
	}
	fscanf(fp,"%d",&testNum);
	for(int testID=1;testID<=testNum;testID++)
	{
		char tmp;
		int redNum=0,blueNum=0,redFound=0,blueFound=0;
		fscanf(fp,"%d%d%c",&N,&KN,&tmp);
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				fscanf(fp,"%c",&tmp);
				start[i][j] = tmp;
//				printf("%c",tmp);
			}
			fscanf(fp,"%c",&tmp);
//			printf("\n");
		}
		for(i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				rotate[i][j] = start[N-1-j][i];
//				printf("%c",rotate[i][j]);
			}
//			printf("\n");
		}
		for(i=N-1;i>=0;i--)
		{
			for(int j=0;j<N;j++)
			{
				if(rotate[i][j] == '.')
				{
					for(int k=i-1;k>=0;k--)
					{
						if(rotate[k][j] != '.')
						{
							rotate[i][j] = rotate[k][j];
							rotate[k][j] = '.';
							break;
						}
					}
				}
			}
		}
		for(i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(redFound == 0 && rotate[i][j] == 'R')
				{
					redNum =1;
					//find in a row;
					for(int k=j+1;k<N;k++)
					{
						if(rotate[i][k]!= 'R')
						{
							redNum = 1;
							break;
						}
						else
							redNum++;
						if(redNum >=KN)
						{
							redFound = 1;
							break;
						}
					}
					//find in a col
					redNum =1;
					for(k=i+1;k<N;k++)
					{
						if(rotate[k][j]!= 'R')
						{
							redNum = 1;
							break;
						}
						else
							redNum++;
						if(redNum >=KN)
						{
							redFound = 1;
							break;
						}
					}
					//find diagonally
					redNum =1;
					k = i;
						for(int kk=j+1;kk<N;kk++)
						{
							k++;
							if(k>=N)
								break;
							if(rotate[k][kk]!= 'R')
							{
								redNum = 1;
								break;
							}
							else
								redNum++;
							if(redNum >=KN)
							{
								redFound = 1;
								break;
							}
						}
					redNum =1;
					k = i;
						for(kk=j-1;kk>=0;kk--)	
						{
							k++;
							if(k>=N)
								break;
							if(rotate[k][kk]!= 'R')
							{
								redNum = 1;
								break;
							}
							else
								redNum++;
							if(redNum >=KN)
							{
								redFound = 1;
								break;
							}
						}
					
				}
				if(blueFound == 0 && rotate[i][j] == 'B')
				{
					blueNum =1;
					//find in a row;
					for(int k=j+1;k<N;k++)
					{
						if(rotate[i][k]!= 'B')
						{
							blueNum = 1;
							break;
						}
						else
							blueNum++;
						if(blueNum >=KN)
						{
							blueFound = 1;
							break;
						}
					}
					//find in a col
					blueNum =1;
					for(k=i+1;k<N;k++)
					{
						if(rotate[k][j]!= 'B')
						{
							blueNum = 1;
							break;
						}
						else
							blueNum++;
						if(blueNum >=KN)
						{
							blueFound = 1;
							break;
						}
					}
					//find diagonally
					blueNum =1;
				    k = i;
						for(int kk=j+1;kk<N;kk++)
						{
							k++;
							if(k>=N)
								break;
							if(rotate[k][kk]!= 'B')
							{
								blueNum = 1;
								break;
							}
							else
								blueNum++;
							if(blueNum >=KN)
							{
								blueFound = 1;
								break;
							}
						}
					//find diagonally
					blueNum =1;
					k = i;
						for(kk=j-1;kk>=0;kk--)	
						{
							k++;
							if(k>=N)
								break;
							if(rotate[k][kk]!= 'B')
							{
								blueNum = 1;
								break;
							}
							else
								blueNum++;
							if(blueNum >=KN)
							{
								blueFound = 1;
								break;
							}
						}
				}
//				printf("%c",rotate[i][j]);
			}
//				
//			printf("\n");
		}
//		printf("\n");
		if(redFound == 1 && blueFound ==1)
			fprintf(fp2,"Case #%d: Both",testID);
		else if(redFound == 0 && blueFound ==0)
			fprintf(fp2,"Case #%d: Neither",testID);
		else if(redFound == 1)
			fprintf(fp2,"Case #%d: Red",testID);
		else
			fprintf(fp2,"Case #%d: Blue",testID);
		if(testID!=testNum)
			fprintf(fp2,"\n");
	}
	fclose(fp);
	fclose(fp2);
	
}