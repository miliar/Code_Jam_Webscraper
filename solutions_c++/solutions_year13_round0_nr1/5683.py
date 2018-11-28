//
//  main.cpp
//  googlecodequalifying1
//
//  Created by Melody Pang on 13/04/2013.
//  Copyright (c) 2013 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{

    ifstream infile("/Users/mellypang/Developer/googlecode/googlecodequalifying1/googlecodequalifying1/input.txt");
    
    if (!infile) {
        cout << "There was a problem opening file "
        << " for reading."
        << endl;
        return 0;
    }
    int nTests;
    char helper;
    infile >> nTests;
    ofstream myfile;
    myfile.open ("/Users/mellypang/Developer/googlecode/googlecodequalifying1/googlecodequalifying1/output.txt");
    for (int k = 0; k < nTests; ++k) {
        vector<vector<int> > results;
        bool FullBoard = true;
        for (int rows = 0; rows < 4; ++rows)
        {
            results.push_back(vector<int>());
            for (int cols = 0; cols < 4; ++cols)
            {
                infile >> helper;
                if ('X' == helper)
                    results[rows].push_back(100);
                if ('O' == helper)
                    results[rows].push_back(-100);
                if ('T' == helper)
                    results[rows].push_back(1);
                if ('.' == helper){
                    results[rows].push_back(0);
                    FullBoard = false;
                }
                
            }
        }
        // now get ten result sums
        vector<int> resultSums(10,0);
        // rows
        for (int i = 0; i < 4 ; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                resultSums[i] += results[i][j];
            }
        }
        // cols
        for (int i = 0; i < 4 ; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                resultSums[i + 4] += results[j][i];
            }
        }
        // diagonal
        resultSums[8] = results[0][0] + results[1][1] + results[2][2] + results[3][3] ;
        resultSums[9] = results[0][3] + results[1][2] + results[2][1] + results[3][0] ;
        
        //for (int i = 0; i < 10; ++i)
            //cout << resultSums[i] << endl;
        
        // if max adds up 301 or 400 then X has won
        int maxValue = *(max_element(resultSums.begin(), resultSums.end()));
        int minValue = *(min_element(resultSums.begin(), resultSums.end()));
        
        if (maxValue == 400 || maxValue == 301)
            myfile << "Case #" << k+1 << ": X won" << endl;
        else if (minValue == -400 || minValue == -299)
            myfile << "Case #" << k+1 << ": O won" << endl;
        else if (FullBoard)
            myfile << "Case #" << k+1 << ": Draw" << endl;
        else
            myfile << "Case #" << k+1 << ": Game has not completed" << endl;        
        
        
        //read blank line for next test case
        //infile >> helper;
                    
    }

}

