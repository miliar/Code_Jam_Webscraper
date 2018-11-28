#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <stdint.h>

using namespace std;

#define MIN(a, b) \
  ({ typeof(a) _a = (a); \
     typeof(b) _b = (b); \
     _a < _b ? _a : _b; })


int16_t dp[100][1000];
vector<string> stringQueries; // the literal string queries
vector<int> intQueries; // Replace a query for a search engine by its index, otherwise -1
map<string, uint8_t> searchEngines;
int nEngines = 0;
uint16_t nQueries = 0;

int16_t minSwitches(uint16_t queryNum, uint8_t engineNum)
{
    int16_t& result = dp[queryNum][engineNum];
    if (result > 0)
        return result;
    
    if (queryNum == nQueries)
        return 0;
    
    if (intQueries[queryNum] != engineNum) // not a engine name or not our engine name
        result = minSwitches(queryNum + 1, engineNum);
    else {
        result = 2001; // MAX number
        // we would need to switch, try all options.
        for (uint8_t newEngineNum=0; newEngineNum < nEngines; newEngineNum++) {
            if (newEngineNum==engineNum)
                continue;
            result = MIN(result, 1 + minSwitches(queryNum + 1, newEngineNum));
        }
    }
    
    return result;
}


int main()
{
    int nTestCases;
    cin >> nTestCases;
    cin.ignore(4, '\n');
    
    for (int caseNum=0; caseNum < nTestCases; caseNum++) {
        cout << "Case #" << caseNum + 1 << ": ";
        for (int i=0;i<100;i++)
            for (int j=0; j<1000; j++)
                dp[i][j]= -1;
        stringQueries.clear();
        intQueries.clear();
        searchEngines.clear();
        
        string line;
        cin >> nEngines; cin.ignore(4, '\n');
        for (int engineNum = 0; engineNum < nEngines; engineNum++) {
            getline(cin, line);
            searchEngines[line] = engineNum;
        }
        
        cin >> nQueries; cin.ignore(4, '\n');
        for (uint16_t queryNum = 0; queryNum < nQueries; queryNum++) {
            getline(cin, line);
            stringQueries.push_back(line);
            if (searchEngines.count(line) == 1) // query is an engine name
                intQueries.push_back(searchEngines[line]);
            else
                intQueries.push_back(-1);
        }
        
        int16_t answer = 10000;
        // loop over starting engines
        for (int engineNum = 0; engineNum < nEngines; engineNum++) {
            answer = MIN(answer, minSwitches(0, engineNum));
        }
        cout << answer << endl;
    }
}