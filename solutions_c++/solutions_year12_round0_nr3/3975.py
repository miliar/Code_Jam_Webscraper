// QC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "string.h"
using namespace std;

#define INFILE "C-large.in"
#define OUTFILE "C-large.out"

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	long numA, numB;
	long result;
	long orig;
	long num;
	long grade;
	int t;
	infile>>t;
	for (int i=0; i<t; i++)
	{
		infile>>numA>>numB;
		result = 0;
		for (int j=numA; j<numB; j++)
		{
			orig = j;
			num = j;
			grade = 1;
			while ((num/10)>=1)
			{
				grade = grade *10;
				num = num/10;
			}
			num = orig;
			do
			{
				int mod = num%10;
				num = mod*grade+(num/10);
				if ((num<=numB)&&(num>orig))
					result++;
			}
			while (num!=orig);
		}
		outfile<<"Case #"<<i+1<<": "<<result<<"\n";
	}

		
	infile.close();	
	outfile.close();

	return 0;
}

