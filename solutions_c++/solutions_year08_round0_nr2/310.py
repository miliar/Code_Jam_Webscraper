// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

typedef	long long llong;

pair<int, int> GetTrainCnt(vector<pair<int, int> > & A, vector<pair<int, int> > & B, int T)
{
	enum	{arrA = 0, arrB = 1, depA = 2, depB = 3};
	vector<pair<int, int> >		events;
	int		curA = 0, curB = 0, allA = 0, allB = 0;
	events.reserve(2*(A.size() + B.size()));
	for (size_t i = 0; i < A.size(); ++i)
	{
		events.push_back(make_pair(A[i].first, depA));
		events.push_back(make_pair(A[i].second + T, arrB));
	}
	for (size_t i = 0; i < B.size(); ++i)
	{
		events.push_back(make_pair(B[i].first, depB));
		events.push_back(make_pair(B[i].second + T, arrA));
	}
	sort(events.begin(), events.end());
	for (size_t i = 0; i < events.size(); ++i)
	{
		switch (events[i].second)
		{
		case arrA:
			curA++;
			break;
		case arrB:
			curB++;
			break;
		case depA:
			if (curA > 0)
				curA--;
			else
				allA++;
			break;
		case depB:
			if (curB > 0)
				curB--;
			else
				allB++;
		}
	}
	return make_pair(allA, allB);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("B-large.in");
	ofstream	outfile("B-large.out");

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		string		tmps;
		int			T;
		infile >> T;

		size_t	nA, nB;
		infile >> nA >> nB;  
		vector<pair<int, int> >	A(nA);
		vector<pair<int, int> >	B(nB);

		getline(infile, tmps);
		for (size_t j = 0; j < nA; ++j)
		{
			int DH, DM, AH, AM;
			string		str;
			getline(infile, str);
			sscanf(str.c_str(), "%d:%d %d:%d", &DH, &DM, &AH, &AM);
			A[j] = make_pair(DH*60 + DM, AH*60 + AM);
		}
		for (size_t j = 0; j < nB; ++j)
		{
			int DH, DM, AH, AM;
			string		str;
			getline(infile, str);
			sscanf(str.c_str(), "%d:%d %d:%d", &DH, &DM, &AH, &AM);
			B[j] = make_pair(DH*60 + DM, AH*60 + AM);
		}

		pair<int, int>	res = GetTrainCnt(A, B, T);
		outfile << "Case #" << i+1 << ": " << res.first << " " << res.second << std::endl;
	}

	return 0;
}

