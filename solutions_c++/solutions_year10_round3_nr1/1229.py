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

#include "BigUnsigned.hh"
#include "BigIntegerUtils.hh"
#include "BigIntegerAlgorithms.hh"

typedef __int64				Int64;
typedef unsigned __int64	uInt64;
typedef unsigned int		uInt32;

struct wire
{
	uInt32 x, y;
};

class WireX
{
public:
	bool operator()(const wire& a, const wire& b)
	{
		return a.x < b.x;
	}
};

class WireY
{
public:
	bool operator()(const wire& a, const wire& b)
	{
		return a.y < b.y;
	}
};

typedef vector<wire> warray;

int _tmain(int argc, _TCHAR* argv[])
{
	//fstream fIn("d:\\Projects\\code jam\\2010\\qualification\\B-large.in");
	//fstream fOut;
	//fOut.open("d:\\Projects\\code jam\\2010\\qualification\\B-large.res", ios_base::out);
	FILE * fIn = NULL;
	fopen_s(&fIn, "d:\\Projects\\code jam\\2010\\1\\A-large.in", "r");
	FILE * fOut = NULL;
	fopen_s(&fOut, "d:\\Projects\\code jam\\2010\\1\\A-large.res", "w+");

	int testNumber = 0;
	fscanf_s(fIn, "%d", &testNumber);

	//fIn >> testNumber;

	for (int i = 0; i < testNumber; ++i)
	{
		cout << "case "<< i+1 << "\n";
		cout.flush();
		
		uInt32 wiresCnt = 0;
		//fIn >> numbers;
		fscanf_s(fIn, "%u", &wiresCnt);

		warray wires;
		for (int j = 0; j < wiresCnt; ++j)
		{
			wire wire_;
			fscanf_s(fIn, "%u", &wire_.x);
			fscanf_s(fIn, "%u", &wire_.y);
			wires.push_back(wire_);
		}

		warray wires_y_sort = wires;

		sort(wires.begin(), wires.end(), WireX());
		//sort(wires_y_sort.begin(), wires_y_sort.end(), WireY());

		uInt32 cnt = 0;

		warray::const_iterator it = wires.begin();
		warray::const_iterator it_end = wires.end();
		size_t size = wires.size();
		for (; it != it_end; ++it)
		{
			warray::const_iterator it2 = it + 1;
			warray::const_iterator it2_end = wires.end();
			for (; it2 != it2_end; ++it2)
			{
				if (it->y > it2->y)
					cnt++;
			}
		}

		//fOut << "Case #" << i+1 <<": "<< res << "\n";
		fprintf(fOut, "Case #%d: %u\n", i + 1, cnt);
	}

	return 0;
}
