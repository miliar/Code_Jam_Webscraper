#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <iostream>
#include <list>
#include <queue>

using namespace std;

bool isDiamondHere(const vector<list<long long>>& graph);

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	long long T;
	input >> T;

	for (long long i = 0; i < T; i++)
	{
		long long nClasses;
		input >> nClasses;

		vector<list<long long> > graph(0);

		for (long long j = 0; j < nClasses; j++)
		{
			long long nAttached;
			input >> nAttached;
			list<long long> thisList;
			for (long long k = 0; k < nAttached; k++)
			{
				long long temp;
				input >> temp;
				thisList.push_back(temp-1);
			}

			graph.push_back(thisList);
		}
		if(isDiamondHere(graph) )
			output << "Case #" << i+1 << ": Yes" << endl;
		else
			output << "Case #" << i+1 << ": No" << endl;
	}
}

bool isDiamondHere(const vector<list<long long>>& graph)
{
	long long nNodes = graph.size();
	for (long long i = 0; i < nNodes; i++)
	{
		vector<bool> found(nNodes);
		for (long long i = 0; i < nNodes; i++)
			found[i] = false;
		
		queue<long long> Q;
		
		Q.push(i);
		found[i] = true;

		while(!Q.empty())
		{
			long long thisNode = Q.front();
			Q.pop();
			list<long long>::const_iterator itr = graph[thisNode].begin();
			while (itr != graph[thisNode].end())
			{
				if(!found[*itr])
				{
					found[*itr] = true;
					Q.push(*itr);
				}
				else
					return true;
				itr++;
			}
		}
	}
	return false;
}