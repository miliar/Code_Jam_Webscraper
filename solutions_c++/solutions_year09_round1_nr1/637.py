/* 
 * File:   main.cpp
 * Author: Florin
 *
 * Created on September 12, 2009, 3:58 AM
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

class HappyFinder
{
public:
    long long* bases;
    long baseCount;

    HappyFinder(fstream& fin)
    {
        char* line = new char[0xFFFF];
        fin.getline(line, 0xFFFF);

        baseCount = 1;

        for(long i = 0; i < strlen(line); i++)
            if(line[i] == ' ')
                baseCount++;

        bases = new long long[baseCount];

        istringstream s(line);

        for(long i = 0; i < baseCount; i++)
            s>>bases[i];

        //for(long i = 0; i < baseCount; i++)
        //    cout<<endl<<bases[i];

        delete line;
    }

    long long getDigitSqrt(long long number, long long base)
    {
        long long result = 0;

        while(number != 0)
        {
            result += (number % base) * (number % base);

            number /= base;
        }

        return result;
    }

    bool isVisited(long long* visited, long visitedCount, long long n)
    {
        for(long i = 0; i < visitedCount; i++)
            if(visited[i] == n)
                return true;

        return false;
    }

    bool isHappy(long long number, long long base)
    {

        long visitedCount = 0;
        long visitedSize = 4 * sizeof(long long);
        long long* visited = (long long*)malloc(visitedSize);

        long long n = number;
        
        while(n != 1)
        {
            n = getDigitSqrt(n, base);

            //cout<<endl<<" ? "<<number<<" in "<<base<<" ~ "<<n;

            if(isVisited(visited, visitedCount, n))
                return false;

            if((visitedCount  + 1) * sizeof(long long) > visitedSize)
            {
                visitedSize *= 2;

                visited = (long long*)realloc(visited, visitedSize);
            }

            visited[visitedCount++] = n;
        }

        if(n == 1)
            return true;

        free(visited);

        return false;
    }

    bool isHappyInAllBases(long long number)
    {
        for(long i = 0; i < baseCount; i++)
            if(!isHappy(number, bases[i]))
                return false;

        return true;
    }

    long long getSmallestHappyNumber()
    {
        long long number = 2;

        while(!isHappyInAllBases(number)){//cout<<endl<<"@"<<number;
            number++;}

        return number;
    }

    ~HappyFinder()
    {
        delete[] bases;
    }
};

int main(int argc, char** argv)
{

    fstream fin("D:\\codejam\\asmall.in", ios::in | ios::binary);
    fstream fo("D:\\codejam\\asmall.out", ios::out | ios::binary);

    long testCaseCount;
    
    fin>>testCaseCount;
    char tmp[0xF];
    fin.getline(tmp, 0xF);

    for(long testCase = 0; testCase < testCaseCount; testCase++)
    {
        HappyFinder hf(fin);

        fo<<"Case #"<<(testCase + 1)<<": "<<hf.getSmallestHappyNumber()<<endl;
        //cout<<endl<<hf.isHappy(91, 9);
        //getchar();
    }

    fin.close();
    fo.close();

    return (EXIT_SUCCESS);
}

