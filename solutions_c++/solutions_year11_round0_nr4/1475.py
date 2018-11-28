#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[])
{
    fstream iFile, oFile;
    iFile.open(*(argv + 1), ios::in);
    oFile.open("output.txt", ios::out);
    vector < int > numVector;
    int numCases, numValues, tempVar;
    int X = 1;
    iFile >> numCases;
    for(int x = 0; x < numCases; x++){
        iFile >> numValues;
        for(int y = 0; y < numValues; y++){
            iFile >> tempVar;
            numVector.push_back(tempVar);
        }
        vector < int > dupVector = numVector;
        sort(dupVector.begin(), dupVector.end());
        int i, j = 0;
        for(i = 0; i < numValues; i++){
            if((numVector[i] != dupVector[i]))
                j++;
        }
        float bnm = (float)(j);
       
        numVector.clear();
        //cout.setf(ios::fixed, ios::floatfield);
       // cout.precision(6);
       // cout << bnm << endl;
        oFile.setf(ios::fixed, ios::floatfield);
        oFile.precision(6);
        oFile << "Case #" << X++ << ": " << bnm << endl;

    }
    iFile.close();
    oFile.close();
    return 0;
}