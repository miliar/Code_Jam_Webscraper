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

using namespace std;
#define maxN 15
int arr[maxN];
int main(int argc, char** argv) {
    

    int n_testCases = 0;
    cin >> n_testCases;

    for(int i=0; i < n_testCases; ++i) {
        int N;
        cin >> N;

        int input = -1;
        cin >> input;
        int mini = input;
        int sum = input;
        int xori = input;
        
        for(int j=1; j< N; j++) {
            cin >> input;
            mini = min(input, mini);
            sum += input;
            xori ^= input;
        }
        

        cout << "Case #"<< i+1 << ": ";
        if(xori == 0) {
            cout << (sum-mini) << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}

