// Code jam 2012
#include <iostream>
#include <fstream>
using namespace std;

const int maxGooglers = 100;
const int judges = 3;

int main()
{
    string fname1 = "B-large.txt";
    string fname2 = "dancingGooglersOutput.txt";
    
    ifstream inFile(fname1.c_str());
    ofstream outFile(fname2.c_str());
    
    int numb, surp, limit, max;
    int array[maxGooglers];
    
    int count;
    inFile >> count;
    
    for (int x=1; x<=count; x++)
    {
        max = 0;
        inFile >> numb >> surp >> limit;
        for (int i=0; i < numb; i++)
            inFile >> array[i];
            
        for (int j=0; j < numb; j++)
        {
            int standLimit = judges*limit;
            
            if (array[j] < limit)
               continue;
            else if (array[j] - standLimit >= -2)
               max++;
            else if (array[j] - standLimit >= -4 && surp > 0) {
                max++;
                surp--;
            }   
        }
        
        outFile << "Case #" << x <<": " << max << endl;
        
    }
    
    
    
    inFile.close();
    outFile.close();
    
    
    system("pause");
    return 0;
}
