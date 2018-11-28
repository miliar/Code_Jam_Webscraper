#include<iostream>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
int main(){
    int cc=0;
    string x;
    map<char,char>m;
    m['y']='a';
    m['e']='o';
    m['q']='z';
    m['z']='q';
    string s="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string s1="our language is impossible to understand";
    string t="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string t1="there are twenty six factorial possibilities";
    string r="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string r1="so it is okay if you want to just give up";
    for(int i=0;i<s.size();i++)m[s[i]]=s1[i];
    for(int i=0;i<t.size();i++)m[t[i]]=t1[i];
    for(int i=0;i<r.size();i++)m[r[i]]=r1[i];
    cin>>cc;
    getline(cin,x);
    for(int i=1;i<=cc;i++){
        getline(cin,x);
        cout<<"Case #"<<i<<": ";
        for(int i=0;i<x.size();i++)cout<<m[x[i]];
        cout<<endl;

    }
}
