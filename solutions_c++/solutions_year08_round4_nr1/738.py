#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

string calc(int M, int V, vector<int> &G, vector<int> &C, vector<int> &I)
{
	vector<int> steps0, steps1, val;
	steps0.resize(M);
	steps1.resize(M);
	val.resize(M);
	for (int i=M-1; i>=0; --i)
	{
		//cout << i << endl;
		if (i>=(M-1)/2)
		{				
			if (I[i-(M-1)/2]==1)
			{
				steps0[i] = -1;
				steps1[i] = 0;
				val[i] = 1;
			}
			else
			{
				steps0[i] = 0;
				steps1[i] = -1;
				val[i] = 0;
			}
		}
		// inner node
		else
		{
			int child1 = i*2+1;
			int child2 = i*2+2;
			val[i] = 
				(G[i]==1) ? 
					val[child1] * val[child2] : 
					min(1,val[child1] + val[child2]);
			{
				if (val[i]==0)
				{
					steps0[i] = 0;
					int step1 = INT_MAX, step2 = INT_MAX, step3 = INT_MAX;
					if (G[i]==1)
					{
						if (steps1[child1]>=0 && steps1[child2]>=0)
							step1 = steps1[child1] + steps1[child2];
						if (C[i]==1)
						{
							if (steps1[child1]>=0)
								step2 = 1 + steps1[child1];
							if (steps1[child2]>=0)
								step3 = 1 + steps1[child2];
						}
					}
					else
					{
						if (steps1[child1]>=0)
							step2 = steps1[child1];
						if (steps1[child2]>=0)
							step3 = steps1[child2];
					}
					steps1[i] = min(min(step1,step2),step3);
					if (steps1[i]==INT_MAX) steps1[i] = -1;
				}
				else
				{
					steps1[i] = 0;
					int step1 = INT_MAX, step2 = INT_MAX, step3 = INT_MAX;
					if (G[i]==1)
					{
						if (steps0[child1]>=0)
							step2 = steps0[child1];
						if (steps0[child2]>=0)
							step3 = steps0[child2];
					}
					else
					{
						if (steps0[child1]>=0 && steps0[child2]>=0)
							step1 = steps0[child1] + steps0[child2];
						if (C[i]==1)
						{
							if (steps0[child1]>=0)
								step2 = 1 + steps0[child1];
							if (steps0[child2]>=0)
								step3 = 1 + steps0[child2];
						}
					}
					steps0[i] = min(min(step1,step2),step3);
					if (steps0[i]==INT_MAX) steps0[i] = -1;
				}
			}
		}
	}
	for (int i=M-1; i>=0; --i)
	{
		//cout << val[i] << " " << steps0[i] << " " << steps1[i] << endl;
	}
	int res = V==1 ? steps1[0] : steps0[0];
	if (res==-1)
		return "IMPOSSIBLE";
	stringstream iss;
	iss << res;
	return iss.str();
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream fin(argv[1]);
	int numcases;
	fin >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int M,V;
		fin >> M >> V;
		vector<int> G,C;
		for (int j=0; j<(M-1)/2; ++j)
		{
			int g,c;
			fin >> g >> c;
			G.push_back(g);
			C.push_back(c);
		}
		vector<int> I;
		for (int j=0; j<(M+1)/2; ++j)
		{
			int ih;
			fin >> ih;
			I.push_back(ih);
		}
		cout << "Case #" << i+1 << ": " << calc(M,V,G,C,I) << endl;
	}
	fin.close();
	return 0;
}