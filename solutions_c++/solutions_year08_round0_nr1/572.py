#include <iostream>
#include <set>
#include <map>
#include <string>

#define uint unsigned int
using namespace std;
int main()
{
	uint nCases;
	cin >> nCases;
	//cerr << nCases << " cases\n";
	for (uint i = 0; i < nCases; ++i)
	{
		uint nEngines;
		cin >> nEngines;
		//cerr << nEngines << " engines\n";
		set<string> engines;
		string s;
		getline(cin, s);
		for (uint j = 0; j < nEngines; ++j)	
		{
			string s;
			getline (cin, s);
			//cerr << "Engine " << j << " " << s << endl;
			engines.insert(s);
		}
		//cerr << "done\n";
		uint nQueries;
		uint nSwitches = 0;
		cin >> nQueries;
		//cerr << nQueries << " queries\n";
		getline(cin, s);
		set<string> cache, emptyCache;
		for (uint j = 0; j < nQueries; ++j)	
		{
			string q;
			getline (cin, q);
			if (engines.count(q))
				cache.insert(q);
			if (cache.size() == nEngines)
			{
				nSwitches++;
				cache = emptyCache;
				cache.insert(q);
			}
		}
		
		cout << "Case #" << i + 1 << ": " << nSwitches << endl;
	}
}
