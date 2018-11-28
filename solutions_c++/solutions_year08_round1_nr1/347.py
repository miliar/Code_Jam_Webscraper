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
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	fin >> casenum;
	for(int ind = 1; ind <= casenum; ind++ )
	{
		int scale;
		fin >> scale;
		int *vec1 = new int [scale];
		int *vec2 = new int [scale];
		for(int i = 0; i < scale; i++)
			fin >> vec1[i];
		for(int i = 0; i < scale; i++)
			fin >> vec2[i];
		sort(&vec1[0],&vec1[scale]);
		sort(&vec2[0],&vec2[scale],greater<int>());
		_int64 salar(0);
		for(int i = 0;  i < scale; i++)
			salar += vec1[i]*vec2[i];
		fout << "Case #"<< ind << ": " << salar << endl;
	}
	return 0;
}

