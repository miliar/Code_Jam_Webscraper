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

void process(int caseNum, ifstream &input, ostream &output)
{
    int N; //number of googler
    int S; //number of suprising
    int p; //min. score
    input>>N>>S>>p;
    int ans=0;
    forloop(i,N)
    {
        int score;
        input>>score;
        
        //handle extreme cases first
        if (p>score)
        {
            continue;
        }
        
        if (p*3 <= score) {
            ans++; //definitely got one that is p
        } else if (p*3-1 <= score)
        {
            ans++;       
        } else if (p*3-2 <= score)
        {
            ans++;  
        }  else if (p*3-3 <= score && S>0) //suprising case
        {
            ans++;
            S--;
        } else if (p*3-4 <= score && S>0) //suprising case
        {
            ans++;
            S--;
        } 
    }
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

