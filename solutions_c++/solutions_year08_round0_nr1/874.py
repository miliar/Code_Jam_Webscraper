#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>

using namespace std;

	int mark[200];

void clearm()
{
	for(int i=0; i<200; i++)
		mark[i] = 0;
}

int main()
{
	int icase = 0;

	fstream infile("A-large.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);
	for(int i=0; i<icase; i++)
	{
		int res = 0;
		vector<string> v;
		clearm();
		getline(infile, line);
		int se;
		sscanf(line.c_str(), "%d", &se);
		for(int j=0; j<se; j++)
		{
			getline(infile, line);
			v.push_back(line);
		}
		getline(infile, line);
		int ip;
		sscanf(line.c_str(), "%d", &ip);
		for(int k=0; k<ip; k++)
		{
			getline(infile, line);
			int a;
			for(a=0; a<v.size(); a++)
				if(v[a] == line)
					break;
			mark[a] = 1;
			int count = 0;
			for(int ii=0; ii<v.size(); ii++)
				if(mark[ii] == 1)
					count++;
			if(count == v.size())
			{
				clearm();
				res++;
				mark[a] = 1;
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}