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

int TestWordForPattern(const string& s, const vector<string>& patt)
{
	int i = 0;
	for (; i < s.length();)
	{
		if (string::npos == patt[i].find(s[i]))
			break;
		++i;
	}

	return i == s.length();
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream fIn("d:\\Projects\\code jam\\2009\\A-large.in");
	fstream fOut;
	fOut.open("d:\\Projects\\code jam\\2009\\A-large.res", ios_base::out);

	int L, D, N;
	fIn >> L;
	fIn >> D;
	fIn >> N;

	vector<string> stroki;
	for (int i = 0; i < D; ++i)
	{
		string s;
		fIn >> s;
		stroki.push_back(s);
	}

	vector<vector<string>> patterns;
	for (int i = 0; i < N; ++i)
	{
		string s;
		fIn >> s;

		vector<string> patt;
		bool braket = false;
		string buff;

		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '(')
			{
				braket = true;
				buff.clear();
				continue;
			}
			else if (s[i] == ')')
			{
				braket = false;
				patt.push_back(buff);
				continue;
			}

			if (braket)
			{
				buff.push_back(s[i]);
			}
			else
			{
				string temp;
				temp.push_back(s[i]);
				patt.push_back(temp);
			}

		}
				
		patterns.push_back(patt);
	}

	for (int i =0; i < N; ++i)
	{
		vector<string>& patt = patterns[i];
		int s = 0;
		for (int j = 0; j < D; ++j)
		{
			s += TestWordForPattern(stroki[j], patt);
		}

		fOut << "Case #" << i+1 <<": "<< s <<"\n";
	}
	//unsigned int testNumber = 0;
	//fIn >> testNumber;

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
