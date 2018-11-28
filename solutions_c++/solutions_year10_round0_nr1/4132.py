#include "stdafx.h"
#include <stdio.h>
#include <vector>
using std::vector;

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <string>
using std::string;

#include <algorithm>
#include <numeric>
#include <fstream>
#include <cmath>
using namespace std;

typedef __int64				Int64;
typedef unsigned __int64	uInt64;
typedef unsigned int		uInt32;



int _tmain(int argc, _TCHAR* argv[])
{
	fstream fIn("d:\\Projects\\code jam\\2010\\qualification\\a-large.in");
	fstream fOut;
	fOut.open("d:\\Projects\\code jam\\2010\\qualification\\a-large.res", ios_base::out);

	int testNumber = 0;
	fIn >> testNumber;

	for (int i = 0; i < testNumber; ++i)
	{
		uInt32 n = 0, k = 0;
		bool bRes = false;
		fIn >> n >> k;

		uInt32 pow2 = (1 << n); 
		bRes = k % pow2 == (pow2 - 1);

		//char buff [5];
		//sprintf(buff, "%04d", res);
		fOut << "Case #" << i+1 <<": "<< (bRes ? "ON" : "OFF") << "\n";
	}

	return 0;
}
