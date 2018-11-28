// CropTriangles.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <set>

using namespace std;

struct Test
{
	int n;
	long A;
	long B;
	long C;
	long D;
	long x0;
	long y0;
	long M;
	vector<pair<__int64, __int64> > points;
};

long solve(Test& test)
{
	__int64 X = (__int64)test.x0;
	__int64 Y = (__int64)test.y0;

	test.points.push_back(make_pair(X, Y));

	int i, j, k;

	for (i = 1; i < test.n; i++)
	{
		X = ((__int64)test.A * X + (__int64)test.B) % test.M;
		Y = ((__int64)test.C * Y + (__int64)test.D) % test.M;
		test.points.push_back(make_pair(X, Y));
	}

	long ret = 0;

	for (i = 0; i < test.n; i++)
	{
		for (j = i + 1; j < test.n; j++)
		{
			for (k = j + 1; k < test.n; k++)
			{
				long x1 = test.points[i].first;
				long x2 = test.points[j].first;
				long x3 = test.points[k].first;

				long y1 = test.points[i].second;
				long y2 = test.points[j].second;
				long y3 = test.points[k].second;
/*
				if (((y2-y1) * (x3-x2)) == ((y3-y2) * (x2-x1)))
				{
					continue;
				}
*/
				__int64 x = x1 + x2 + x3;
				__int64 y = y1 + y2 + y3;

				if ((x % 3) == 0 && (y % 3 == 0))
				{
					ret++;
				}
			}
		}
	}

	return ret;
}

int main(int argc, char* argv[])
{
	vector<Test> testCases;

	fstream fs("A-small-attempt1.in", ios::in);

	int N;

	fs >> N;

	int i;

	for (i = 0; i < N; i++)
	{
		Test test;

		fs >> test.n >> test.A >> test.B >> test.C >> test.D >> test.x0 >> test.y0 >> test.M;

		testCases.push_back(test);
	}

	
	fs.close();

	fstream ofs("output.txt", ios::out);

	for (i = 1; i <= N; i++)
	{
		ofs << "Case #" << i << ": " << solve(testCases[i-1]) << endl;
	}

	ofs.close();
	
	return 0;
}
