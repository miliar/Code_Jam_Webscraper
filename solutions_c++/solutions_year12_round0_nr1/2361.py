//
//  main.cpp
//  CodeJam-1-1
//
//  Created by Ryan Luedders on 4/13/12.
//  Copyright 2012 n/a. All rights reserved.
//

#include <iostream>
#include <fstream>

#include "CodeJam-1-1.h"

int main (int argc, const char * argv[])
{
    bool result = false;
    
    if( argc > 1 )
    {
        std::vector<std::string> codeLines = CJ11::readFile( argv[1] );
        std::vector<std::string> translatedLines;
        
        // start at line 1, to ignore the first line which is just the
        // number of lines to follow
        for( int i = 1; i < codeLines.size(); i++ )
        {
            if( codeLines[i].size() > 0 )
            {
                translatedLines.push_back( CJ11::solveProblem( i, codeLines[i] ) );
            }
        }
        
        result = CJ11::writeFile( argv[2], translatedLines );
    }
    return result;
}

