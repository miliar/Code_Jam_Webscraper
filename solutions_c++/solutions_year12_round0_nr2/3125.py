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
int solve(vector<int> vect, int p, int supr);
int solve(vector<int> vect, int p, int supr){
    if (p==1 || p ==0 || p ==2)
        cout<<endl;
    int suprise_border=max(3 * p - 2, p);
    int res=0;
    int supr_num=0;
    int suprise_lower_border = max(3 * p -4, p);
    for (int i=0;i<vect.size();++i){
        if (vect[i]>=suprise_border)
            ++res;
        else{
            if (vect[i]>=suprise_lower_border)
                ++supr_num;
        }
    }
    res = supr_num > supr? res+supr:res+supr_num;
    return res;
}

int main (int argc, const char * argv[])
{
    fstream myfile;
    
    myfile.open("B-large.in");
    vector <string> vec;
    string k;
    getline(myfile, k);
    
    fstream zout;
    zout.open("out.txt");
    int case_num=1;
    for (int i=0;i<atoi(k.c_str());++i){
        string str;
        getline(myfile, str);
        istringstream iss(str);
        cout<<str<<endl;
        int num_googlers;
        int supr;
        int p;
        vector <int> vect;
        iss>>num_googlers;
        iss>>supr;
        iss>>p;
        for (int i=0;i<num_googlers;++i){
            int tmp;
            iss>>tmp;
            vect.push_back(tmp);
        }
        zout<<"Case #"<<case_num<<": "<<solve(vect, p, supr)<<endl;
        //cout<<"Case #"<<case_num<<": "<<solve(vect, p, supr)<<endl;
        cout<<endl;
        ++case_num;
    }
    myfile.close();
    zout.close();
    return 0;
}

