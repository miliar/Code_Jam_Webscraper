#include <iostream>
#include <string>
#include <vector>
#include <set>

#include <math.h>

using namespace std;

// return true if has more work to do
//   the string at the 'return true' point is the engine to use from the beginning pos to the ending pos.
bool findNextSwitchPoint(set<string>& engines, vector<string>& queries, int& pos)
{
    set<string> foundEngines;
    if (pos != -1)
        foundEngines.insert(queries[pos]);
    int uniqueEnginesSeen = foundEngines.size();

    for (unsigned i = pos + 1; i < queries.size(); i++)
    {
        if (engines.find(queries[i]) != engines.end() && foundEngines.find(queries[i]) == foundEngines.end())
        {
            uniqueEnginesSeen++;
            foundEngines.insert(queries[i]);

            if (uniqueEnginesSeen == engines.size())
            {
                pos = i;
                return true;
            }
        }
    }
    return false;
}

// run contest1 < input_file > output_file
int main()
{
    int sets;
    cin >> sets;

    for (int i = 0; i < sets; i++)
    {
        int numEngines;
        set<string> engines;
        cin >> numEngines;
        for (int j = 0; j < numEngines; j++)
        {
            string temp;
            getline(cin, temp);
            if (temp == "")
                getline(cin, temp);
            engines.insert(temp);
        }

        int numQueries;
        cin >> numQueries;
        vector<string> queries;
        queries.reserve(1000);
        for (int j = 0; j < numQueries; j++)
        {
            string temp;
            getline(cin, temp);
            if (temp == "")
                getline(cin, temp);
            queries.push_back(temp);
        }

        int numSwitches = 0;
        int pos = -1;
        while (findNextSwitchPoint(engines, queries, pos) == true)
        {
            numSwitches++;
        }
        cout << "Case #" << i+1 << ": " << numSwitches << endl;
    }

    return 0;
}