/* 
 * File:   main.cpp
 * Author: frox
 *
 * Created on April 14, 2012, 1:48 PM
 */

#include <cstdlib>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <time.h>

using namespace std;

/*
 * 
 */
int solveProblem(string line) {
    int i, n, s, p;
    stringstream str;
    str << line;
    string tmp;
    str >> tmp;
    n = atoi(tmp.c_str());
    str >> tmp;
    s = atoi(tmp.c_str());
    str >> tmp;
    p = atoi(tmp.c_str());
    //   cout << "n:" << n << " s: " << s << " p:" << p;
    int scoreSum;
    int result = 0;
    for (i = 0; i < n; i++) {
        str >> tmp;
        scoreSum = atoi(tmp.c_str());
        if ((scoreSum / 3) >= p) {
            result++;
            continue;
        }
        int j;
        char judges[3];
        for (j = 0; j < 2; j++) {//
            judges[j] = (p - j);
            scoreSum -= (p - j);            
        }        
        if(scoreSum<0)continue;
        if ((judges[0] - scoreSum) >= 4)continue;
        if ((judges[0] - scoreSum) >= 2) {
            if (s) {
                s--;
            } else continue;
        }
        result++;
    }
    return result;
}

int main(int argc, char** argv) {
    int i;
    ifstream inFile("/home/frox/Dropbox/Dropbox/private/Codejam/CODEJAM_2A/sample", ios::in);
    string line;
    getline(inFile, line);
    int cases;
    cases = atoi(line.c_str());
    for (i = 1; i <= cases; i++) {
        cout << "Case #" << i << ": ";
        getline(inFile, line);
        cout << solveProblem(line);
        if (i != cases)cout << endl;
    }

    return 0;
}

