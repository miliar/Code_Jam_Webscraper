/* 
 * File:   main.cpp
 * Author: NQH
 * Problem B. Dancing with the Googlers
 * Created on April 14, 2012, 2:42 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

#define MAXN 101

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream fin ("B-large.in");
    ofstream fout ("probb.out");
    int nt, t;
    int n, s, p, cnt;
    int score[MAXN];
    int i;
    int best1, best2;
    fin >> nt;
    for (t=1; t<=nt; t++) {
        // Read input
        fin >> n >> s >> p;
        for (i=0; i<n; i++) 
            fin >> score[i];
        // Process
        cnt = 0;
        for (i=0; i<n; i++) {
            switch (score[i]%3) {
                case 0: 
                    best1 = score[i]/3;
                    best2 = (best1>0) ? best1+1:best1;
                    break;
                case 1: 
                    best1 = score[i]/3 + 1;
                    best2 = best1;
                    break;
                case 2: 
                    best1 = score[i]/3 + 1;
                    best2 = best1+1;
                    break;
                default: 
                    best1 = 0;
                    best2 = 0;
            }
            if (best1>=p) 
                cnt++;
            else if (best2>=p && s>0) {
                cnt++;
                s--;
            }
        }
        // Write output
        fout << "Case #" << t << ": " << cnt << '\n';
    }
    return 0;
}

