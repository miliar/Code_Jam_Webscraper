#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
using namespace std;
char mapping[1000];
int main()
{
    string X[3];
    string Y[3];
    X[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    Y[0]="our language is impossible to understand";
    X[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    Y[1]="there are twenty six factorial possibilities";
    X[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    Y[2]="so it is okay if you want to just give up";
    for(int i=0;i<1000;i++)
        mapping[i]='#';
    for(int i=0;i<3;i++)
        for(int j=0;j<X[i].size();j++)
            mapping[X[i][j]]=Y[i][j];
    mapping['y']='a';
    mapping['e']='o';
    mapping['q']='z';
    mapping['z']='q';
    int T=0;
    string Ts;
    getline(cin, Ts);
    for(int i=0;i<Ts.size();i++)
        T=T*10+Ts[i]-'0';
    for(int t=1;t<=T;t++)
    {
        string X;
        getline(cin, X);
        for(int j=0;j<X.size();j++)
            X[j]=mapping[X[j]];
        cout << "Case #" << t << ": " << X << endl;

    }
}