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

int B;
int A;
double* backSpace;

void calculate(int currPos, int size,  double* arr, int earliestMistakePos, double currentProbability)
{
    if (currPos==size) {
        for (int n=1; n<size+1; n++) {
            int ear = earliestMistakePos<0?A:earliestMistakePos;
            int one = ((A-n)>ear)?(2*n+2*B+2-A):(2*n+B-A+1);
            double result = one*currentProbability;
            backSpace[n-1]+=result;
        }
    } else
    {
        int currPosMistake = earliestMistakePos<0?currPos:earliestMistakePos;
        
        //if made no mistake
        calculate(currPos+1, size, arr, earliestMistakePos, currentProbability*arr[currPos]);
        
        //if made mistke
        calculate(currPos+1, size, arr, currPosMistake, currentProbability*(1-arr[currPos]));
    }
}

double process(int caseNum, ifstream &input, ostream &output)
{
    input>>A>>B;
    double *arr = new double[A];
    
    double allCorrectProb = 1;
    for (long i =0; i<A; i++) {
        input>>arr[i];
        allCorrectProb*=arr[i];
    }
    double keepTyping = allCorrectProb*(B-A+1)+(1-allCorrectProb)*(2*B-A+2);
    double pressRightAway = B+2;

    backSpace = new double[A];
    calculate(0,A, arr, -1, 1);
    
    double ans = keepTyping;
    ans = pressRightAway<ans?pressRightAway:ans;
    forloop(i, A)
    {
        ans = backSpace[i]<ans?backSpace[i]:ans;
    }
    delete arr;
    delete backSpace;
    
    return ans;
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
            cout<<process(i,input,cout);
            cout<<"\n";
        } else
        {
            output<<"Case #"<<i+1<<": ";
            output<<process(i,input,output);
            output<<"\n";
        }
    }
    input.close();
    output.close();
    return 0;
}

