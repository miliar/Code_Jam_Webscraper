#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool IsLightOnNumber(int n, long k)
{
     long temp = (long)pow(2, (long double)n);
     if (((k+1) % temp) == 0)
        return true;
        
     return false;
 } 

int main(int argc, char* argv[])
{
    ifstream inFile;
    long caseCount = 0;
    int numberOfSnapper = 0;
    int numberOfSnap = 0;
    
    char fileName[] = "A-large.in";
    
    inFile.open(fileName);
    
    if(!inFile)
    {
        cout << "Can not open input file" << endl;
        return 1;
    }
    
    inFile >> caseCount;
    
    for (int i = 0; i < caseCount; ++i)
    {
        inFile >> numberOfSnapper;
        inFile >> numberOfSnap;
        
        if (IsLightOnNumber(numberOfSnapper, numberOfSnap))
           cout << "Case #" << i+1 << ": ON" << endl;
        else
           cout << "Case #" << i+1 << ": OFF" << endl;
    }
    
    inFile.close();
    
    return 0;
}
