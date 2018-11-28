//
//  main.cpp
//  RecycledNumbers
//
//  Created by Youngjin Kim on 12. 4. 14..
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>

std::string convertInt(int i);

using namespace std;

int main (int argc, const char * argv[])
{
    ifstream inFile;
    inFile.open("input.txt");
    
    string sInputLine = "";
    string sOutputLine = "";
    getline(inFile, sInputLine);
    
    int nCase = atoi(sInputLine.c_str());
    
    for(int i = 0; i < nCase; i++) {
        string sFromLine = "";
        string sToLine = "";
        
        getline(inFile, sFromLine, ' ');
        getline(inFile, sToLine);
        
        int nFrom = atoi(sFromLine.c_str());
        int nTo = atoi(sToLine.c_str());
        size_t nDigit = sFromLine.length();
        int nRN = 0;
        
        //cout << nFrom << " ~ " << nTo << ", nDigit = " << nDigit << endl;
        
        for(int n = nFrom; n <= nTo; n++) {
            
            if(nDigit == 1)
                continue;
            
            sOutputLine = sInputLine = convertInt(n);

            bool changed = false;
            for(int q = 0; q < nDigit - 1; q++) {
                if(sOutputLine[q] != sOutputLine[q+1]) {
                    changed = true;
                }
            }
            
            if(!changed) {
                continue;
            }
            
            int prevOutput = 0;
            
            for(int k = 0; k < nDigit; k++) {
                size_t size = sInputLine.length();
                for(int j = 0; j < size-1; j++) {
                    sOutputLine[j] = sInputLine[j+1];
                }
                sOutputLine[size-1] = sInputLine[0];
                
                int nOutput = atoi(sOutputLine.c_str());
                
                if(n < nOutput && prevOutput != nOutput && nOutput >= nFrom && nOutput <= nTo) {
                    //cout << n << " -> " << nOutput << "(" << (nRN+1) << ")" << endl;
                    nRN++;
                    prevOutput = nOutput;
                }
                sInputLine = sOutputLine;
            }
        }
        cout << "Case #" << (i+1) << ": " << nRN << endl;
    }
    
    inFile.close();
    return 0;
}

std::string convertInt(int i)
{
    std::stringstream ss;
    std::string s;
    ss << i;
    s = ss.str();
    
    return s;
}
