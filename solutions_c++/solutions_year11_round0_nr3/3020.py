#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
int main(int argc, char* argv [])
{
    fstream iFile, oFile;
    oFile.open("output.txt", ios::out);
    iFile.open(*(argv + 1), ios::in);
    int numCases, numCandy, X = 1;
    unsigned int tempVar;
    
    iFile >> numCases;
    vector <unsigned int > candyVector;
    for(int i = 0; i < numCases; i++){
        iFile >> numCandy;
        unsigned int tempSum = 0;
        for(int j = 0; j < numCandy; j++){
            iFile >> tempVar;
            tempSum += tempVar;
            candyVector.push_back(tempVar);
        }
        // sort the input
        sort(candyVector.begin(), candyVector.end());
        /*pos indicates the position in the vector till which Sean can have candies 
          with values starting from the right end of the vector*/
        int counter = 1;
        unsigned int seanSum, patrickSum;
        unsigned int totalSum = 0;
        while(counter < numCandy){
            seanSum = 0;
            patrickSum = 0;
            //patrick
            for(int a = 0; a < counter; a++)
                patrickSum = candyVector.at(a) ^ patrickSum;

            //sean
            for(int x = counter; x < numCandy; x++)
                seanSum = candyVector.at(x) ^ seanSum;

             if(patrickSum == seanSum){
                 for(int y = counter; y < numCandy; y++)
                     totalSum += candyVector.at(y);
                 cout << "Case #" << X << ": "<< totalSum << endl;
                 oFile << "Case #" << X << ": "<< totalSum << endl;
                 X++;
                 break;
             }
             else
                 counter++;
        }
        if(!totalSum){
            cout << "Case #" << X << ": " << "NO" << endl;
            oFile << "Case #" << X << ": "<< "NO" << endl;
            X++;
        }
        candyVector.clear();
    }
    iFile.close();
    oFile.close();
    return 0;
}