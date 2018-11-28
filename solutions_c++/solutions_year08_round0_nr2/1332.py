#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <map>

using namespace std;

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
		if ( !getline(fin, strLine) )
		{
			cerr << "Fail to get time T" << endl;
			return -1;
		}
		int T = atoi(strLine.c_str());

		if ( !getline(fin, strLine) )
		{
			cerr << "Fail to get NA, NB for case " << i << endl;
			return -1;
		}
		istringstream isstrm;
		isstrm.str(strLine);
		int NA, NB;
		if ( !(isstrm >> NA >> NB) )
		{
			cerr << "Fail to parse NA, NB for case " << i << endl;
			return -1;
		}

		map<int, int> mapA, mapB;
		for ( int j = 0; j < NA; ++j )
		{
			if ( !getline(fin, strLine) )
			{
				cerr << "Fail to read TA for case " << i << endl;
				return -1;
			}
			int dep, arr, dh, dm, ah, am;
			sscanf(strLine.c_str(), "%2d:%2d %2d:%2d\n", &dh, &dm, &ah, &am);
			dep = dh * 60 + dm;
			arr = ah * 60 + am;
			mapA[dep]--;
			mapB[arr+T]++;
		}

		for ( int j = 0; j < NB; ++j )
		{
			if ( !getline(fin, strLine) )
			{
				cerr << "Fail to read TB for case " << i << endl;
				return -1;
			}
			int dep, arr, dh, dm, ah, am;
			sscanf(strLine.c_str(), "%2d:%2d %2d:%2d\n", &dh, &dm, &ah, &am);
			dep = dh * 60 + dm;
			arr = ah * 60 + am;
			mapB[dep]--;
			mapA[arr+T]++;
		}

		int minA, minB, sumA, sumB;
		minA = minB = sumA = sumB = 0;
		map<int, int>::const_iterator iter;
		for ( iter = mapA.begin(); iter != mapA.end(); ++iter )
		{
			sumA += iter->second;
			minA = min(minA, sumA);
		}

		for ( iter = mapB.begin(); iter != mapB.end(); ++iter )
		{
			sumB += iter->second;
			minB = min(minB, sumB);
		}

		cout << "Case #" << i+1 << ": " << -minA << ' ' << -minB << endl;
	}
}
