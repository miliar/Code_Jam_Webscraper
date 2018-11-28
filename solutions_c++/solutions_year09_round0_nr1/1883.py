/* 
 * File:   Alien.cpp
 * Author: hayoungpark
 *
 * Created on September 2, 2009, 4:05 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

bool check(string word, char* testCase, int nIndex, const int L);
char* parenEater(char* testCase);

int main(int argc, char** argv) {

    int L, D, N;
    fin >> L;
    fin >> D;
    fin >> N;

    string *pWords = new string[D];

    for(int iD = 0; iD < D; iD++)
        fin >> *(pWords + iD);

    int nIndex, nCount;
    string word, testCase;

    for(int iN = 0; iN < N; iN++) {
        nCount = 0;
        fin >> testCase;

        for(int iD = 0; iD < D; iD++) {
            nIndex = 0;
            word = *(pWords + iD);
            if(check(word, &testCase[0], nIndex, L))
                nCount++;
        }

        fout << "Case #" << iN + 1 << ": " << nCount << endl;
    }
    return 0;
}

bool check(string word, char* testCase, int nIndex, const int L) {
    bool bParen = false;
    
    if(nIndex > L)
        return true;
    
    if(*testCase == '(') {
        testCase++;
        bParen = true;
    }
    
    do {
        if(*testCase == word[nIndex]) {
            if(bParen)
                testCase = parenEater(testCase);
        
            return check(word, ++testCase, ++nIndex, L);
        }
        testCase++;
        if(*testCase == ')')
            bParen = false;
    } while(bParen);
    
    return false;
}

char* parenEater(char* testCase) {
    while(*testCase != ')')
        testCase++;
    return testCase;
}
