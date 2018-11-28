// MinScalarProduct.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <iostream>
#include <algorithm>

#include <fstream>

using namespace std;

long calc(vector<pair<vector<int>, vector<int> > > vec, int i)
{
	vector<int>& v1 = vec[i].first;
	vector<int>& v2 = vec[i].second;

	sort(v1.begin(), v1.end());

	sort(v2.begin(), v2.end());

	reverse(v2.begin(), v2.end());

	int length = v1.size();

	long ret = 0;

	int j;

	for (j = 0; j < length; ++j)
	{
		ret += v1[j] * v2[j];
	}

	return ret;
}

int main(int argc, char* argv[])
{
	int T;

	vector<pair<vector<int>, vector<int> > > testCases;

	fstream file_op("A-small-attempt0.in",ios::in);

	fstream file_out("result.txt", ios::out);

	file_op >> T;

	int i, j;

	for (i = 0; i < T; i++)
	{
		int L;

		vector<int> v1;
		vector<int> v2;

		file_op >> L;

		for (j = 0; j < L; j++)
		{
			int e;

			file_op >> e;
			v1.push_back(e);
		}

		for (j = 0; j < L; j++)
		{
			int e;

			file_op >> e;
			v2.push_back(e);
		}

		testCases.push_back(make_pair(v1, v2));
	}

	for (i = 0; i < testCases.size(); ++i)
	{
		file_out << "Case #" << i+1 << ": " << calc(testCases, i) << endl;
	}

	return 0;
}
