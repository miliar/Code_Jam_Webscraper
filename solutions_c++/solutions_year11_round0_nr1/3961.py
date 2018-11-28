//
//  main.cpp
//  codejam
//
//  Created by Gavin Song on 5/7/11.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, const char * argv[])
{
    string line;
    
    ifstream inputFile;
    inputFile.open("A-large.in.txt");
    
    ofstream outputFile;
    outputFile.open("A-large.out.txt");
    
    
    if (inputFile.is_open()) {
        
        getline(inputFile, line);
        int T = atoi (line.c_str());
        for (int Case = 1; Case <= T; Case++) {
            
            outputFile << "Case #" << Case << ": ";
            
            int orangePos = 1;
            int bluePos = 1;
            int orangeExtraTime = 0;
            int blueExtraTime = 0;
            int totalTime = 0;
            
            getline(inputFile, line, ' ');
            for (int N = atoi(line.c_str()); N > 1; N--) {
                getline(inputFile, line, ' ');
                if (line == "O") {
                    getline(inputFile, line, ' ');
                    int taskTime = 1 + fabs(orangePos - atoi(line.c_str())) - orangeExtraTime;
                    orangePos = atoi(line.c_str());
                    if (taskTime < 1) {
                        orangeExtraTime = 0;
                        taskTime = 1;
                    } else orangeExtraTime = 0;
                    blueExtraTime += taskTime;
                    totalTime += taskTime;
                } else {
                    getline(inputFile, line, ' ');
                    int taskTime = 1 + fabs(bluePos - atoi(line.c_str())) - blueExtraTime;
                    bluePos = atoi(line.c_str());
                    if (taskTime < 1) {
                        blueExtraTime = 0;
                        taskTime = 1;
                    } else blueExtraTime = 0;
                    orangeExtraTime += taskTime;
                    totalTime += taskTime;
                }
            }
            
            getline(inputFile, line, ' ');
            if (line == "O") {
                getline(inputFile, line);
                int taskTime = 1 + fabs(orangePos - atoi(line.c_str())) - orangeExtraTime;
                orangePos = atoi(line.c_str());
                if (taskTime < 1) {
                    orangeExtraTime = 0;
                    taskTime = 1;
                } else orangeExtraTime = 0;
                blueExtraTime += taskTime;
                totalTime += taskTime;
            } else {
                getline(inputFile, line);
                int taskTime = 1 + fabs(bluePos - atoi(line.c_str())) - blueExtraTime;
                bluePos = atoi(line.c_str());
                if (taskTime < 1) {
                    blueExtraTime = 0;
                    taskTime = 1;
                } else blueExtraTime = 0;
                orangeExtraTime += taskTime;
                totalTime += taskTime;
            }
            
            outputFile << totalTime << endl;
            
        }
        
    } else cout << "failed to open input file";
    
    return 0;
}

