//
//  main.cpp
//  Speaking in Tongues
//
//  Created by Hon-ming Chen on 4/13/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <map>
using namespace std;

int main(int argc, const char * argv[])
{
    string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string str2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    const char *charArr1 = str1.c_str();
    const char *charArr2 = str2.c_str();
    
    map<char,char> charMap;
    map<char,char>::iterator it;
    int i = 0;
    while (charArr1[i]) {
        
        if (charArr1[i] == ' ') {
            i++;
            continue;
        }
        
        it = charMap.find(charArr1[i]);
        if (it == charMap.end()) {
            charMap[charArr1[i]] = charArr2[i];
        }
        i++;
    }
    
    string mapKeys;
    string mapValues;
    charMap['q'] = 'z';
    charMap['z'] = 'q';
    charMap[' '] = ' ';
    it = charMap.begin();
    for (; it != charMap.end(); it++) {
        mapKeys += it->first;
        mapValues += it->second;
    }
    cout << mapKeys << endl;
    cout << mapValues << endl;
    
    cout << "Size of charMap: " << charMap.size() << endl << endl;
    
    // Open input file
    ifstream fin("/Users/hmchen/Developer/CS144/CodeJam_2012/Speaking in Tongues/input.txt");
    
    if (fin.is_open()) {
        cout << "File is open" << endl;
    } else {
        cout << "File did not open" << endl;
        return 1;
    }
    
    // Open ouput file
    ofstream fout("/Users/hmchen/Developer/CS144/CodeJam_2012/Speaking in Tongues/output.txt");
    
    string input, output;
    // Read number of cases
    int cases;
    fin >> cases;
    getline(fin,input);
    
    for (int i = 0; i < cases; i++) {
        output = "";
        getline(fin, input);
        const char *charInput = input.c_str();
        
        int j = 0;
        while (charInput[j]) {
            output += charMap[charInput[j]];
            j++;
        }
        fout << "Case #" << i+1 << ": " << output << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}

