//
//  main.cpp
//  SpeakingInTongues
//
//  Created by Youngjin Kim on 12. 4. 14..
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>

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
        getline(inFile, sInputLine);
        sOutputLine = sInputLine;
        
        size_t size = sInputLine.length();
        for(int j = 0; j < size; j++) {
            char c = sInputLine[j];
            switch (c) {
                case 'a': c = 'y'; break;
                case 'b': c = 'h'; break;
                case 'c': c = 'e'; break;
                case 'd': c = 's'; break;
                case 'e': c = 'o'; break;
                case 'f': c = 'c'; break;
                case 'g': c = 'v'; break;
                case 'h': c = 'x'; break;
                case 'i': c = 'd'; break;
                case 'j': c = 'u'; break;
                case 'k': c = 'i'; break;
                case 'l': c = 'g'; break;
                case 'm': c = 'l'; break;
                case 'n': c = 'b'; break;
                case 'o': c = 'k'; break;
                case 'p': c = 'r'; break;
                case 'q': c = 'z'; break;
                case 'r': c = 't'; break;
                case 's': c = 'n'; break;
                case 't': c = 'w'; break;
                case 'u': c = 'j'; break;
                case 'v': c = 'p'; break;
                case 'w': c = 'f'; break;
                case 'x': c = 'm'; break;
                case 'y': c = 'a'; break;
                case 'z': c = 'q'; break;
                default:
                    break;
            }
            sOutputLine[j] = c;
        }
        
        cout << "Case #" << (i+1) << ": " << sOutputLine << endl;
    }
    
    inFile.close();
    
    return 0;
}

