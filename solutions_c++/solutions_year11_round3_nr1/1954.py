/* 
 * File:   main.cpp
 * Author: sharad
 *
 * Created on 13 February, 2011, 2:47 PM
 */

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>

using namespace std;

int main(int argc, char** argv) {
    int n_testCases = 0;
    cin >> n_testCases;
    char arr[] = {'/','\\','\\','/'};
    for(int i=0; i < n_testCases; ++i) {
        int N,M;

        cin >> N;
        cin >> M;

        char *oWPArr = new char[N*M];
        
        for(int j=0; j< N*M; j++) {
            cin >> oWPArr[j];
        }

        bool bImpossible = false;
        for(int j=0; j < N*M; j++) {
            if(oWPArr[j] == '#') {
                if(j+M+1 >= N*M) {
                    bImpossible = true;
                    break;
                }
                oWPArr[j] = arr[0];
                if(oWPArr[j+1] != '#') {
                    bImpossible = true;
                } else {
                    oWPArr[j+1] = arr[1];
                }
                if(oWPArr[j+M] != '#') {
                    bImpossible = true;
                } else {
                    oWPArr[j+M] = arr[2];
                }
                if(oWPArr[j+M+1] != '#') {
                    bImpossible = true;
                } else {
                    oWPArr[j+M+1] = arr[3];
                }

            }
        }
        cout << "Case #" << (i+1) << ":" << endl;
        if(bImpossible) {
            cout << "Impossible" << endl;
        } else {
            for(int j=0; j< N*M; j++) {
                cout << oWPArr[j];
                if((j+1)%M == 0) {
                    cout << endl;
                }
                
            }
            
        }
        
        delete []oWPArr;

    }

    return 0;
}

