#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>

using namespace std;

ifstream f("input.in");
ofstream g("output.out");

#define nmax 5
#define ll long long

char a[nmax][nmax];
string S;

void citeste(){
    //S.clear();
    for(int i=1; i<=4; ++i){
        S.clear(); getline(f, S);
        for(int j=0; j<4; ++j) a[i][j+1] = S[j];//, cout << a[i][j+1] << " ";
        //cout << "\n";
    }
    //cout << "\n";
}

inline int check(){
    for(int i=1; i<=4; ++i){// am pe linie
        int x = 0, o = 0;
        for(int j=1; j<=4; ++j){
            if (a[i][j] == 'O') ++o;
            if (a[i][j] == 'X') ++x;
            if (a[i][j] == 'T') ++o, ++x;
        }
        if (x == 4) return 0;
        if (o == 4) return 1;
    }

    for(int j=1; j<=4; ++j){
        int x = 0, o = 0;
        for(int i=1; i<=4; ++i){
            if (a[i][j] == 'O') ++o;
            if (a[i][j] == 'X') ++x;
            if (a[i][j] == 'T') ++o, ++x;
        }
        if (x == 4) return 0;
        if (o == 4) return 1;
    }

    int x = 0; int o = 0;
    for(int i=1; i<=4; ++i){
        if (a[i][i] == 'O') ++o;
        if (a[i][i] == 'X') ++x;
        if (a[i][i] == 'T') ++o, ++x;
    }
    if (x == 4) return 0;
    if (o == 4) return 1;

    x = 0, o = 0;
    for(int i=1; i<=4; ++i){
        int j = 4 - i + 1;
        if (a[i][j] == 'O') ++o;
        if (a[i][j] == 'X') ++x;
        if (a[i][j] == 'T') ++o, ++x;
    }
    if (x == 4) return 0;
    if (o == 4) return 1;
    for(int i=1; i<=4; ++i) for(int j=1; j<=4; ++j) if (a[i][j] == '.') return 3;
    return 2;
}

void rezolva(){
    int t = 0;
    f >> t;f.get();
    for(int i=1; i<=t; ++i){
        citeste();
        getline(f, S); S.clear();
        int ok = check();
        if (ok == 0){
            g << "Case #" << i << ": " << "X won" << "\n";
        }
        if (ok == 1){
            g << "Case #" << i << ": " << "O won" << "\n";
        }
        if (ok == 2){
            g << "Case #" << i << ": " << "Draw" << "\n";
        }
        if (ok == 3) {
            g << "Case #" << i << ": " << "Game has not completed" << "\n";
        }
    }
}

int main(){
    rezolva();

    f.close();
    g.close();

    return 0;
}

