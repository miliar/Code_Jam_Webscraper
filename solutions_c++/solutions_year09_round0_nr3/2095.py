#include "stdafx.h"
#include <stdio.h>
#include <vector>
using std::vector;

#include <string>
using std::string;

#include <algorithm>
#include <numeric>
#include <fstream>
#include <cmath>
using namespace std;

const string t("welcome to code jam");

int FindSubString(const string& a, const string& b, int posa, int posb)
{
	size_t i = posa;

	if (posb == b.length() - 1)
	{
		size_t i = posa;
		size_t count = 0;
		while(i != string::npos)
		{
			size_t pos = a.find(b[posb], i);
			if (pos == string::npos)
				break;

			i = pos + 1;
			count++;
		}
		return count;
	}


	size_t count = 0;

	while(i < a.length())
	{
		size_t pos = a.find(b[posb], i);
		if (pos == string::npos)
			break;
	
		size_t subCount = FindSubString(a, b, pos + 1, posb+1);
		if (subCount == 0)
			break;

		count += subCount % 1000;

		i = pos + 1;
	}

	return count;
	
}

size_t calc(const string& s)
{
	size_t n = 0;

	return FindSubString(s, t, 0, 0);

	return n;
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream fIn("d:\\Projects\\code jam\\2009\\C-small-attempt0.in");
	fstream fOut;
	fOut.open("d:\\Projects\\code jam\\2009\\C-small-attempt0.res", ios_base::out);

	int testNumber = 0;
	fIn >> testNumber;

	for (int i = 0; i < testNumber; ++i)
	{
		string s;
		while(s.length() == 0)
		{
			char temp [1000];
			fIn.getline(temp, 900);
			s = temp;
		}
		

		int res = calc(s);
		
		char buff [5];
		sprintf(buff, "%04d", res);
		fOut << "Case #" << i+1 <<": "<<buff << "\n";
	}

	//double test = 1438010552.3278773255045661463992;


	//double s = log10(3.0 + sqrt(5.0));
	//for(unsigned int i = 1; i <= testNumber; ++i)
	//{
	//	__int64 n;
	//	fIn >> n;

	//	double p = s; 
	//	p *= n;

	//	unsigned int digits = floor(p)*3;
	//	//double p = fmod(q, 3.0);
	//	//p = pow(10.0, p);
	//	//p = floor(p);
	//	p = pow(10.0, fmod(p, 3.0));

	//	for (unsigned int j =0; j < digits; ++j)
	//	{
	//		p*=10;
	//	}

	//	fOut << "Case #" << i <<": ";
	//	fOut << int(floor(fmod(p,1000)/100.0));
	//	fOut << int(floor(fmod(p,100)/10.0));
	//	fOut << int(floor(fmod(p,10)));
	//	fOut << "\n";

	//}


	return 0;
}
