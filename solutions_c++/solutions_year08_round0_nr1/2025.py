#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int solveSwitching(const vector<string>& engines, const vector<string>& queries)
{
    map<string, int> stringMap;
    int numEngines = engines.size();
    for(int e = 0; e < numEngines; ++e)
        stringMap[engines[e]] = e;
    
    int numQueries = queries.size();
    int numSwitches = 0;
    
    vector<bool> engineUsed(numQueries, false);
    int enginesSeen = 0;    
    int lastEngine = -1;
    for(int q = 0; q < numQueries; ++q)
    {
        int engineIndex = stringMap[queries[q]];
        //cout << engineIndex << endl;
        if(!engineUsed[engineIndex])
        {
            //cout << "first time seeing..." << endl;
            engineUsed[engineIndex] = true;
            ++enginesSeen;
            
            if(enginesSeen == (numEngines - 1) && lastEngine >= 0 && !engineUsed[lastEngine])
            {
                lastEngine = engineIndex;
                
                //cout << "exh"
                ++numSwitches;
                enginesSeen = 0;
                engineUsed = vector<bool>(numQueries, false);
                --q;
            }
            
            else if(enginesSeen == numEngines)
            {
                lastEngine = engineIndex;
                
                //cout << "exh"
                ++numSwitches;
                enginesSeen = 0;
                engineUsed = vector<bool>(numQueries, false);
                --q;
            }
        }
    }
        
    return numSwitches;
}

int main()
{
    int numCases;
    cin >> numCases;
    //cout << "cases: " << numCases << endl;    
    for(int c = 0; c < numCases; ++c)
    {
        int numEngines;
        cin >> numEngines;
        cin.ignore();
        
        vector<string> engines;
        //cout << "num engines: " << numEngines << endl;
        for(int e = 0; e < numEngines; ++e)
        {
            char engineName[128];
            cin.getline(engineName, 128);
            engines.push_back(engineName);
            //cout << "engine: " << engineName << endl;
        }
                
        int numQueries;
        cin >> numQueries;
        cin.ignore();
        
        vector<string> queries;
        //cout << "num queries: " << numQueries << endl;
        for(int q = 0; q < numQueries; ++q)
        {
            char query[128];
            cin.getline(query, 128);
            queries.push_back(query);
            //cout << "query: " << query << endl;
        }
        
        int numSwitches = solveSwitching(engines, queries);
        cout << "Case #" << (c + 1) << ": " << numSwitches << endl;
    }
    
    return 0;
}