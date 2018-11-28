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
#include <set>
#include <math.h>
using namespace std;

/*
 *
 */
int main(int argc, char** argv) {
    int T,N;
    cin >> T;
    vector<int> values;
    int maxSetValue = 0;
    vector<int> P, S;
    int Petric=-1, Sean=-1;
    for(int index = 1; index <= T ;index++)
    {
        P.clear();
        S.clear();
        cin >> N;
        maxSetValue = (int)pow(2,N)-1;
        //cout << "maxSetValue: " <<maxSetValue << endl;
        values.clear();
        for(int i=0;i<N;i++){
            int value;
            cin >> value;
            values.push_back(value);
        }
            
        int maxXOR = -1;
        int maxSum = -1;

        for(int i=1;i<maxSetValue-1;i++){


            P.clear();
            S.clear();
            int v = i;
            for(int j=N-1;j>=0;j--){
                if(v%2 == 1)
                    P.push_back(values[j]);
                else
                    S.push_back(values[j]);
                v /= 2;
            }

           /* cout << "\nP = ";
            for(int j=0;j<P.size();j++)
                cout << P[j];
            cout << "\nS = ";
            for(int j=0;j<S.size();j++)
                cout << S[j];
                */

            int pXOR = 0;
            int sXOR = 0;

            int sSum = 0;
            for(int j=0;j<P.size();j++)
                pXOR ^= P[j];

            for(int j=0;j<S.size();j++){
                sXOR ^= S[j];
                sSum += S[j];
            }

            if(pXOR == sXOR && sSum > maxSum) {
                //cout << "\nFound!\n";
                maxXOR = sXOR;
                maxSum = sSum;
            }
        }
        cout << "Case #" << index << ": ";
        if(maxXOR == -1)
            cout << "NO" << endl;
        else
            cout << maxSum << endl;
    }
    return 0;
}

