//
//  1A.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    char c[128]={0};
    c['a']='y';
    c['b']='h';
    c['c']='e';
    c['d']='s';
    c['e']='o';
    c['f']='c';
    c['g']='v';
    c['h']='x';
    c['i']='d';
    c['j']='u';
    c['k']='i';
    c['l']='g';
    c['m']='l';
    c['n']='b';
    c['o']='k';
    c['p']='r';
    c['q']='z';
    c['r']='t';
    c['s']='n';
    c['t']='w';
    c['u']='j';
    c['v']='p';
    c['w']='f';
    c['x']='m';
    c['y']='a';
    c['z']='q';
    
    int t;
    cin>>t;
    string s;
    getline(cin, s);
    for (int i=0; i<t; i++){
        getline(cin, s);
        for (int j=0; j<s.length(); j++)
            if (s[j]>='a' && s[j]<='z')
                s[j]=c[s[j]];
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
}
