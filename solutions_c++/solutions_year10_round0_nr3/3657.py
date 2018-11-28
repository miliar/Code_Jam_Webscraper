/* 
 * File:   main.cpp
 * Author: tiago
 *
 * Created on May 8, 2010, 1:18 AM
 */

#include <stdlib.h>
#include <iostream>
#include <queue>

using namespace std;

/*
Input

3 --> T = number of test cases. each test case is 2 lines
4 6 4 --> R, k and N groups follow
1 4 2 1 --> g
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3  	
Output

Case #1: 21
Case #2: 100
Case #3: 20

 * 
 */
int main(int argc, char** argv) {
    unsigned int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        unsigned long Total=0;
        unsigned long R;
        unsigned long k;
        unsigned int N;
        queue<unsigned long> Groups;
        cin >> R >> k >> N;
        for(;N>0;N--){
            unsigned long g;
            cin >> g;
            Groups.push(g);
        }
        // para cada R encher Roller
        for(;R>0;R--){
            unsigned long roundMax=0;
            queue<unsigned long> Roller;

            while(!Groups.empty() && roundMax+Groups.front() <= k ){
                Roller.push(Groups.front());
                roundMax+=Groups.front();
                Groups.pop();
            }
            while(!Roller.empty()){
                Groups.push(Roller.front());
                Roller.pop();
            }
            Total += roundMax;
        }
        cout << "Case #" << t << ": " << Total << endl;

    }


    return (EXIT_SUCCESS);
}

