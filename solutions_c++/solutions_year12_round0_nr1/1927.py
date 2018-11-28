//
//  main.cpp
//  A
//
//  Created by Peter Vajda on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream imap("map.txt");
    if(!imap) {cout << "no file"; return 0;}
    char map[256];
    int T;
    imap >> T;
    imap.ignore(); 
    for(int i=0;i<T;i++){
        string s,t;
        getline(imap,s);
        getline(imap,t);
        for(int j=0; j<s.length(); j++){
            map[s[j]] = t[j];
        }
    }
    imap.close();
    
    ifstream input("input.txt");
    ofstream output("output.txt");
    input >> T;
    input.ignore();
    cout << endl << T << endl;
    for(int i=0;i<T;i++){
        string s;
        getline(input,s);
        output << "Case #" << i+1 << ": ";
        for(int j=0; j<s.length(); j++){
            output << map[s[j]];
        }
        output << endl;
    }
    input.close();
    output.close();
    
    return 0;
}

