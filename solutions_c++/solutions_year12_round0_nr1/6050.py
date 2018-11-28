/* 
 * File:   main.cpp
 * Author: Andrew Jones
 * 
 * Google Code Jam Qualification Round
 * Speaking In Tongues
 * Created on April 13, 2012, 7:36 PM
 */

#include <cstdlib>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int X = 1;

string SpeakingInTongues(string S);

int main(int argc, char** argv) {
    
    const char * inFilename = argv[1];
    const char * outFilename = argv[2];
        
    ifstream inFile(inFilename);
    ofstream outFile(outFilename);
    
    string inputLine;
    string outputLine;
    
    getline(inFile, inputLine);
    string count = inputLine;

    while (getline(inFile, inputLine))
    {
        outputLine = SpeakingInTongues(inputLine);
        outFile << outputLine << endl;
        X++;
    }
    return 0;
}

string SpeakingInTongues(string S)
{
    string output;
    
    for(int i = 0; i < S.length(); i++)
    {
          switch(S[i])
          {
               case 'a':
               S[i] = 'y';
               break;
               
               case 'b':
               S[i] = 'h';
               break;
               
               case 'c':
               S[i] = 'e';
               break;
               
               case 'd':
               S[i] = 's';
               break;
               
               case 'e':
               S[i] = 'o';
               break;
               
               case 'f':
               S[i] = 'c';
               break;
               
               case 'g':
               S[i] = 'v';
               break;
               
               case 'h':
               S[i] = 'x';
               break;
               
               case 'i':
               S[i] = 'd';
               break;
               
               case 'j':
               S[i] = 'u';
               break;
               
               case 'k':
               S[i] = 'i';
               break;
               
               case 'l':
               S[i] = 'g';
               break;
               
               case 'm':
               S[i] = 'l';
               break;
               
               case 'n':
               S[i] = 'b';
               break;
               
               case 'o':
               S[i] = 'k';
               break;
               
               case 'p':
               S[i] = 'r';
               break;
               
               case 'q':
               S[i] = 'z';
               break;
               
               case 'r':
               S[i] = 't';
               break;
               
               case 's':
               S[i] = 'n';
               break;
               
               case 't':
               S[i] = 'w';
               break;
               
               case 'u':
               S[i] = 'j';
               break;
               
               case 'v':
               S[i] = 'p';
               break;
               
               case 'w':
               S[i] = 'f';
               break;
               
               case 'x':
               S[i] = 'm';
               break;
               
               case 'y':
               S[i] = 'a';
               break;
               
               case 'z':
               S[i] = 'q';
               break;
              
          }
    }
    stringstream sstring;
    
    sstring << "Case #" << X << ": " << S;
    output = sstring.str();
    
    return output;
}

