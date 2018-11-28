// Problem 1: Imploding Universe

#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef  map<string, bool>  StringIntMap;

void
ResetVisited (StringIntMap&  visitedElems)
{
    StringIntMap::iterator begin = visitedElems.begin();
    StringIntMap::iterator end   = visitedElems.end();
    for ( ; begin != end; ++begin) 
        begin->second = false;
}


unsigned int
FindNumSwitches()
{
    char line[101];
    unsigned int numElems;
    cin >> numElems;
    cin.getline(line, 101);
    
    vector<string> elems(numElems);
    StringIntMap   visitedElems;
  
    for (unsigned int i = 0; i < numElems; ++i) {
        cin.getline(line, 101);
        elems[i] = line;
        visitedElems[elems[i]] = false;
    }
   
    unsigned int seqSize;
    cin >> seqSize;
    cin.getline(line, 101);
    
    vector<string>  sequence(seqSize);
    StringIntMap::iterator  pos;
    unsigned int numSwitches = 0;
    unsigned int count = 0;
   
    for (size_t i = 0; i < seqSize; ++i) {
        cin.getline(line, 101);
        sequence[i] = line;
        
        pos = visitedElems.find(sequence[i]);
        if (pos->second)
            continue;
        
        pos->second = true;
        ++count;
        if (count < numElems) 
            continue;

        numSwitches++;
        ResetVisited(visitedElems);
        pos->second = true;
        count = 1;
    }
    
    return numSwitches;
}


int 
main()
{
    int numSequences;
    cin >> numSequences;
    for (size_t i = 0; i < numSequences; ++i) 
        cout << "Case #" << i + 1 << ": " << FindNumSwitches() << endl;
}
