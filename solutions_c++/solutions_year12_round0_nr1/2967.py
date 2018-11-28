/* 
 * File:   main.cpp
 * Author: sajtos
 *
 * Created on April 14, 2012, 10:15 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

string read(ifstream& file)
{
    string line;
    getline(file, line);
    return line;
}

void conv(string& s, char*& tabl)
{
    for(int i = 0; i<s.length(); i++)
    {
        s[i] = tabl[s[i]];
    }
}
/*
 * 
 */
int main(int argc, char** argv)
{
    char* tabl = new char[128];
    
    tabl[' '] = ' ';
    tabl['a'] = 'y';
    tabl['b'] = 'h';
    tabl['c'] = 'e';
    tabl['d'] = 's';
    tabl['e'] = 'o';
    tabl['f'] = 'c';
    tabl['g'] = 'v';
    tabl['h'] = 'x';
    tabl['i'] = 'd';
    tabl['j'] = 'u';
    tabl['k'] = 'i';
    tabl['l'] = 'g';
    tabl['m'] = 'l';
    tabl['n'] = 'b';
    tabl['o'] = 'k';
    tabl['p'] = 'r';
    tabl['q'] = 'z';
    tabl['r'] = 't';
    tabl['s'] = 'n';
    tabl['t'] = 'w';
    tabl['u'] = 'j';
    tabl['v'] = 'p';
    tabl['w'] = 'f';
    tabl['x'] = 'm';
    tabl['y'] = 'a';
    tabl['z'] = 'q';
    
    ifstream file;
    ofstream ofile;
    
    string path = argv[0];
    path += ".in";
    file.open(path.c_str());
    
    path = argv[0];
    path += ".out";
    ofile.open(path.c_str(), ios::trunc);
    
    int n = atoi(read(file).c_str());
    
    for(int i = 0; i<n; i++)
    {
        string cas = read(file);
        conv(cas, tabl);
    
        ofile << "Case #" << i+1 << ": " << cas << endl;
    }
    
    file.close();
    return 0;
}

