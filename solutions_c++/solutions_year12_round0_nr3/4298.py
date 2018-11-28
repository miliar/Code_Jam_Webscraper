//
//  RecycledNumbers.cpp
//  CodeJam2012
//
//  Created by Donny Lee on 14/4/12.
//  Copyright (c) 2012 Duke University. All rights reserved.
//
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include "CodeJam.h"

std::string int2string( int input);
int MoveBackToFront(int input);
bool isItPair( int first, int second);
std::string MoveBackToFront( std::string input );

std::string int2string( int input ){
    int myInput = input;
    std::string s;
    std::stringstream out;
    out << myInput;
    s = out.str();
    return s;
}

int MoveBackToFront(int input) {
    int myInput = input;
    // Convert to String.
    std::string stringInput = int2string( myInput );
    stringInput = stringInput[ stringInput.size() - 1 ] + stringInput.substr(0, stringInput.size() - 1);
    return atoi(stringInput.c_str());
}

std::string MoveBackToFront( std::string input ){
    std::string stringInput = input;
    stringInput = stringInput[ stringInput.size() - 1 ] + stringInput.substr(0, stringInput.size() - 1);
    return stringInput;
}

// Assume both is different.
bool isItPair(int first, int second){
    int myFirst = first;
    int mySecond = second;
    std::string myFirstString = int2string(myFirst);
    int mySize = (int)myFirstString.size();
    for ( int i = 0; i < mySize - 1; i++ ){
        myFirstString = MoveBackToFront(myFirstString);
        if ( atoi(myFirstString.c_str()) == mySecond )
            return true;
    }
    return false;
}

int main (int argc, const char * argv[])
{
    int first;
    int second;
    
    int count = 1;
    // Open a file.
    std::ofstream answerFile;
    answerFile.open ("/Users/catalyst/Documents/iPhone_dev/CodeJam2012/CodeJam2012/RNAnswer.txt");
    //answerFile << "Output\n";
    
    // insert code here...
    std::cout << "Let's solve Recycled Number.\n";
    std::string aLine = "";
    std::ifstream aFile;
    aFile.open("/Users/catalyst/Documents/iPhone_dev/CodeJam2012/CodeJam2012/RNInput.txt");
    
    if (aFile.is_open() == true)
    {
        getline (aFile,aLine);
        std::cout << "File opened." << std::endl;
        while ( aFile.good() )
        {
            int numberOfPairs = 0;
            getline (aFile,aLine);
            std::cout << aLine << std::endl;
            
            // Get the first int.
            first = atoi( (aLine.substr(0, aLine.find(" ") )).c_str() );
            second = atoi( (aLine.substr(aLine.find(" ") + 1)).c_str() );
                        
            std::cout << "first is " << first << " second is " << second << std::endl;
            
            //std::cout << "Is it a pair " << isItPair(130, 301) << std::endl;
            
            // If size is 1, return none.
            if ( first < 10 ) {
                numberOfPairs = 0;
            } else { 
                for ( int i = second ; i > first; i-- ) {
                    for ( int j = i - 1; j >= first; j-- ) {
                        //std::cout << "first is " << i << " second is " << j << std::endl;
                        if ( isItPair( i, j ) == true )
                            numberOfPairs = numberOfPairs + 1;
                    }
                }
            
            }
            answerFile << "Case #" << count << ": " << numberOfPairs << std::endl;
            //answerFile << convertToEnglish(aLine) << std::endl;
            count = count + 1;
        }
        aFile.close();
    }
    
    answerFile.close();
    std::cout << "Program has ended" << std::endl;
    return 0;
}
