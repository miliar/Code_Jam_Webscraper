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

int num(int n, int s, int p, vector<int> totals)
{
	if (p==0) return totals.size();

	sort(totals.begin(), totals.end(), greater<int>());

	int count = 0;
	for (int i = 0; i < totals.size(); i++)
	{
		if (totals[i]>=3*p-2) {count++;continue;}
		if ((p>1)&&(s>0))
		{
			if (totals[i]>=3*p-4) {count++;s--;}
		}
	}

	return count;
}

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
		int i = 1;
		while (i<=T)
		{
			char cc[1001] = {0};
			infile.getline(cc,1000,'\n');

			int n = 0;
			int s = 0;
			int p = 0;
			string str1;

			istringstream ss;
			ss.str(string(cc));
			ss >> n >> s >> p;

			vector<int> totals;
			for (int j = 0; j < n; j++)
			{
				int k = 0;
				ss >> k;
				totals.push_back(k);
			}

			cerr << "n = " << n << endl;
			cerr << "s = " << s << endl;
			cerr << "p = " << p << endl;
			for (int j = 0; j < n; j++)
			{
				cerr << "player #" << j << " total score = " << totals[j] << endl;
			}
			cerr << "------------------" << endl;
			
			//cerr << totals[0] << " : " << totals[1] << endl;

			cout << "Case #" << i << ": " << num(n,s,p,totals) << endl;
			i++;
		}
	}

	return 0;

}
