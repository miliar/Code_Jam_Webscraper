//
//  SpeakingInTongues.cpp
//  Programs
//
//  Created by Shivendra Dayal on 14/04/12.
//  Copyright (c) 2012 sdayal@gmail.com. All rights reserved.
//

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<char,char> code;
    code['y'] = 'a';
    code['e'] = 'o';
    code['q'] = 'z';
    code['z'] = 'q';
    
    string inputString =   "ejp mysljylc kd kxveddknmc re jsicpdrysi ";
    inputString += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd " +
    inputString += "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string outputString =  "our language is impossible to understand " ;
    outputString += "there are twenty six factorial possibilities " +
    outputString += "so it is okay if you want to just give up";
    
    for (int i=0; i<inputString.length(); i++) {
        code[inputString[i]] = outputString[i];
    }
    
    int T;
    cin>>T;
    string s;
    getline(cin, s);
    for (int t = 1; t <= T; t++) {
        getline(cin, s);
        cout << "Case #" << t << ": " ;
        for (int i=0; i<s.length(); i++) {
            cout << code[s[i]];
        }
        cout << endl;
    }

}