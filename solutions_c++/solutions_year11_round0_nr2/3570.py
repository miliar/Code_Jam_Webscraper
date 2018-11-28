//
//  main.cpp
//  codejam
//
//  Created by Gavin Song on 5/7/11.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, const char * argv[])
{
    string line;
    
    ifstream inputFile;
    inputFile.open("B-large.in.txt");
    
    ofstream outputFile;
    outputFile.open("B-large.out.txt");
    
    
    if (inputFile.is_open()) {
    
        getline(inputFile, line);
        int T = atoi (line.c_str());
        for (int Case = 1; Case <= T; Case++) {
            
            outputFile << "Case #" << Case << ": [";
            
            getline(inputFile, line, ' ');
            int C = atoi (line.c_str());
			string * combines = new string [C];
            string * results = new string [C];
			for (int i = 0; i < C; i++) {
                getline(inputFile, line, ' ');
                combines[i] = line.substr(0, 2);
                results[i] = line.substr(2, 1);
            }
			
            getline(inputFile, line, ' ');
            int D = atoi (line.c_str());
			string * opposes = new string [D];
			for (int i = 0; i < D; i++) {
                getline(inputFile, line, ' ');
                opposes[i] = line;
            }
            
            getline(inputFile, line, ' ');
            
            getline(inputFile, line);
            string elements = line;
            
            for (int index = 0; index < elements.size() - 1; index++) {
                if (elements.size() == 0) break;
                
                string pair = elements.substr(index, 2);
                string reversepair = pair.substr(1, 1) + pair.substr(0, 1);
                for (int i = 0; i < C; i++) {
                    if (combines[i] == pair || combines[i] == reversepair) {
                        elements.replace(index, 2, results[i]);
                        break;
                    }
                }
                
                
                string nextElement = elements.substr(index + 1, 1);
                for (int i = 0; i < D; i++) {
                    if (opposes[i].substr(0, 1) == nextElement) {
                        if (elements.substr(0, index + 1).find(opposes[i].substr(1, 1)) != -1) {
                            elements.erase(0, index + 2);
                            index = -1;
                            break;
                        }
                    } else if (opposes[i].substr(1, 1) == nextElement) {
                        if (elements.substr(0, index + 1).find(opposes[i].substr(0, 1)) != -1) {
                            elements.erase(0, index + 2);
                            index = -1;
                            break;
                        }
                    }
                }
                
            }
            
            if (elements.size() > 0) {
                outputFile << elements[0];
                for (int i = 1; i < elements.size(); i++) {
                    outputFile << ", " << elements[i];
                }
            }
            outputFile << "]";
            outputFile << endl;
            
        }
        
    } else cout << "failed to open input file";
    
    return 0;
}

