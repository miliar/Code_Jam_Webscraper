#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <math.h>
using namespace std;

#define MaxSpace		5000

unsigned int nTotalTestCase;

char * Judge (long long N, int PD, int PG);
int GCD(int a, int b);

void main(void)
{
	ifstream inFile;
	ofstream outFile;
	char temp[MaxSpace];
	unsigned int spacePos;
	string tmp1, tmp2;

	long long N;
	int  PD, PG;


	inFile.open("A-large.in");
	outFile.open("B-large.out");

	inFile.getline(temp, MaxSpace);
	nTotalTestCase = atoi(temp);


	for (unsigned int i = 0;i < nTotalTestCase; i++)
	{
		inFile.getline(temp, MaxSpace);
		string t(temp);

		spacePos = t.find(' ');
		tmp1 = t.substr(0, spacePos);
		tmp2 = t.substr(spacePos+1, t.length() - 1);
		N = (long long)atoi(tmp1.c_str());

		spacePos = tmp2.find(' ');
		tmp1 = tmp2.substr(0, spacePos);
		tmp2 = tmp2.substr(spacePos+1, t.length() - 1);
		PD = atoi(tmp1.c_str());
		PG = atoi(tmp2.c_str());


		//Display
		tmp1 ="Case #";
		_itoa_s(i+1, temp, 10);
		tmp1 += temp;
		tmp1 += ": ";
		tmp1 += Judge(N, PD, PG);
		tmp1+= "\n";
		outFile.write(tmp1.c_str(), tmp1.length());

	}
	inFile.close();
	outFile.close();
}

char * Judge (long long N, int PD, int PG)
{
	if ((PG == 100)&&(PD<100))
	{
		return "Broken";
	}
	if ((PG == 0)&&(PD>0))
	{
		return "Broken";
	}
	if ((PG == 0)&&(PD==0))
	{
		return "Possible";
	}

	int gcd = GCD(PD, 100);
	int maxGames = (long long)100/gcd;

	if (maxGames>N)
	{
		return "Broken";
	}
	else
		return "Possible";


}

int GCD(int a, int b)
{
	while( 1 )
	{
		a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

		if( b == 0 )
			return a;
	}
}