//
//  SpeakTongue.cpp
//  CodeJam2012
//
//  Created by Donny Lee on 14/4/12.
//  Copyright (c) 2012 Duke University. All rights reserved.
//

#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include "CodeJam.h"

std::string convertToEnglish( std::string Input ){
    std::string InputString = Input;
    std::string aString = "";
    while ( InputString.size() > 0 ) {
        if ( InputString[0] == 'a' )
            aString = aString + "y";
        if ( InputString[0] == 'b' )
            aString = aString + "h";
        if ( InputString[0] == 'c' )
            aString = aString + "e";
        if ( InputString[0] == 'd' )
            aString = aString + "s";
        if ( InputString[0] == 'e' )
            aString = aString + "o";
        if ( InputString[0] == 'f' )
            aString = aString + "c";
        if ( InputString[0] == 'g' )
            aString = aString + "v";
        if ( InputString[0] == 'h' )
            aString = aString + "x";
        if ( InputString[0] == 'i' )
            aString = aString + "d";
        if ( InputString[0] == 'j' )
            aString = aString + "u";
        if ( InputString[0] == 'k' )
            aString = aString + "i";
        if ( InputString[0] == 'l' )
            aString = aString + "g";
        if ( InputString[0] == 'm' )
            aString = aString + "l";
        if ( InputString[0] == 'n' )
            aString = aString + "b";
        if ( InputString[0] == 'o' )
            aString = aString + "k";
        if ( InputString[0] == 'p' )
            aString = aString + "r";
        if ( InputString[0] == 'q' )
            aString = aString + "z";
        if ( InputString[0] == 'r' )
            aString = aString + "t";
        if ( InputString[0] == 's' )
            aString = aString + "n";
        if ( InputString[0] == 't' )
            aString = aString + "w";
        if ( InputString[0] == 'u' )
            aString = aString + "j";
        if ( InputString[0] == 'v' )
            aString = aString + "p";
        if ( InputString[0] == 'w' )
            aString = aString + "f";
        if ( InputString[0] == 'x' )
            aString = aString + "m";
        if ( InputString[0] == 'y' )
            aString = aString + "a";
        if ( InputString[0] == 'z' )        // Don't know.
            aString = aString + "q";
        if ( InputString[0] == ' ' )
            aString = aString + " ";
        if ( InputString.size() == 1 )
            break;
        InputString = InputString.substr(1);
    }

    return aString;
}

int main (int argc, const char * argv[])
{
    int count = 1;
    // Open a file.
    std::ofstream answerFile;
    answerFile.open ("/Users/catalyst/Documents/iPhone_dev/CodeJam2012/CodeJam2012/STAnswer.txt");
    //answerFile << "Output\n";
    
    // insert code here...
    std::cout << "Let's solve Speak Tongue.\n";
    std::string aLine = "";
    std::ifstream aFile;
    aFile.open("/Users/catalyst/Documents/iPhone_dev/CodeJam2012/CodeJam2012/STInput.txt");
    
    if (aFile.is_open() == true)
    {
        getline (aFile,aLine);
        std::cout << "File opened." << std::endl;
        while ( aFile.good() )
        {
            getline (aFile,aLine);
            std::cout << aLine << std::endl;
            
            // Write the answer to output file.
            answerFile << "Case #" << count << ": ";
            answerFile << convertToEnglish(aLine) << std::endl;
            count = count + 1;
        }
        aFile.close();
    }
    
    answerFile.close();
    std::cout << "Program has ended" << std::endl;
    return 0;
}

