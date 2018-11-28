//
//  main.cpp
//  CodeJam-1-3
//
//  Created by Ryan Luedders on 4/13/12.
//  Copyright 2012 n/a. All rights reserved.
//

#include <iostream>
#include <fstream>

#include "CodeJam-1-3.h"

int main (int argc, const char * argv[])
{
    bool result = false;
    
    if( argc > 1 )
    {
        std::vector<std::string> codeLines = CJ13::readFile( argv[1] );
        std::vector<std::string> resultLines;
        
        // start at line 1, to ignore the first line which is just the
        // number of lines to follow
        for( int i = 1; i < codeLines.size(); i++ )
        {
            if( codeLines[i].size() > 0 )
            {
                resultLines.push_back( CJ13::solveProblem( i, codeLines[i] ) );
            }
        }
        
        result = CJ13::writeFile( argv[2], resultLines );
    }
    return result;
}

