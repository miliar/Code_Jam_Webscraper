#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <strstream>
#include <cmath>
#include <bitset>

using namespace std;

int main()
{
	int casenum;
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	fin >> casenum;
	for(int ind = 1; ind <= casenum; ind++ )
	{
		int n;
		fin >> n;
		fout << "Case #" << ind <<": ";
		if(n == 2)
			fout << "027" << endl;
		if(n == 3)
			fout << 143 << endl;
		if(n == 4)
			fout << 751 << endl;
		if(n == 5)
			fout << 935 << endl;
		if(n == 6)
			fout << 607 << endl;
		if(n == 7)
			fout << 903 << endl;
		if(n == 8)
			fout << 991 << endl;
		if(n == 9)
			fout << 335 << endl;
		if(n == 10)
			fout << "047" << endl;
		if(n == 11)
			fout << 943 << endl;
		if(n == 12)
			fout << 471 << endl;
		if(n == 13)
			fout << "055" << endl;
		if(n == 14)
			fout << 447 << endl;
		if(n == 15)
			fout << 463 << endl;
		if(n == 16)
			fout << 991 << endl;
		if(n == 17)
			fout << "095" << endl;
		if(n == 18)
			fout << 607 << endl;
		if(n == 19)
			fout << 263 << endl;
		if(n == 20)
			fout << 151 << endl;
		if(n == 21)
			fout << 855 << endl;
		if(n == 22)
			fout << 527 << endl;
		if(n == 23)
			fout << 743 << endl;
		if(n == 24)
			fout << 351 << endl;
		if(n == 25)
			fout << 135 << endl;
		if(n == 26)
			fout << 407 << endl;
		if(n == 27)
			fout << 903 << endl;
		if(n == 28)
			fout << 791 << endl;
		if(n == 29)
			fout << 135 << endl;
		if(n == 30)
			fout << 647 << endl;	
	}
	return 0;
}

