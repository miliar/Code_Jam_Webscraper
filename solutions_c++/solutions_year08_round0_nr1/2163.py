#include <iostream>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

int main()
{
	string temp;
	int N, S, Q, switches;
	
	getline(cin, temp);
	N = atoi(temp.c_str());
	
	for (int i=1; i<=N; i++)
	{
		cout << "Case #" << i << ": ";
		
		getline(cin,temp);
		S = atoi(temp.c_str());
		
		set<string> engines;
		
		while (S--)
		{
			string name;
			getline(cin, name);
			engines.insert(name);
		}
		
		getline(cin,temp);
		Q = atoi(temp.c_str());
		
		set<string> copy(engines);
		switches = 0;
		
		while (Q--)
		{
			string query;
			getline(cin, query);
			
			copy.erase(query);
			if (copy.empty())
			{
				copy = engines;
				copy.erase(query);
				switches++;
			}
		}
		
		
		cout << switches << endl;
	}
	
	
	return 0;
}