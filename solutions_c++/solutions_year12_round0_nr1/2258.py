//
//  main.c
//  codejam2012
//
//  Created by Петро Бойчук on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[])
{
    
    string in  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    
    map <char, char> m;
    
    m['z'] = 'q';
    m['q'] = 'z';
    m[' '] = ' ';
    
    for (int i=0; i < in.length(); i++) {
        m[in[i]] = out[i];
    }
    
//    for(int i=0; i<26; i++) {
//        cout << (char)('a' + i) << " " << (char)m['a'+ i] << endl;
//    }
    
    
    ifstream inf("A-small-attempt1.in");
    freopen("out.txt", "w", stdout);
    string ss;
    int n;
    inf >> n; 
    getline(inf, ss);
    for (int line = 0; line < n; line++) {
        getline(inf, ss);
        cout <<"Case #" << line+1 << ": ";
        for (int i=0; i<ss.length(); i++) {
            cout <<  m[ss[i]];
        }
        cout << endl;
    }
    
    
    
    return 0;
}

