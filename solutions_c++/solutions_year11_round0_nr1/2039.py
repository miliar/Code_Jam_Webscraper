/* 
 * File:   p1main.cpp
 * Author: snehasish
 *
 * Created on May 7, 2011, 6:58 AM
 */

#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <iostream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        int C;
        cin >> C;
        unsigned long long int totTime=0L;
        
        map<char,unsigned long long int> time;
        map<char,int> pos;
        time['O']=0;
        time['B']=0;
        pos['O']=1;
        pos['B']=1;
        while(C--){
            char col;
            int dpos;
            cin>>col;
            cin>>dpos;
            

            int rtime = time[col] + abs(pos[col] - dpos) + 1;
            if (rtime > totTime) {
                totTime = (unsigned long long )rtime;
            } else {
                totTime += 1L;
            }
            pos[col] = dpos;
            time[col] = totTime;

        }
        cout << "Case #" << i << ": " << totTime << endl;
    }

    return 0;
}

