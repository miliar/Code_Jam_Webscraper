#include <iostream>
#include <string>
#include <map>
using namespace std;

typedef map<string,bool> Engine;

int main()
{
	int i_cases;

	cin >> i_cases;

	for (int i = 0; i < i_cases; i++)
	{
		int i_engines, i_queries;
		Engine engines;
		cin >> i_engines;
		string engine_str;
		cin.ignore();
		for (int j = 0; j < i_engines; j++)
		{
			getline (cin, engine_str);
			engines[engine_str] = true;
		}

		cin >> i_queries;
		cin.ignore();
		string queries[i_queries];
		int switches = 0;
		string query;
		int soft_count = 0;
		for (int j = 0; j < i_queries; j++)
		{
			getline (cin, query);
		//	cout << "Query: " << query << " ";
			if (engines[query])
			{
		//		cout << "Changing state: " << query << endl; 
				engines[query] = false;
				soft_count++;
			}

			if (soft_count == i_engines)
			{
				switches++;
		//		cout << "Resetting"<< endl;
				for (Engine::iterator ii = engines.begin(); 
						ii != engines.end(); ++ii)
					ii->second = true;
				engines[query] = false;
				soft_count = 1;
			}
		}
		cout << "Case #" << i+1 << ": " << switches << endl;
	}
}


