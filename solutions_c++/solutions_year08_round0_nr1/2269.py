#include<iostream>
#include<vector>
#include<map>

using namespace std;

void
resetSearchEng (map<string, bool>& searchEngMap)
{
    map<string, bool>::iterator begin = searchEngMap.begin();
    map<string, bool>::iterator end = searchEngMap.end();
    while (begin != end) {
        begin->second = false;
        ++begin;
    }
}


int
processTc ()
{
    int numSearchEngs;
    cin >> numSearchEngs;
    vector<string> searchEngs(numSearchEngs);
    map<string, bool> searchEngMap;
  
    char line[101];
    cin.getline(line, 101);
    for (size_t i = 0; i < numSearchEngs; ++i) {
        cin.getline(line, 101);
        searchEngs[i] = line;
        searchEngMap[searchEngs[i]] = false;
    }
   
    int numQueries;
    cin >> numQueries;
    cin.getline(line, 101);
    vector<string> queries(numQueries);
    map<string, bool>::iterator findItr;
    int cswitch = 0;
    int found = 0;
   
    for (size_t i = 0; i < numQueries; ++i) {
        cin.getline(line, 101);
        queries[i] = line;
        findItr = searchEngMap.find(queries[i]);
        if (!findItr->second) {
            findItr->second = true;
            found++;
            if (found == numSearchEngs) {
                cswitch++;
                resetSearchEng(searchEngMap);
                findItr->second = true;
                found = 1;
            }
        }
    }
    return cswitch;
}


int main()
{
    int numTcs;
    cin >> numTcs;
    for (size_t i = 0; i < numTcs; ++i) {
        int sol = processTc();
        cout << "Case #" << i+1 << ": " << sol << endl;
    }
}
