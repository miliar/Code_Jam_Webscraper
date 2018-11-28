#include <iostream>
#include <map>
#include <string>

using namespace std;

void doTestCase();

int main()
{
    int numTestCases;
    cin >> numTestCases;

    for( int testCase = 1; testCase <= numTestCases; ++testCase )
    {
        cout << "Case #" << testCase << ": ";
        doTestCase();
    }

    return 0;
}

void doTestCase()
{
    int numSearchEngines;

    cin >> numSearchEngines;

    map<string, int> searchEngineMap;

    cin.ignore(1000, '\n');
    for( int i = 0; i < numSearchEngines; ++i )
    {
        string temp;
        getline(cin, temp);
        searchEngineMap[temp] = i;
    }

    int numQueries;
    cin >> numQueries;
    cin.ignore(1000, '\n');

    int numSwitches = 0;

    bool used[numSearchEngines];
    memset( used, 0, numSearchEngines );

    int usedCount = 0;

    for( int i = 0; i < numQueries; ++i )
    {
        string temp;
        getline(cin, temp);
        int searchEngineNumber = searchEngineMap[temp];

        if( !used[searchEngineNumber] )
        {
            ++usedCount;

            if( usedCount == numSearchEngines )
            {
                ++numSwitches;
                memset( used, 0, numSearchEngines );
                usedCount = 1;
            }

            used[searchEngineNumber] = true;
        }
    }

    cout << numSwitches << endl;
}
