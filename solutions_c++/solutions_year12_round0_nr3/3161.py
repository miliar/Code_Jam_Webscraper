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
#include "sstream"



using namespace std;
bool isRotation(string s1, string s2);
bool isRotation(string s1, string s2){
    if (s1.size() == 1)
        return false;
    string s2twice = s2+s2;
    return string::npos != s2twice.find(s1);
}

int solve(int a,int b);
int solve(int a,int b){
    if (a == 1)
        cout<<endl;
    int res=0;
    for (int i=a;i<b;++i){
        for (int k=i+1;k<=b;++k){
            std::stringstream str;
            str << i;
            std::stringstream sstr;
            sstr << k;
            string str1 = str.str();
            string str2 = sstr.str();
            std::stringstream out1;
            out1 << k;
            if (isRotation(str1,str2))
                ++res;
        }
    }
    return res;
}
int main (int argc, const char * argv[])
{
    fstream myfile;
    
    myfile.open("C-small-attempt2.in");
    
    string k;
    getline(myfile, k);
    
    fstream zout;
    zout.open("out.txt");
    int case_num=1;
    int a;
    int b;
    cout<<k;
    for (int i=0;i<atoi(k.c_str());++i){
        string str;
        getline(myfile, str);
        istringstream iss(str);
        cout<<str<<endl;
        vector <int> vect;
        iss>>a;
        iss>>b;
        zout<<"Case #"<<case_num<<": "<<solve(a,b)<<endl;
        //cout<<"Case #"<<case_num<<": "<<solve(a,b)<<endl;
        //cout<<endl;
        ++case_num;
    }
    myfile.close();
    
    zout.close();
    return 0;
}

