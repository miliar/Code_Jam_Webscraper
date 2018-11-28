#include<string>
#include<iostream>
#include<fstream>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("B-large.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;
	int googlerNo, noSuprise, bestResult;
	int scores[100];

	int tmp;
	int result=0;
	for(int t=1; t<= caseNo; t++)
	{
		file >> googlerNo;
		file >> noSuprise;
		file >> bestResult;

		for(int number=1;number <= googlerNo; number++)
		{
			file >> scores[number-1];
		}

		for(int m=0;m<googlerNo-1;m++)
		{
			for(int n=0;n<googlerNo-1-m;n++)
			{
				if(scores[n] <= scores[n+1])
				{
					tmp=scores[n+1];
					scores[n+1]=scores[n];
					scores[n]=tmp;
				}
			}
		}

		for(int number=1;number <= googlerNo; number++)
		{
			if(scores[number-1] >= bestResult*3-2 && scores[number-1] >= bestResult) result++;
			else if(scores[number-1] >= bestResult*3-4 && scores[number-1] >= bestResult && noSuprise>0)
			{
				result++;
				--noSuprise;
			}
		}

		output << "Case #" << t << ": " << result << endl;

		result=0;
	}
	
	return 0;
}