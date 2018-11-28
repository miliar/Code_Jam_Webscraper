/*
 * File:   main.cpp
 * Author: Florin
 *
 * Created on September 12, 2009, 6:53 PM
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

long cnt[10];

int number[100];

bool inline ok(unsigned long long n)
{
    int digits[100];
    int idx = 0;

    while(n != 0)
    {
        digits[idx++] = n % 10;
        
        n /= 10;
    }

    long t_cnt[10];

    for(int i = 0; i < 10; i++)
        t_cnt[i] = 0;

    for(int i = 0; i < idx; i++)
        t_cnt[digits[i]]++;

    for(int i = 1; i < 10; i++)
        if(cnt[i] != t_cnt[i])
            return false;

    return true;
}

unsigned long long solve(unsigned long long x)
{
    int digits[100];
    int idx = 0;

    unsigned long long n = x;

    while(n != 0)
    {
        digits[idx++] = n % 10;

        n /= 10;
    }

    for(int i = 0; i < 10; i++)
        cnt[i] = 0;

    for(int i = 0; i < idx; i++)
        cnt[digits[i]]++;

    for(n = x + 1; !ok(n); n++);

    return n;
}

int main(int argc, char** argv)
{
    try
    {
        fstream fin("D:\\codejam\\bsmall.in", ios::in | ios::binary);
        fstream fo("D:\\codejam\\bsmall.out", ios::out | ios::binary);

        long testCasecnt;

        fin>>testCasecnt;

        for(long testCase = 0; testCase < testCasecnt; testCase++)
        {
            cout<<endl<<"#"<<testCase;

            unsigned long long x;
            fin>>x;

            fo<<"Case #"<<(testCase + 1)<<": "<<solve(x)<<endl;
        }

        fin.close();
        fo.close();
    }
    catch(exception e)
    {
        cout<<endl<<"Err: "<<e.what();
    }

    return (EXIT_SUCCESS);
}

