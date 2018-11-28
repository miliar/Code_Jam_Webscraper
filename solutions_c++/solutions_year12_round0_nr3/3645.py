//
//  main.cpp
//  recycled
//
//  Created by Pierre Lacave on 14/04/2012.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <sstream>

std::string convertInt(int number)
{
    std::stringstream ss;//create a stringstream
    ss << number;//add number to the stream
    return ss.str();//return a string with the contents of the stream
}

int main (int argc, const char * argv[])
{

    // insert code here...
    int a;
    int b;
    int count = 0;
    int recycle = 0;
    std::string s;
    std::cin >> count;
    std::cin.ignore();
    
    for (int c = 0; c < count; c++)
    {
        std::getline( std::cin, s );
        std::istringstream iss(s, std::istringstream::in);
        iss >> a;
        iss >> b;
        recycle = 0;
        for (int i = a; i < b; i++)
        {
            for (int j = i + 1; j <= b; j++)
            {
                std::string doublestr = convertInt(i) + convertInt(i);
                //std::cout << doublestr << " " << i << std::endl;
                if (doublestr.find(convertInt(j)) != std::string::npos)
                    recycle++;
            }
                
        }
        std::cout << "Case #"<<c+1<<": "<< recycle << std::endl;
    }
    return 0;
}

