#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream inFile;
    long caseCount = 0;
    long numberOfRuns = 0;
    long numberOfCapacity = 0;
    int numberOfGroups = 0;
    int* groupPeople;
    
    char fileName[] = "C-small-attempt0.in";
    
    inFile.open(fileName);
    
    if(!inFile)
    {
        cout << "Can not open input file" << endl;
        return 1;
    }
    
    inFile >> caseCount;
    
    for (int i = 0; i < caseCount; ++i)
    {
        inFile >> numberOfRuns;
        inFile >> numberOfCapacity;
        inFile >> numberOfGroups;
        
        groupPeople = new int[numberOfGroups];
        
        for (int j=0; j<numberOfGroups; ++j)
            inFile >> groupPeople[j];
            
        int curIndex = 0;
        long income = 0;
            
        for (int j=0; j<numberOfRuns; ++j)
        {
            int curPeople = groupPeople[curIndex];
            int curGroupNumber = 1;
            
            curIndex = (curIndex + 1)%numberOfGroups;
            
            while (( (numberOfCapacity - curPeople) >= groupPeople[curIndex] ) && (curGroupNumber < numberOfGroups))
            {
                  curPeople += groupPeople[curIndex];
                  curIndex = (curIndex + 1)%numberOfGroups;
                  curGroupNumber++;
            }
            
            income += curPeople;
        }
        
        cout << "Case #" << i+1 << ": " << income << endl;
        
    }
    
    inFile.close();
    
    return 0;
}
