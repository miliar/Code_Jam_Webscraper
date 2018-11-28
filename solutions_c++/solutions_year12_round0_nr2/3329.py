// dance.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

ifstream in("test.txt");
ofstream out("out.txt");

int p;
int s;

int maxMarkSuprising(int total)
{
	int magicNumber = total / 3;
	int m = -1;
	for(int a = max(magicNumber - 2, 0); a <= min(magicNumber + 2, 10); a++)
		for(int b = max(magicNumber - 2, 0); b <= min(magicNumber + 2, 10); b++)
			for(int c = max(magicNumber - 2, 0); c <= min(magicNumber + 2, 10); c++)
				if(a + b + c == total)
					if( ((abs(a-b) == 2) || (abs(a-c) == 2) || (abs(b-c) == 2))
						&& (abs(a-b) < 3) && (abs(a-c) < 3) && (abs(b-c) < 3))
						m = max(m,max(a,max(b,c)));
	return m;
}

int maxMark(int total)
{
	int magicNumber = total / 3;

	int m = -1;

	for(int a = max(magicNumber - 2, 0); a <= min(magicNumber + 2, 10); a++)
		for(int b = max(magicNumber - 2, 0); b <= min(magicNumber + 2, 10); b++)
			for(int c = max(magicNumber - 2, 0); c <= min(magicNumber + 2, 10); c++)
				if(a + b + c == total)
					if( (abs(a-b) <= 1) && (abs(a-c) <= 1) && (abs(b-c) <= 1))
						m = max(m,max(a,max(b,c)));
	return m;
}


void runCase(int test)
{
	int count;
	in >> count;
	in >> s >> p;
	
	int suprisings = 0;
	int result = 0;

	while(count > 0)
	{
		int total;

		in >> total;
		if(maxMark(total) >= p)
			result++;
		else
			if(maxMarkSuprising(total) >= p && suprisings < s)
			{
				suprisings++;
				result++;
			}
		count--;
	}

	out << "Case #" << test << ": " << result << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	in >> T;

	for(int i = 0; i < T; i++)
		runCase( i+1);

	return 0;
}
