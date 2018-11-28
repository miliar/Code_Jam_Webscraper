/*
 * sand.cpp
 *
 *  Created on: May 15, 2011
 *      Author: bill
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;

bool isAttainable(int max, int percent)
{
	if(percent == 0 || percent == 100) return true;
	for(int i=2; i<=max; i++)
	{
		for(int j=1; j<i; j++)
		{
			if((double(j * 100) / i) == percent) return true;
		}
	}
	return false;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int testCases, Case = 1;
	fin >> testCases;
	while(testCases--)
	{
		fout << "Case #" << Case++ << ": ";
		int N, pG, pD;
		fin >> N >> pD >> pG;
		if((pD != 100 && pG == 100) || (pD != 0 && pG == 0)) fout << "Broken" << endl;
		else if(isAttainable(N, pD)) fout << "Possible" << endl;
		else fout << "Broken" << endl;
	}
	return 0;
}
