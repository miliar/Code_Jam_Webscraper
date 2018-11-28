/* 
 * File:   main.cpp
 * Author: pchambino
 *
 * Created on May 8, 2010, 9:31 PM
 */

#include <iostream>

using namespace std;
/*
 * 
 */
int main() {

    int t, n, k, x;

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n >> k;

        // calculates snappes to loop
        x = 1;
        for (int j = 0; j < n; j++) {
            x = (x << 1);
        }

        // check if it is ON or OFF
        cout << "Case #" << (i+1) << ": " << (((k+1) % x) == 0 ? "ON" : "OFF") << endl;
    }

    return 0;
}

