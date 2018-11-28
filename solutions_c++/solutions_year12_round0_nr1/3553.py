/* 
 * File:   A.cpp
 * Author: Ants
 *
 * Created on April 14, 2012, 11:51 AM
 */

#include <cstdlib>
#include <iostream>
#include <string>


using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    const int N = 256;
    char map[N];
    for (int c = 0; c < N; c++) map[c] = c;
    map['a'] = 'y';
    map['b'] = 'h';
    map['c'] = 'e';
    map['d'] = 's';
    map['e'] = 'o';
    map['f'] = 'c';
    map['g'] = 'v';
    map['h'] = 'x';
    map['i'] = 'd';
    map['j'] = 'u';
    map['k'] = 'i';
    map['l'] = 'g';
    map['m'] = 'l';
    map['n'] = 'b';
    map['o'] = 'k';
    map['p'] = 'r';
    map['q'] = 'z';
    map['r'] = 't';
    map['s'] = 'n';
    map['t'] = 'w';
    map['u'] = 'j';
    map['v'] = 'p';
    map['w'] = 'f';
    map['x'] = 'm';
    map['y'] = 'a';
    map['z'] = 'q';
    
    int T;
    string line;
    cin >> T;
    getline(cin, line);
    for (int t = 1; t <= T; t++) {
        getline(cin, line);
        for (int i = 0; i < line.length(); i++) {
            line[i] = map[line[i]];
        }
        cout << "Case #" << t << ": " << line << endl;   
    }
    
    return 0;
}

