#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int icase = 0;

	fstream infile("A-small-attempt0.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);
	for(int i=0; i<icase; i++)
	{
		int res = 0;
		vector<int> v;
		getline(infile, line);
		int max;
		int ke;
		int se;
		sscanf(line.c_str(), "%d %d %d", &max, &ke, &se);
		getline(infile, line);
		stringstream sin(line);
		for(int j=0; j<se; j++)
		{
			int temp;
			sin >> temp;
			v.push_back(temp);
			//cout << temp;
		}
		sort(v.begin(), v.end());
		int cou = 0;
		int inc = 1;
		for(j=se-1; j>-1; j--)
		{
			if(cou == ke)
			{
				inc++;
				cou = 0;
			}
			cou ++;
			res += v[j]*inc;
		}


		cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}