//
//  main.cpp
//  cj2
//
//  Created by Soshi Manako on 12/04/14.
//  Copyright (c) 2012. All rights reserved.
//

#include <iostream>
#include <string.h>

int main(int argc, const char * argv[])
{
    // Read input
    char inputBuffer[2048];
    memset(inputBuffer, 0, sizeof(inputBuffer));
    gets(inputBuffer);
    
    int nLines = atoi(inputBuffer);
    for (int i = 0; i < nLines; ++i) { 
        int nAlreadyExceed = 0;
        int nCanExceedBySurprising = 0;
        
        memset(inputBuffer, 0, sizeof(inputBuffer));
        gets(inputBuffer);
        
        char* ptr = strtok(inputBuffer, " ");
        // Get number of googlers
        int nGooglers = atoi(ptr);
        //printf("g:%d¥n", nGooglers);
        
        // Get number of surprising
        ptr = strtok(NULL, " ");
        int nSurprising = atoi(ptr);
        
        // Get best result threshold
        ptr = strtok(NULL, " ");
        int thBestResult = atoi(ptr);
        
        // Get each total scores
        int totalScore = 0;
        for (int g = 0; g < nGooglers; ++g) {
            ptr = strtok(NULL, " ");
            totalScore = atoi(ptr);
            
            int d = totalScore / 3;
            int r = totalScore % 3;
            
            switch (r) {
                case 0:
                    if (thBestResult <= d) {
                        ++nAlreadyExceed;
                    } else if (0 < d && thBestResult <= (d + 1)) {
                        ++nCanExceedBySurprising;
                    }
                    break;
                    
                case 1:
                    if (thBestResult <= (d + 1)) {
                        ++nAlreadyExceed;
                    }
                    break;
                    
                case 2:
                    if (thBestResult <= (d + 1)) {
                        ++nAlreadyExceed;
                    } else if (thBestResult <= (d + 2)) {
                        ++nCanExceedBySurprising;
                    }
                    break;
            }
                            
        }
        
        // Compute result
        int nMaximumExceed = nAlreadyExceed
            + std::min<int>(nCanExceedBySurprising, nSurprising);
        
        // Write output
        std::cout << "Case #" << (i+1) << ": " << nMaximumExceed << std::endl; 
    }
    return 0;
}

