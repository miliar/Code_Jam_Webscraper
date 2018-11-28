//
//  QualsB.cpp
//  CodeJam2012
//
//  Created by Yushi Wang on 4/14/12.
//  Copyright (c) 2012 Stanford University. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int cases;
    ofstream outFile;
    ifstream inFile;
    inFile.open("//Users//yushiwang//Documents//Stanford 2011-2012//Winter11-12//CS97SI1//CodeJam2012//B-small-attempt3.in");
    outFile.open("//Users//yushiwang//Documents//Stanford 2011-2012//Winter11-12//CS97SI1//CodeJam2012//B-small3.out");
    inFile >> cases;
    inFile.ignore();
    cout << cases;
    int total, surprises, cutoff, good;
    for (int num = 1; num <= cases; num++) {
        good = 0;
        int currScore, modThree;
        inFile >> total >> surprises >> cutoff;
        cout << num << " " << total;
        for (int i = 0; i < total; i++) {
            inFile >> currScore;
            modThree = currScore % 3;
            cout << " " << currScore;
            currScore /= 3;
            if (modThree > 0) currScore++;
            if (currScore >= cutoff) good++;
            else if ((currScore == cutoff - 1) && (modThree != 1) && (surprises > 0) && (currScore > 0)) {
                surprises--;
                good++;
            }
        }
        cout << endl;
        outFile << "Case #" << num << ": " << good << endl;
    }
    return 0;
}