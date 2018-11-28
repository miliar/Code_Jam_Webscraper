//
//  main.cpp
//  CandySplitting
//
//  Created by Wanasit Tanakitrungruang on 5/7/11.
//  Copyright 2011 Chulalongkorn University. All rights reserved.
//

#include <iostream>
#include <vector>

int NUMBER_OF_TESTCASE;
int NUMBER_OF_CANDY;

using namespace std;

void doTestCase(int testNumber)
{
    
    std::cin >> NUMBER_OF_CANDY;
    
    int minCandy = 2000000;
    vector<int> candies;

    int candy;
    for (int i = 0; i<NUMBER_OF_CANDY; i++) {
        
        std::cin >> candy;
        if(minCandy > candy) minCandy = candy;
        
        candies.push_back(candy);
    }
    
    int notEqual = 0;
    int sumValue = 0;
    vector<int>::const_iterator cii;
    for(cii=candies.begin(); cii!=candies.end(); cii++)
    {
        notEqual = notEqual ^ *cii;
        sumValue += *cii;
    }
    
    if(notEqual)
    {
        std::cout <<"Case #" << (testNumber+1) << ": NO" << endl;
        return;
    }
    else{
        int seanCandies = sumValue-minCandy;
        std::cout << "Case #" << (testNumber+1) << ": " << seanCandies << endl;
    }
    
}

int main (int argc, const char * argv[])
{
    
    std::cin >> NUMBER_OF_TESTCASE;
    
    for (int i=0; i<NUMBER_OF_TESTCASE; i++) {
        doTestCase(i);
    }
    
    return 0;
}