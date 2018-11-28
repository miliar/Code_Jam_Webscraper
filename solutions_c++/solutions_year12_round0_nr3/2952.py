#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>

//#include <cctype>
#include <cmath>

#include <fstream>

using namespace std;

int num(int a, int b)
{
	int count[10] = {0};

	for (int i = a; i <= b; i++)
	{
		char ci[100] = {0};
		itoa(i, ci, 10);
		int n = strlen(ci);
		if (n==1) continue;

		for (int j = a; j <= b; j++)
		{
			if (i==j) continue;

			char cj[100] = {0};
			itoa(j, cj, 10);

			if (n!=strlen(cj)) continue;
			

			int basis = 1;
			for (int k = 0; k < n-1; k++)
			{
				basis *= 10;	
			}

			int w = i;
			for (int k = 0; k < n; k++)
			{
				int res = w%10;
				int del = w/10;
				w = basis*res+del;
				if (w==j) 
				{
					count[n]++;
					//cerr << "i= " << i << " j= " << j << " basis=" << basis << endl;
					break;
				}
			}
		}
	}

	int r = 0;
	for (int i = 1; i < 10; i++)
	{
		r += count[i];
	}
	return r/2;
}
//----------------------------------------------------------//
int main(int argc, char *argv[])
{
	if (argc < 2) {cout << "wrong input" << endl;return 0;}

	ifstream infile;
	infile.open(argv[1]);
	int T = 0;
	if (infile.is_open())
	{
		char cc[1001] = {0};
		infile.getline(cc,1000,'\n');
		T = atoi(cc);
		cerr << "number of cases = " << T << endl;

		string line;
		int t = 1;
		while (t<=T)
		{
			char cc[1001] = {0};
			infile.getline(cc,1000,'\n');

			int a = 0;
			int b = 0;

			istringstream ss;
			ss.str(string(cc));
			ss >> a >> b;

			cout << "Case #" << t << ": " << num(a,b) << endl;
			t++;
		}
	}

	return 0;

}
