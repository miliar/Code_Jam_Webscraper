#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <bitset>
using namespace std;

int T;
int N;
int weight[1001];

void test()
{
	printf("%d %d",(5^6)^7,5^(6^7));
	int temp;
	scanf("%d",&temp);
}
int main()
{

	FILE *in = fopen("f:/problem3a.in","r");
	FILE *out = fopen("f:/solution3a.out","w");
	fscanf(in,"%d",&T);
	for(int i = 1;i <= T ; i++)
	{
		fscanf(in,"%d",&N);
		int tempResult  = 0;//所有元素异或
		int SumTotal = 0;
		int tempPart1 = 0;
		int SumPart1 = 0;
		int tempPart2 = 0;
		int SumPart2 = 0;
		for(int j = 1;j <= N;j ++)
		{
			fscanf(in,"%d",&(weight[j]));
			tempResult ^= weight[j];
			SumTotal += weight[j];
		}
		int isExists = 0;
		int LargeBenefit = 0;
		//如果只有1个,那么直接输出NO
		int FinalResult = 0;
		for(int j = 1;j < pow(2.0,N)-1-0.1;j ++)
		{
			bitset<1000> testBit(j);
			SumPart1 = 0;
			tempPart1 = 0;

			for(int k = 0;k < N ;k ++)
			{
				if(testBit.test(k))
				{
					tempPart1^=weight[k+1];
					SumPart1 += weight[k+1];
				}
			}
			if((tempResult^tempPart1) == tempPart1)//两者异或值相同
			{
				isExists = 1;
				if(SumTotal - SumPart1 > SumPart1)
				{
					FinalResult = (SumTotal-SumPart1>FinalResult)?(SumTotal-SumPart1):FinalResult;
				}
				else
				{
					FinalResult = (SumPart1>FinalResult)?SumPart1:FinalResult;
				}
			}
		}
		if(isExists)
		{
			fprintf(out,"Case #%d: %d\n",i,FinalResult);
		}
		else
		{
			fprintf(out,"Case #%d: NO\n",i);
		}



	}


}