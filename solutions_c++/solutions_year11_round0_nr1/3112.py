/* 
 * File:   main.cpp
 * Author: Sagar
 *
 * Created on May 7, 2011, 11:22 AM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    vector<pair<char,int> > seq;

    int N;
    char c;
    int num;
    for(int index = 1; index <= T ;index++)
    {
        seq.clear();
        
        cin >> N;
        for(int i=0;i<N;i++){
            cin >> c;
            cin >> num;
            seq.push_back(make_pair<char,int>(c,num));
        }

        int oTime=0, bTime=0, totalTime=0, incriment=0;
        int i=0;
        int pos_O = 1, pos_B = 1;
        int steps = 0;

        for(int i=0;i<seq.size();i++)
        {
            if(seq[i].first == 'O')
            {
                steps = abs(seq[i].second - pos_O);

                if(steps > oTime)
                    incriment = (steps - oTime) + 1;
                else
                    incriment = 1;
                totalTime += incriment;
                bTime += incriment;
                oTime = 0;
                pos_O = seq[i].second;
            }
            else if(seq[i].first == 'B')
            {
                steps = abs(seq[i].second - pos_B);
                if(steps > bTime)
                    incriment = (steps - bTime) + 1;
                else
                    incriment = 1;
                totalTime += incriment;
                oTime += incriment;
                bTime = 0;
                pos_B = seq[i].second;
            }
        }

        cout << "Case #" << index << ": " << totalTime << endl;
    }
    return 0;
}


