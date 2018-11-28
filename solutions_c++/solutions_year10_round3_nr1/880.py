#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
using namespace std;

int main() {

	int icase = 0;
	vector<string> dic;
	fstream infile("A-large.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);
	
	for(int i=0; i<icase; i++)
	{
		vector<pair<int, int> > p;
		int ipair = 0;
		getline(infile, line);
		sscanf(line.c_str(), "%d", &ipair);
		int res = 0;
		int x, y;
		for(int j=0; j<ipair; j++)
		{
			getline(infile, line);
			sscanf(line.c_str(), "%d %d", &x, &y);
			p.push_back(make_pair(x, y));

		}
		for( j=0; j<ipair; j++)
		{
			for(int k=0; k<ipair; k++)
			{
				if((p[j].first-p[k].first)*(p[j].second-p[k].second) < 0)
					res ++;
			}
		}
		cout << "Case #" << i+1 << ": " << res/2 << endl;
	}

	return 0;
}
