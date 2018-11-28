#include <iostream>
#include <fstream>
#include <vector>
#include <string>


using namespace std;

//ifstream fin("sample.in");
//#define cin fin


int optimize(vector<string> engines, vector<string> queries)
{
	vector<pair<int,int> > encounters;

	for (int i=0; i < engines.size(); i++)
	{
		bool engine_counted = false;
		bool optimized = true;
		for (int j=0; j < queries.size(); j++)
		{
			if (engines[i].compare(queries[j]) == 0)
			{
				if (!engine_counted)
				{
					encounters.push_back(make_pair(i,j));
					engine_counted = true;
				}
				optimized = false;
			}
				
		}
		if (optimized)
			return 0;
	}
	
	int last_queried = 0;
	int last_engine = 0;
	for (int k=0; k < encounters.size(); k++)
	{
		if (last_queried < encounters[k].second)
		{
			last_engine = k;
			last_queried = encounters[k].second;
		}
	}

	vector<string> queries_left;
	for (int i=last_queried; i < queries.size(); i++)
	{
		queries_left.push_back(queries[i]);
	}
	
	return 1 + optimize(engines, queries_left);
}


int main()
{
	int numtestcases, numengines, numqueries;
	cin >> numtestcases;
	
	for (int i=1; i <= numtestcases; i++)
	{
		cin >> numengines;
		string curengine;
		vector<string> engines;
		
		string trash;
		getline(cin, trash);
		for (int j=1; j <= numengines; j++)
		{
			getline(cin, curengine);
			engines.push_back(curengine);	
		}
		
		string curquery;
		vector<string> queries;
		cin >> numqueries;
		getline(cin, trash);
		for (int k=1; k <= numqueries; k++)
		{
			getline(cin, curquery);
			queries.push_back(curquery);
		}
		
		int switches = optimize(engines, queries);
		cout << "Case #" << i << ": " << switches << endl;	
	}
}
