//
//  main.cpp
//  gcj
//
//  Created by Kirill on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>

using namespace std;

int main (int argc, const char * argv[])
{
    map <char, char> test;
    vector<string> vect;
        vector<string> vect1;
    vect.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    vect.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    vect.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    vect1.push_back("our language is impossible to understand");
    vect1.push_back("there are twenty six factorial possibilities");
    vect1.push_back("so it is okay if you want to just give up");
    test['z'] = 'q';
    test['q'] = 'z';
    for (int i=0;i<vect.size();++i){
        for (int j=0;j<vect[i].size();++j){
            if (!test[vect[i][j]]){
                test[vect[i][j]] = vect1[i][j];
            }
        }
    }
    
    fstream myfile;
    
    myfile.open("A-small-attempt1.in");
    vector <string> vec;
    int k;
    myfile>>k;
    for (int i=0;i<k+1;++i){
        string str;
        getline(myfile, str);
        vec.push_back(str);
    }
    fstream zout;
    zout.open("out.txt");
    int p=1;
    for (int i=0;i<vec.size();++i){
        string str = vec[i];
        if (str.size()==0)
            continue;
        for (int i=0;i<str.size()+1;++i)
            str[i] = test[str[i]];
        zout<<"Case #"<<p<<": "<<str<<endl;
        ++p;
    }
    myfile.close();
    zout.close();
    return 0;
}

