#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("D-small-attempt0.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		string s;
		fin >> s;

		ull ones = 0;
		ull zeros = 0;
		for (int i=0; i<s.size(); ++i)
		{
			ones <<= 1;
			zeros <<= 1;

			char c = s[i];
			if (c == '1') ones |= 1;
			if (c == '0') zeros |= 1;
		}

		double dStart = sqrt(double(ones));
		ull result = dStart;
		if (result * result > ones)
			--result;

		while (true)
		{
			ull square = result * result;
			bool onesOK = (square & ones) == ones;
			bool zerosOK = (square & zeros) == 0;
			if (onesOK && zerosOK)
				break;
			++result;
		}

		result *= result;
		string rOut;
		while (result > 0)
		{
			string next = (result%2 > 0) ? "1" : "0";
			rOut = next + rOut;
			result /= 2;
		}

		fout << "Case #" << zz << ": " << rOut << endl;
	}

	return 0;
}