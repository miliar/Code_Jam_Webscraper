#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("a.out");

int main() {
    int T , i , j , k = 1;
    string s;
    char map[5][5];
    fin >> T;
    while(T--) {
        int flag = 0;
        int xcnt , ocnt , tcnt;
        int dotcnt = 0;
        for(i = 1 ; i <= 4 ; i++) {
            fin >> s;
            for(j = 1 ; j <=4 ; j++) {
                map[i][j] = s[j-1];
                if(s[j-1] == '.') dotcnt++;
            }
        }

        for(i = 1 ; i <= 4 ; i++) {
            xcnt = 0 ; ocnt = 0 ; tcnt = 0;
            for(j = 1 ; j <= 4 ; j++) {
                if(map[i][j] == 'X') xcnt++;
                if(map[i][j] == 'O') ocnt++;
                if(map[i][j] == 'T') tcnt++;
            }
            if(xcnt == 4 || (xcnt == 3)&&(tcnt == 1)) {flag = 1; break;}
            if(ocnt == 4 || (ocnt == 3)&&(tcnt == 1)) {flag = -1; break;}
        }
        if(flag == 1) {fout << "Case #" << k++ << ": X won" << endl; continue;}
        if(flag == -1){fout << "Case #" << k++ << ": O won" << endl;continue;}

        for(j = 1 ; j <= 4 ; j++) {
            xcnt = 0 ; ocnt = 0 ; tcnt = 0;
            for(i = 1 ; i <= 4 ; i++) {
                if(map[i][j] == 'X') xcnt++;
                if(map[i][j] == 'O') ocnt++;
                if(map[i][j] == 'T') tcnt++;
            }
            if(xcnt == 4 || (xcnt == 3)&&(tcnt == 1)) {flag = 1; break;}
            if(ocnt == 4 || (ocnt == 3)&&(tcnt == 1)) {flag = -1; break;}
        }
        if(flag == 1) {fout << "Case #" << k++ << ": X won" << endl;continue;}
        if(flag == -1){fout << "Case #" << k++ << ": O won" << endl;continue;}

        xcnt = 0 ; ocnt = 0 ; tcnt = 0;
        for(i = 1 ; i <= 4 ; i++) {
            if(map[i][i] == 'X') xcnt++;
            if(map[i][i] == 'O') ocnt++;
            if(map[i][i] == 'T') tcnt++;
        }
        if(xcnt == 4 || (xcnt == 3)&&(tcnt == 1)) {fout << "Case #" << k++ << ": X won" << endl;continue;}
        if(ocnt == 4 || (ocnt == 3)&&(tcnt == 1)) {fout << "Case #" << k++ << ": O won" << endl;continue;}

        xcnt = 0 ; ocnt = 0 ; tcnt = 0;
        for(i = 1 ; i <= 4 ; i++) {
            if(map[i][5-i] == 'X') xcnt++;
            if(map[i][5-i] == 'O') ocnt++;
            if(map[i][5-i] == 'T') tcnt++;
        }
        if(xcnt == 4 || (xcnt == 3)&&(tcnt == 1)) {fout << "Case #" << k++ << ": X won" << endl;continue;}
        if(ocnt == 4 || (ocnt == 3)&&(tcnt == 1)) {fout << "Case #" << k++ << ": O won" << endl;continue;}

        if(dotcnt > 0) {fout << "Case #" << k++ << ": Game has not completed" << endl;continue;}
        else {fout << "Case #" << k++ << ": Draw" << endl;continue;}
    }
    return 0;
}
