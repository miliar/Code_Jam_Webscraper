//
//  main.cpp
//  cj1
//
//  Created by Soshi Manako on 12/04/14.
//  Copyright (c) 2012. All rights reserved.
//

#include <iostream>
#include <ctype.h>

struct TranslationRuleItem
{
    char eng;
    char goog;
};

const TranslationRuleItem translationRule[] = {
    { 'a' , 'y' },
    { 'b' , 'n' },
    { 'c' , 'f' },
    { 'd' , 'i' },
    { 'e' , 'c' },
    { 'f' , 'w' },
    { 'g' , 'l' },
    { 'h' , 'b' },
    { 'i' , 'k' },
    { 'j' , 'u' },
    { 'k' , 'o' },
    { 'l' , 'm' },
    { 'm' , 'x' },
    { 'n' , 's' },
    { 'o' , 'e' },
    { 'p' , 'v' },
    { 'q' , 'z' },
    { 'r' , 'p' },
    { 's' , 'd' },
    { 't' , 'r' },
    { 'u' , 'j' },
    { 'v' , 'g' },
    { 'w' , 't' },
    { 'x' , 'h' },
    { 'y' , 'a' },
    { 'z' , 'q' },
};

char TranslateChar(char c, const char* translationTable);

int main(int argc, const char * argv[])
{
    char translationTable[26];
    for (int i = 0; i < 26; ++i) {
        TranslationRuleItem item = translationRule[i];
        int tableIndex = item.goog - 'a';
        translationTable[tableIndex] = item.eng;
    }

    // Read input
    char inputBuffer[128];
    char outputBuffer[128];
    memset(inputBuffer, 0, sizeof(inputBuffer));
    gets(inputBuffer);
    int nLines = atoi(inputBuffer);
    
    for (int i = 0; i < nLines; ++i) {
        memset(inputBuffer, 0, sizeof(inputBuffer));
        memset(outputBuffer, 0, sizeof(outputBuffer));
        gets(inputBuffer);
        
        // Translate
        char* pSrc = inputBuffer;
        char* pDst = outputBuffer;
        while (*pSrc) {
            *pDst = TranslateChar(*pSrc, translationTable);            
            ++pSrc;
            ++pDst;
        }
        
        // Write output
        std::cout << "Case #" << (i+1) << ": " << outputBuffer << std::endl;
    }
    
    return 1;
}

char TranslateChar(char c, const char* translationTable)
{
    if (isalpha(c)) {
        return translationTable[c - 'a'];
    }
    return ' ';
}
