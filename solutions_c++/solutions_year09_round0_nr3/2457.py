/* 
 * File:   main.cpp
 * Author: root
 *
 * Created on September 3, 2009, 12:52 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

bool matches(char* input, unsigned long* s, unsigned int size)
{
    char* pattern = "welcome to code jam";

    //cout<<endl<<s[0];
    //getchar();

    for(int i = 0; i < size; i++)
        if(pattern[i] != input[s[i]])
            return false;

    return true;
}

void count(char* input, unsigned long start, unsigned long* s, int idx, unsigned long* presult)
{
    if(idx == 19)
    {
        if(matches(input, s, 19))
            (*presult)++;
        
        return;
    }

    if(!matches(input, s, idx))
        return;
   
    for(unsigned long i = start; i < strlen(input); i++)
    {
        s[idx] = i;
        count(input, i + 1, s, idx + 1, presult);
    }
}

int main(int argc, char** argv)
{
    fstream fin("/tmp/csmall.in", ios::in | ios::binary);
    fstream fo("/tmp/csmall.out", ios::out | ios::binary);

    unsigned long testCaseCount;
    fin>>testCaseCount;

    char* input = new char[0xFFF];
    
    fin.getline(input, 0xFFF);

    for(unsigned long testCase = 0; testCase < testCaseCount; testCase++)
    {
        fin.getline(input, 0xFFF);

        unsigned long result = 0;
        unsigned long s[19];
        count(input, 0, &s[0], 0, &result);
        cout<<endl<<"INPUT = '"<<input<<"'";
        unsigned long digits[4];
        
        digits[3] = result % 10;
        digits[2] = (result / 10) % 10;
        digits[1] = (result / 100) % 10;
        digits[0] = (result / 1000) % 10;

        fo<<"Case #"<<(testCase + 1)<<": "<<digits[0]<<digits[1]<<digits[2]<<digits[3]<<endl;

        
    }

    delete[] input;

    fin.close();
    fo.close();

    return (EXIT_SUCCESS);
}

