// round1.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string>
#include <iostream>
#include <boost/regex.hpp>
using namespace std;
int _tmain(void)
{
    int L, D, N;
    cin >> L >> D >>N;

    vector<string> word;
    for(int i = 0; i < D; ++i )
    {
        string iWord;
        cin >> iWord;
        word.push_back(iWord);
    }

    std::vector<string> testCase(N);
    for(int i = 0; i < N; ++i){
        cin >> testCase[i];
    }

    //get the regular expression
    std::vector<string> reg(N);
    for(int i  = 0; i < testCase.size(); ++i){
        reg[i] = testCase[i];
        for(int j = 0; j < testCase[i].length(); ++j){
            if(testCase[i][j] == '('){
                reg[i][j] = '['; 
            }else if(testCase[i][j] == ')'){
                reg[i][j] = ']'; 
            }
        }
    }

    for(int i = 0; i < N; ++i){
        int count = 0;
        //cout << reg[i]<<endl;
        for (int j = 0; j < D; j++) {
            if(boost::regex_match(word[j],  boost::regex(reg[i]))){
                ++count;
            }
        }
        cout << "Case #"<< i+1<<": "<<count<<endl;
    }

	return 0;
}
