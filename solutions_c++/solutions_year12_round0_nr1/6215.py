/* 
 * File:   main.cpp
 * Author: root
 *
 * Created on April 14, 2012, 11:53 AM
 */

#include <cstdlib>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */

void initializeMapping (char* mapping)
{
    mapping['a'] = 'y';
    mapping['b'] = 'h';
    mapping['c'] = 'e';
    mapping['d'] = 's';
    mapping['e'] = 'o';
    mapping['f'] = 'c';
    mapping['g'] = 'v';
    mapping['h'] = 'x';
    mapping['i'] = 'd';
    mapping['j'] = 'u';
    mapping['k'] = 'i';
    mapping['l'] = 'g';
    mapping['m'] = 'l';
    mapping['n'] = 'b';
    mapping['o'] = 'k';
    mapping['p'] = 'r';
    mapping['q'] = 'z';
    mapping['r'] = 't';
    mapping['s'] = 'n';
    mapping['t'] = 'w';
    mapping['u'] = 'j';
    mapping['v'] = 'p';
    mapping['w'] = 'f';
    mapping['x'] = 'm';
    mapping['y'] = 'a';
    mapping['z'] = 'q';
    mapping[' '] = ' ';
}


int main(int argc, char** argv) {
    char mapping[200];
    int numberOfSamples;
    char output[101]; 
    string a;
    char* fileName = strdup(argv[1]);
    ifstream stream;
    stream.open(fileName, ifstream::in);
    initializeMapping(mapping);
    
    getline(stream,a);
    
    numberOfSamples = atoi(a.c_str());
    char input[30][101];
    //cin.ignore();
    for (int i = 0; i < numberOfSamples; i++)
    { 
        getline(stream,a);
        strncpy(input[i],a.c_str(), a.length());
    }
    
    for (int i = 0; i < numberOfSamples; i++)
    {
        for (int j = 0; j < strlen(input[i]); j++)
            output[j] = mapping[input[i][j]];
        output[strlen(input[i])] = '\0'; 
        printf("Case #%d: %s\n", (i+1), output);
    } 
            
    return 0;
}

