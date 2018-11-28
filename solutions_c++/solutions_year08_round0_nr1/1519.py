#include<iostream>
#include<vector>
#define INVALID 999999
using namespace std;

int findFirst(vector<string> names, string name, int pos)
{
	for(int i = pos; i < names.size();i++)
	{
		if(names[i] == name)
			return i;
	}
	return INVALID;
}

int main()
{
	int testCases;
	cin >> testCases;
	for(int test = 0; test < testCases;test++)
	{
		int numEngines;
		cin >> numEngines;
		string garbage;
		getline(cin, garbage);
		vector<string> names;
		for(int i = 0; i < numEngines;i++)
		{
			string name;
			getline(cin, name);
			names.push_back(name);
		}
		
		
		int numQueries;
		cin >> numQueries;
		getline(cin, garbage);		
		vector<string> queries;
		for(int i = 0; i < numQueries;i++)
		{
			string line;
			getline(cin, line);
			queries.push_back(line);
		}
		
			
		int pos = 0;
		int max = pos;
		for(int i = 0; i < names.size();i++)
		{
			int temp = findFirst(queries, names[i], pos);
			if(temp > max)
				max = temp;
		}
		pos = max;
		int num = 0;
		while(pos < queries.size())
		{
			max = pos;
			for(int i = 0; i < names.size();i++)
			{
				int temp = findFirst(queries, names[i], pos);
				if(temp > max)
					max = temp;
			}
			//cout << "pos is " << pos << endl;
			pos = max;
			num++;
		}
		
		cout << "Case #" << test+1 << ": " << num << endl;
		
	}
		
}