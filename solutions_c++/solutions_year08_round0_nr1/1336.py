#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <limits>

using namespace std;

int solve(const vector<string> & vecQuery, const vector<string> & vecSe)
{
	vector<int> vecSt;
	vecSt.resize(vecQuery.size() + 1);

	// Init
	fill(vecSt.begin(), vecSt.end(), numeric_limits<int>::max());
	for ( size_t i = 0; i < vecSe.size(); ++i )
	{
		size_t j = 0;
		for ( j = 0; j < vecQuery.size(); ++j )
		{
			if ( vecQuery.at(j) == vecSe.at(i) )
			{
				vecSt.at(j) = min(1, vecSt.at(j));
				break;
			}
		}
		if ( j >= vecQuery.size() )
		{
			vecSt.at(vecQuery.size()) = min(0, vecSt.at(vecQuery.size()));
		}
	}

	// compute
	for ( size_t i = 0; i < vecQuery.size(); ++i )
	{
		if ( vecSt.at(i) >= numeric_limits<int>::max() )
		{
			continue;
		}

		for ( size_t j = 0; j < vecSe.size(); ++j )
		{
			if ( vecQuery.at(i) == vecSe.at(j) )
			{
				continue;
			}
			size_t k = i + 1;
			for ( ;k < vecQuery.size(); ++k )
			{
				if ( vecQuery.at(k) == vecSe.at(j) )
				{
					vecSt.at(k) = min(vecSt.at(i)+1, vecSt.at(k));
					break;
				}
			}
			if ( k >= vecQuery.size() )
			{
				vecSt.at(vecQuery.size()) = min(vecSt.at(vecQuery.size()), vecSt.at(i));
			}
		}
	}

	return vecSt.at(vecQuery.size());
}

int main(int argc, char *argv[])
{
	if ( argc < 2 )
	{
		return -1;
	}

	ifstream fin(argv[1]);
	if ( !fin )
	{
		cerr << "Fail to open file " << argv[1] << endl;
		return -1;
	}

	int N = 0;
	string strLine;
	if ( !getline(fin, strLine) )
	{
		cerr << "Fail to read N" << endl;
		return -1;
	}
	N = atoi(strLine.c_str());

	for ( int i = 0; i < N; ++i )
	{
		vector<string> vecQuery, vecSe;

		// Read se name
		if ( !getline(fin, strLine) )
		{
			cerr << "Fail to read se number" << endl;
			return -1;
		}

		int se = atoi(strLine.c_str());
		for ( int s = 0; s < se; ++s )
		{
			if ( !getline(fin, strLine) )
			{
				cerr << "Fail to read se name" << endl;
				return -1;
			}
			vecSe.push_back(strLine);
		}

		// Read query
		if ( !getline(fin, strLine) )
		{
			cerr << "Fail to read query number" << endl;
			return -1;
		}
		int qn = atoi(strLine.c_str());
		for ( int q = 0; q < qn; ++q )
		{
			if ( !getline(fin, strLine) )
			{
				cerr << "Fail to read query " << q << endl;
				return -1;
			}
			vecQuery.push_back(strLine);
		}

		// Output result
		cout << "Case #" << i + 1 << ": " << solve(vecQuery, vecSe) << endl;
	}
	return 0;
}
