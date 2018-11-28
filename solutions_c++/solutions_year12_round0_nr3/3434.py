//
//  main.cpp
//  q2.google.code
//
//  Created by Yuanfeng on 12-04-14.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <queue>
#include <assert.h>

#define forloop(i,count) for (int i=0;i<count;i++)
using namespace std;

bool debug = false; //for debugging

int processLong(long i, long end)
{
    long originalNum = i;
    int ans = 0;
    long j=i;
    int length = 0;
    while (j/10 != 0) {
        j/=10;
        length++;
    }
    length++;
    int *arr = new int[length*2-1]; //ex: 122 -> 12212
    
    j=i;
    forloop(i, length)
    {
        arr[length-1-i] = (int)j%10;
        j/=10;
    }
    
    j=i/10;
    for (int i = length*2-1-1; i>=length; i--) {
        //now fill the "12" at the end
        arr[i] = (int)j%10;
        j/=10;
    }
    
    int startingIndex = 1;
    long prevAns = 0;
    forloop(i, length-1) //just count number of generating of num
    {
        long newNum = 0;
        forloop(j, length)
        {
            newNum*=10;
            newNum+=arr[startingIndex + j];
        }
        if (newNum > originalNum && newNum<=end && newNum != prevAns) {
            ans++; //!!! 
            prevAns = newNum;
        }
        startingIndex++;
    }
    
    return ans;
}

void process(int caseNum, ifstream &input, ostream &output)
{
    long start;
    long end; 
    input>>start>>end;
    int ans=0;
    if (start>end || end<=11) {
        goto returnAns;
    }
    
    for (long i =start; i<=end; i++) {
        ans += processLong(i, end);
    }
    
returnAns:
    output<<ans;
}

int main (int argc, const char * argv[])
{
    ifstream input;
    input.open("1.txt");
    
    ofstream output;
    output.open("out.txt");
    
    int numCase;
    input>>numCase;
    input.get(); //get rid of \n for the first line
    forloop(i, numCase)
    {
        if (debug) {
            cout<<"Case #"<<i+1<<": ";
            process(i,input,cout);
            cout<<"\n";
        } else
        {
            output<<"Case #"<<i+1<<": ";
            process(i,input,output);
            output<<"\n";
        }
    }
    input.close();
    output.close();
    return 0;
}

