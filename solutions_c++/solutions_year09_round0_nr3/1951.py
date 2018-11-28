/* 
 * File:   welcome.cpp
 * Author: hayoungpark
 *
 * Created on September 3, 2009, 7:14 AM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

#define SIZE 30

ifstream fin("C-small-attempt2.in");
ofstream fout("C-small-attempt2.out");

string welcome = "welcome to code jam";

int compare(char*, int);
void output(int);
int main(int argc, char** argv) {
    int N, nCount;
    fin >> N;

    char* testCase = new char[SIZE + 1];
    fin.ignore();
    for(int i = 0; i < N; i++) {
        fin.getline(testCase, SIZE + 1);
        nCount = compare(testCase, 0);
        fout << "Case #" << i + 1 << ": ";
        output(nCount);
    }

    return (EXIT_SUCCESS);
}

int compare(char* pText, int nIndex) {
    int n = 0;
    do{
        if(*pText == welcome[nIndex]) {
            if(nIndex == welcome.length() - 1)
                n++;
            else
                n += compare(pText + 1, nIndex + 1);
        }
    }while(*(++pText));
    return n;
}

void output(int nCount){
    char digit[5];
    nCount %= 10000;
    digit[0] = (char)(nCount / 1000 + 48);
    nCount %= 1000;
    digit[1] = (char)(nCount / 100 + 48);
    nCount %= 100;
    digit[2] = (char)(nCount / 10 + 48);
    nCount %= 10;
    digit[3] = (char)(nCount + 48);
    digit[4] = NULL;
    fout << &digit[0] << endl;
}