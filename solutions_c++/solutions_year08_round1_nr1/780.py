#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <algorithm>

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

	fstream infile("A-small-attempt0.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);
	for(int i=0; i<icase; i++)
	{
		int res = 0;
		vector<int> v, w;
		clearm();
		getline(infile, line);
		int se;
		sscanf(line.c_str(), "%d", &se);
		getline(infile, line);
		stringstream sin(line);
		for(int j=0; j<se; j++)
		{
			int temp;
			sin >> temp;
			v.push_back(temp);
			//cout << temp;
		}
		getline(infile, line);
		stringstream sin2(line);
		for(j=0; j<se; j++)
		{
			int temp;
			sin2 >> temp;
			w.push_back(temp);
			//cout << temp;
		}
					int max = 0;
		for(j=0; j<se; j++)
		{
			max += v[j]*w[j];
		}
		sort(v.begin(), v.end());
		do{
			int pud = 0;
		for(j=0; j<se; j++)
		{
			pud += v[j]*w[j];
		}
		if(pud < max)
			max = pud;



		}while(next_permutation(v.begin(), v.end()));

		cout << "Case #" << i+1 << ": " << max << endl;
	}

	return 0;
}