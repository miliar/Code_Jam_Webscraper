//
//  main.cpp
//  cj3
//
//  Created by Soshi Manako on 12/04/14.
//  Copyright (c) 2012. All rights reserved.
//

#include <iostream>

const int divisors[] = {
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
};

int main(int argc, const char * argv[])
{
    char inputBuffer[2048];
    memset(inputBuffer, 0, sizeof(inputBuffer));
    gets(inputBuffer);
    
    int nLines = atoi(inputBuffer);
    
    for (int i = 0; i < nLines; ++i) {
        memset(inputBuffer, 0, sizeof(inputBuffer));
        gets(inputBuffer);
        
        // Read limits
        char* ptr = strtok(inputBuffer, " ");
        int digits = strlen(ptr);
        int minimum = atoi(ptr);
        
        ptr = strtok(NULL, " ");
        int maximum = atoi(ptr);
        
        int count = 0;

        // Count
        for (int n = minimum; n < maximum; ++n) {
            for (int shift = 1; shift < digits; ++shift) {
                
                // Compute B
                int divisor = divisors[shift - 1];
                int q = n / divisor;
                int r = n % divisor;
                
                int m = q + r * divisors[digits - shift - 1];
                
                if (n < m && m <= maximum) {
                   ++count;
                }
            }
        }
        
        // Write result
        int lineno = i + 1;
        std::cout << "Case #" << lineno;
        std::cout << ": " << count << std::endl;
        
    }
    return 0;
}

