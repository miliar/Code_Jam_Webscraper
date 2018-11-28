#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int c_digit(int i)
{
	int digit=0;
	for(int b=i;b>0;b=b/10) digit++;
	return digit;
}

int main(void)
{
	ifstream file;
	file.open("C-small-attempt0.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;
	int start, end;


	int result=0;
	int loopCache;

	
	for(int t=1; t<= caseNo; t++)
	{
		file >> start;
		file >> end;
		int checkDump=0;
		int digitCache[7]={0};

		for(int number=start; number<=end; number++)
		{
			checkDump=0;
			for(int check=0; check<7; check++) digitCache[check]=0;
			int digit = c_digit(number);
			if(digit != 0)
			{
				loopCache=number;
				for(int loop=0;loop<digit;loop++)
				{
					loopCache=(int)(loopCache/10)+(int)(loopCache%10)*(int)pow((double)10,digit-1);
					if(loopCache > number && loopCache <= end)
					{
						for(int check=0; check<7; check++)
						{
							if(digitCache[check] == loopCache) result--;
						}
						digitCache[checkDump]=loopCache;
						checkDump++;
						result++;

					}
				}
			}
		}
		output << "Case #" << t << ": " << result << endl;
		result=0;
	}
}