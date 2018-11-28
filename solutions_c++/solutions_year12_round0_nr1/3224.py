//
//  main.cpp
//  q1.google.code
//
//  Created by Yuanfeng on 12-04-14.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <queue>
#include <assert.h>

#define floop(i,count) for (int i=0;i<count;i++)
using namespace std;

bool debug = false; //for debugging

char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void process(int caseNum, ifstream &input, ostream &output)
{
    char ch;
    ch = input.get();
    while ( ch != '\n' && !input.eof()) {
        if (ch == ' ') {
            output<<ch;
        } else 
        {
           output<<mapping[ch-97]; 
        }
        ch = input.get();
    }
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
    floop(i, numCase)
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

