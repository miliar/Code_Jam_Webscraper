/* 
 * File:   main.cpp
 * Author: asaroha
 *
 * Created on April 14, 2012, 9:16 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;



void parsefile(map<char,char> &lookUp){
    ifstream file;
    file.open("A-small-attempt0.in",ios::in);
    ofstream o_file;
    o_file.open("output.txt",ios::out);
    int t, count = 1;
    string line;
    string o_line;
    string::iterator it;
    while (file.good()) {
        getline(file,line);
        t = atoi(line.c_str());
        cout<<t<<"\n";
        while (count <= t) {
            o_file<<"Case #"<<count<<": ";
            getline(file,line);
            o_line = "";
            for(it = line.begin(); it < line.end(); it++){
                o_line += lookUp[*it];
            }
            o_file<<o_line<<"\n";
            count ++;
        }
    }
    file.close();
    o_file.close();
};
int main(int argc, char** argv) {
    map <char, char> lookUp;
    lookUp['a'] = 'y';
    lookUp['b'] = 'h';
    lookUp['c'] = 'e';
    lookUp['d'] = 's';
    lookUp['e'] = 'o';
    lookUp['f'] = 'c';
    lookUp['g'] = 'v';
    lookUp['h'] = 'x';
    lookUp['i'] = 'd';
    lookUp['j'] = 'u';
    lookUp['k'] = 'i';
    lookUp['l'] = 'g';
    lookUp['m'] = 'l';
    lookUp['n'] = 'b';
    lookUp['o'] = 'k';
    lookUp['p'] = 'r';
    lookUp['q'] = 'z';
    lookUp['r'] = 't';
    lookUp['s'] = 'n';
    lookUp['t'] = 'w';
    lookUp['u'] = 'j';
    lookUp['v'] = 'p';
    lookUp['w'] = 'f';
    lookUp['x'] = 'm';
    lookUp['y'] = 'a';
    lookUp['z'] = 'q';
    lookUp[' '] = ' ';

    parsefile(lookUp);
    return 0;
}

