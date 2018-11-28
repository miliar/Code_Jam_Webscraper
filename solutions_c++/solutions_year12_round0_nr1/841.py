#include <cstdio>
#include <string>
#include <fstream>
#include <map>
#include <iostream>
using namespace std;
string fx="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
string x="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string D="abcdefghijklmnopqrstuvwxyz ";
string I="abcdefghijklmnopqrstuvwxyz ";
map<char,char> f;
int main()
{
    f['a']='y';
    f['o']='e';
    f['z']='q';
    for (int i=0;i<x.length();i++)
        f[x[i]]=fx[i];
    char _x,_fx;
    for (int i=0;i<D.length();i++)
        if (f.find(D[i])==f.end())
           _x=D[i];
    for (int i=0;i<I.length();i++)
    {
        bool found=false;
        for (map<char,char>::iterator it=f.begin();it!=f.end();it++)
            if (it->second==I[i]) found=true;
        if (!found) _fx=I[i];
    }
    f[_x]=_fx;
    cout<<f.size()<<endl;
    ifstream cin("i.txt");
    ofstream cout("o.txt");
    int T;
    cin>>T;
    cin.get();
    for (int t=1;t<=T;t++)
    {
        string s;
        getline(cin,s);
        cout<<"Case #"<<t<<": ";
        for (int i=0;i<s.length();i++)
            cout<<f[s[i]];
        cout<<endl;
    }
    while (std::cin.get()!='q'); 
}
