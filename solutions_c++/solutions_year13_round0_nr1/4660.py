//
//  main.cpp
//  q1
//
//  Created by zhou on 13-4-12.
//  Copyright (c) 2013年 zhou. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int f[128];
ifstream in("in.txt");
ofstream ou("out.txt");

int check(string &s){
    f['X']=0;
    f['T']=0;
    f['O']=0;
    for(int i=0;i<4;i++)
        f[s[i]]++;
    if((f['T']==1&&f['X']==3)||f['X']==4)return 1;
    if((f['T']==1&&f['O']==3)||f['O']==4)return 2;
    return 0;
}
int test(){
    string s[4];
    memset(f, 0, sizeof(f));
    for(int i=0;i<4;i++)
        in>>s[i];
    int flag;
    string ms;
    for(int i=0;i<4;i++){
        flag=check(s[i]);
        if (flag)return flag;
        }
    for(int i=0;i<4;i++){
        ms="";
        ms=ms+s[0][i]+s[1][i]+s[2][i]+s[3][i];
        flag=check(ms);
        if (flag)return flag;
    }
        ms="";
        ms=ms+s[0][0]+s[1][1]+s[2][2]+s[3][3];
        flag=check(ms);
        if (flag)return flag;
        ms="";
        ms=ms+s[0][3]+s[1][2]+s[2][1]+s[3][0];
        flag=check(ms);
        if (flag)return flag;
    if (f['.'])
        return 3;
    else
        return 0;
    
}
int main(int argc, const char * argv[])
{
    int tc;
    in>>tc;
    string out[4]={"Draw\n","X won\n","O won\n","Game has not completed\n"
    };
    for(int t=0;t<tc;t++){
        ou<<"Case #"<<t+1<<": "<<out[test()];
    // insert code here...
    }
    return 0;
}

