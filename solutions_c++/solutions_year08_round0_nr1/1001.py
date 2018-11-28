#include <iostream>
#include <fstream>
#include <set>

int main()
{
    int numTestCases = 0;
    std::cin >> numTestCases;

    typedef std::set<std::string> SearchEngineMap;
    typedef SearchEngineMap::iterator SEMI;

    for (int i = 0; i < numTestCases; ++i)
    {
	char buf[101];

	int numSwitches = 0;
	int numSearchEngines = 0;
	std::cin >> numSearchEngines;
	std::cin.getline(buf, sizeof buf, '\n');

	SearchEngineMap searchEngines;
	for (int j = 0; j < numSearchEngines; ++j)
	{
	    std::cin.getline(buf, sizeof buf, '\n');
	    std::string se(buf);
//	    std::cout << "Read SE: " << se << std::endl;
	    searchEngines.insert(se);
	}

	int numQueries = 0;
	std::cin >> numQueries;
	std::cin.getline(buf, sizeof buf, '\n');

	SearchEngineMap queriers = searchEngines;

	for (int k = 0; k < numQueries; ++k)
	{
	    std::cin.getline(buf, sizeof buf, '\n');
	    std::string query(buf);
//	    std::cout << "Read Query: " << query << std::endl;

	    SEMI iter = queriers.find(query);
	    if (iter != queriers.end())
	    {
		queriers.erase(iter);
		if (queriers.empty())
		{
//		    std::cout << "Query so far: " << query << std::endl;
		    ++numSwitches;
		    queriers = searchEngines;
		    queriers.erase(query);
		}
	    }
	}
	std::cout << "Case #" << i+1 << ": " << numSwitches << std::endl;
    }

    return 0;
}
