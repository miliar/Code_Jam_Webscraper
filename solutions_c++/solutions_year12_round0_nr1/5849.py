//
//  QualsA.cpp
//  CodeJam2012
//
//  Created by Yushi Wang on 4/14/12.
//  Copyright (c) 2012 Stanford University. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int lines;
    char inString[200];
    char outString[200];
    char convert[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
    ofstream outFile;
    ifstream inFile;
    inFile.open("//Users//yushiwang//Documents//Stanford 2011-2012//Winter11-12//CS97SI1//CodeJam2012//A-small-attempt1.in");
    inFile >> lines;
    inFile.ignore();
/*    cin >> lines;
    cin.ignore();*/
    outFile.open("//Users//yushiwang//Documents//Stanford 2011-2012//Winter11-12//CS97SI1//CodeJam2012//A-small1.out");
    cout << lines << endl;
    for (int num = 1; num <= lines; num++) {
        inFile.getline(inString, 101);
        for (int i = 0; i < 101; i++) {
            if (inString[i] <= 'z' && inString[i] >= 'a') {
                outString[i] = convert[inString[i] - 'a'];
            }
            else outString[i] = inString[i];
        }
        cout << num << " " << inString << endl;
        cout << num << " " << outString << endl;
        outFile << "Case #" << num << ": " << outString << endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}