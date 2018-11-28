#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;




int main()
{
	//ifstream inp("input.txt");
	//ofstream out("output.txt");

	//ifstream inp("B-small.in");
	//ofstream out("B-small.out");

	ifstream inp("B-large.in");
	ofstream out("B-large.out");

	int numCases;
	inp >> numCases;	
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		int t, na, nb;
		string temp;
		inp >> t >> na >> nb;
		
		getline(inp, temp);
		vector<int> ta(60 * 24 + t, 0);
		vector<int> tb(60 * 24 + t, 0);


		for (int i = 0; i < na; i++) 
		{
			getline(inp,  temp);
			int h1, m1, h2, m2;
			sscanf(temp.c_str(),"%d:%d %d:%d", &h1, &m1, &h2, &m2);
			ta[60 * h1 + m1]--;
			tb[60 * h2 + m2 + t] ++;
		}

		for (int i = 0; i < nb; i++) 
		{
			getline(inp,  temp);
			int h1, m1, h2, m2;
			sscanf(temp.c_str(),"%d:%d %d:%d", &h1, &m1, &h2, &m2);
			tb[60 * h1 + m1]--;
			ta[60 * h2 + m2 + t] ++;
		}
		
		int curA = 0, curB = 0;
		int needA = 0, needB = 0;
		for (int i = 0; i < 60 * 24; i++)
		{
			curA += ta[i];
			if (curA < 0)
			{
				needA -= curA;
				curA = 0;
			}

			curB += tb[i];
			if (curB < 0)
			{
				needB -= curB;
				curB = 0;
			}
		}

		out << "Case #" << curCase << ": " << needA << " " << needB << endl;

	}

	return 0;
}