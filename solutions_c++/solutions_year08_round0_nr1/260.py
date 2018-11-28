#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int calc(vector<string> &engines, vector<string> &queries)
{
	/*cout << "En:\n";
	for (int i=0; i<engines.size(); ++i)
		cout << engines[i] << endl;
	cout << "Qu:\n";
	for (int i=0; i<queries.size(); ++i)
		cout << queries[i] << endl;*/

	int sw = 0;

	set<int> next;
	int last = -1;
	
	next.clear();
	for (int i=0; i<(int)engines.size(); ++i) next.insert(i);
	
	for (vector<string>::iterator query = queries.begin(); query != queries.end(); ++query)
	{
		for (int i=0; i<(int)engines.size(); ++i)
			if (engines[i]==*query)
			{
				next.erase(i);
				last = i;
				break;
			}
		//if (next.size()==1)
			//cout << engines[*next.begin()] << endl;
		if (next.empty())
		{
			for (int i=0; i<(int)engines.size(); ++i) if (last!=i) next.insert(i);
			sw++;
		}
	}
	
	return sw;
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream f(argv[1]);
	int numcases;
	f >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int numengine, numquery;
		vector<string> engines;
		vector<string> queries;
		f >> numengine;
		for (int j=0; j<=numengine; ++j)
		{
			char str[200];
			f.getline(str, 200);
			if (j>0)
				engines.push_back(str);
		}
		f >> numquery;
		for (int j=0; j<=numquery; ++j)
		{
			char str[200];
			f.getline(str, 200);
			if (j>0)
				queries.push_back(str);
		}
		cout << "Case #" << i+1 << ": " << calc(engines, queries) << endl;
	}
	f.close();
	return 0;
}