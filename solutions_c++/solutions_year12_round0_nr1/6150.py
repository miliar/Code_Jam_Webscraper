/* 
 * File:   main.cpp
 * Author: pol
 *
 * Created on April 14, 2012, 11:04 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <functional>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    map<char, char> a;
    a['a'] = 'y';
    a['e'] = 'o';
    a['i'] = 'd';
    a['o'] = 'k';
    a['u'] = 'j';
    a['b'] = 'h';
    a['c'] = 'e';
    a['d'] = 's';
    a['f'] = 'c';
    a['g'] = 'v';
    a['h'] = 'x';
    a['j'] = 'u';
    a['k'] = 'i';
    a['l'] = 'g';
    a['m'] = 'l';
    a['n'] = 'b';
    a['p'] = 'r';
    a['q'] = 'z';
    a['r'] = 't';
    a['s'] = 'n';
    a['t'] = 'w';
    a['v'] = 'p';
    a['w'] = 'f';
    a['x'] = 'm';
    a['y'] = 'a';
    a['z'] = 'q';
    a[' '] = ' ';
    int n;
    in >> n;
    string s;
    char c;
    getline(in, s);
    for (int i = 0; i < n; i++) {
        std::getline(in, s);
        out << "Case #" << i + 1 << ": ";
        for (int i = 0; i < s.length(); i++) {
            out << a[s[i]];
        }
        out << endl;
    }



    return 0;
}

