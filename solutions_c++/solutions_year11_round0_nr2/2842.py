#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

int T;
int C;
int D;
int N;

int Matrix[9][9];//QWERASDF
int Delete[9][9];
char inputString[102];

int switchChar(char c)
{
	switch(c)
	{
	case'Q':
		return 1;break;
	case'W':
		return 2;break;
	case'E':
		return 3;break;
	case'R':
		return 4;break;
	case'A':
		return 5;break;
	case'S':
		return 6;break;
	case'D':
		return 7;break;
	case'F':
		return 8;break;
	default:
		return 0;break;
	}
}

void clearMatrix()
{
	for(int i= 0; i <= 8;i ++)
	{
		for(int j = 0;j <=8 ; j++)
		{
			Matrix[i][j] = 0;
			Delete[i][j] = 0;
		}
	}
}

int main()
{
	FILE *in = fopen("f:/problem2b.in","r");
	FILE *out = fopen("f:/solution2b.out","w");
	fscanf(in,"%d",&T);
	for(int i = 1;i <= T ; i++)
	{
		clearMatrix();
		fscanf(in,"%d",&C);
		if(C > 0)
		{
			char tempChar1;
			char tempChar2;
			char tempChar3;
			for(int j  = 1;j <= C;j ++)
			{
				fscanf(in," %c%c%c",&tempChar1,&tempChar2,&tempChar3);
				int tempInt1 = switchChar(tempChar1);
				int tempInt2 = switchChar(tempChar2);
				Matrix[tempInt1][tempInt2] = tempChar3;
				Matrix[tempInt2][tempInt1] = tempChar3;
			}
		}
		fscanf(in,"%d",&D);
		if(D > 0)
		{
			char tempChar1;
			char tempChar2;
			for(int j  = 1;j <= D;j ++)
			{
				fscanf(in," %c%c",&tempChar1,&tempChar2);
				int tempInt1 = switchChar(tempChar1);
				int tempInt2 = switchChar(tempChar2);
				Delete[tempInt1][tempInt2] = 1;
				Delete[tempInt2][tempInt1] = 1;
			}
		}
		fscanf(in,"%d ",&N);
		
		for(int j = 0 ;j < N;j ++)
		{
			fscanf(in,"%c",&(inputString[j]));
		}
		inputString[N] = 0;
		char resultString[102] = "";
		int resultLength = 0;
		for(int j = 0;j < N ;j ++)
		{
			resultString[resultLength] = inputString[j];
			if(resultLength  == 0)
			{
				resultLength ++;
				continue;
			}
			else
			{
				int tempInt1 = switchChar(resultString[resultLength]);
				int tempInt2 = switchChar(resultString[resultLength-1]);
				if(Matrix[tempInt1][tempInt2] == 0)
				{
					for(int k = 0; k < resultLength; k ++)
					{
						int tempInt3 = switchChar(resultString[k]);
						if(Delete[tempInt1][tempInt3] == 1)
						{
							resultLength = -1;
							break;
						}
					}
					resultLength ++;
				}
				else
				{
					resultLength --;
					resultString[resultLength] = Matrix[tempInt1][tempInt2];
					resultLength ++;
				}
				
			}
		}
		resultString[resultLength] = 0;
		fprintf(out,"Case #%d: [",i);
		for(int j = 0;j < resultLength;j ++)
		{
			if(j != resultLength -1)
			{
				fprintf(out,"%c, ",resultString[j]);
			}
			else
			{
				fprintf(out,"%c]\n",resultString[j]);
			}
		}
		if(resultLength == 0)
			fprintf(out,"]\n");
	}


}