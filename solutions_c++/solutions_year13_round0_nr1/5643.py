/* 
 * File:   main.cpp
 * Author: SCORPIUS
 *
 * Created on April 14, 2013, 2:01 AM
 */

#include <cstdlib>
#include <string.h>
#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s[4];
        for(int j=0;j<4;j++)
        cin>>s[j];
        char r[4],c[4],d2=s[0][3],d1=s[0][0], rs=0;
        for (int j = 0; j < 4; j++) {
            r[j]=s[j][0];if(r[j]=='T')r[j]=s[j][1];
            c[j]=s[0][j];if(c[j]=='T')c[j]=s[1][j];
        }
        bool b = false;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++) {
                if (s[j][k] == '.') b = true;
                if (c[k] != s[j][k] && s[j][k] != 'T') c[k] = 0;
                if (r[j] != s[j][k] && s[j][k] != 'T') r[j] = 0;
                if (j == k && d1 != s[j][k] && s[j][k] != 'T') d1 = 0;
                if ((j + k) == 3 && d2 != s[j][k] && s[j][k] != 'T') d2 = 0;
            }
        for (int j = 0; j < 4; j++) {
            if (c[j] != 0 && c[j] != '.') {
                rs = c[j];break;
            }else if (r[j] != 0 && r[j] != '.') {
                rs = r[j];break;
            }
        }if (d1 != 0 && d1 != '.') 
                rs = d1;
            else if (d2 != 0 && d2 != '.') 
                rs = d2;
            
        printf("Case #%d: ", i);
        if (rs == 0 && !b) cout << "Draw" << endl;
        else if (rs == 0 && b) cout << "Game has not completed" << endl;
        else cout << rs << " won" << endl;
    }
    return 0;
}

