#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>

#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;



int Solve(istream &in)
{
	int n;
	in >> n;
	vector< int > c(n);
	int xor = 0, sum = 0, c_min = INT_MAX;
	for (int i = 0; i < n; ++i)
	{
		in >> c[i];
		xor ^= c[i];
		sum += c[i];
		c_min = min(c_min, c[i]);
	}

	return !xor ? sum - c_min : 0;
}


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t;
	fin >> t;
	for (int cnt = 1; cnt <= t; ++cnt)
	{
		fout << "Case #" << cnt << ": ";
		int res = Solve(fin);
		if (res)
			fout << res;
		else
			fout << "NO";
		fout << endl;
	}

	return 0;
}