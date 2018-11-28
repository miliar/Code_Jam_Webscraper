#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

static const size_t npos = -1;
bool IsPossible(int max, int pDay, int pGlob);

int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;
	cout << N << " num cases" << endl;

	for( int n = 0; n < N; n++ ) {
		int maxToday = 0;
		int pDay = 0;
		int pGlobal = 0;
		string maxStr = "";

		fin >> maxStr;
		fin >> pDay;
		fin >> pGlobal;

		if (maxStr.length() >= 3)
			maxToday = 100;
		else
			maxToday = atoi(maxStr.c_str());

		string answer = IsPossible(maxToday, pDay, pGlobal) ? "Possible" : "Broken";

			
		cout << "Case #" << n+1 << ": " << answer << endl;
		fout << "Case #" << n+1 << ": " << answer << endl;
	}

	return 0;
}

bool IsPossible(int max, int pDay, int pGlob)
{
	if (pGlob == 100 && pDay != 100)
		return false;

	if (pGlob == 0 && pDay != 0)
		return false;

	if (pDay == 0 || pDay == 100)
		return true;

	int dayDenom = 100;

	while (pDay != 0 && pDay % 5 == 0 && dayDenom % 5 == 0)
	{
		pDay /= 5;
		dayDenom /= 5;
	}
	while (pDay != 0 && pDay % 2 == 0 && dayDenom % 2 == 0)
	{
		pDay /= 2;
		dayDenom /= 2;
	}
	if (max < dayDenom)
		return false;

	return true;
}
