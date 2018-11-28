#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int nTestCases;
int caseNumber;
long long N;
int Pd;
int Pg;

bool ProcessCase()
{
	if (Pd == 0 && Pg == 0)
		return true;
	if (Pd > 0 && Pg == 0)
		return false;
	if (Pd < 100 && Pg == 100)
		return false;
//	if (Pd < Pg)
		//return false;
	int maxy;
	if (N < 100)
		maxy = (int)N;
	else
		maxy = 100;
	bool possible = false;
	int win = 0;
	for (int i=1; i<=maxy; i++)
	{
		int x = (Pd*i)%100;
		if (x==0)
		{
			return true;
		}
	}
	return possible;
}

int main()
{
	string file1;
	string file2;
	file1 = "e:\\A-small-attempt3.in";
	//file1 = "e:\\zin.txt";
	file2 = "e:\\z2.out";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// comment this line for console output:
	freopen_s(&ps, file2.c_str(), "wt", stdout);

	scanf("%d", &nTestCases);
	for (int caseNumber=1; caseNumber<=nTestCases; caseNumber++)
	{
		cin >> N;
		cin >> Pd;
		cin >> Pg;
		string result;
		if (ProcessCase())
			result = "Possible";
		else
			result = "Broken";
		cout << "Case #" << caseNumber << ": ";
		cout << result << endl;
	}
	return 0;
}
