#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
using namespace std;

map<string,string> R;
set<string> S;

string replace(string a,char ad)
{
    if(a.size()==0)return a+ad;
    string t = "";
    t+=a[a.size()-1];
    t+=ad;
    if(R.count(t)>0)
        return replace(a.substr(0,a.size()-1),R[t][0]);
    return a+ad;
}
string clr(string a)
{
    for(int j = 0; j < a.size()-1 ; ++j)
    {
        string temp = "";
        temp += a[j];
        temp += a[a.size()-1];
        if(S.count(temp)>0)
            return "";
    }
    return a;
}
int main(int argc, char** argv) 
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TC;
    cin>>TC;
    for(int tc = 1; tc<=TC;++tc)
    {
        R = map<string,string>();
        S = set<string>();
        int C;
        cin>>C;
        for(int i = 0; i< C; ++i)
        {
            string t;cin>>t;
            R[t.substr(0,2)] = t.substr(2);
            swap(t[0],t[1]);
            R[t.substr(0,2)] = t.substr(2);
        }
        int D;
        cin>>D;
        for(int i = 0; i< D; ++i)
        {
            string t;cin>>t;
            S.insert(t);
            swap(t[0],t[1]);
            S.insert(t);
        }
        int N;
        cin>>N;
        string STR;cin>>STR;
        string act="";
        for(int i = 0; i < STR.size(); ++i)
        {
            act = replace(act,STR[i]);
            act = clr(act);
        }
        cout<<"Case #"<<tc<<": ";
        cout<<"[";
        for(int i = 0; i < act.size(); ++i)
            if(i==0)cout<<act[i];
            else cout<<", "<<act[i];
        cout<<"]"<<endl;
    }
    return 0;
}



/* 
 * File:   B.cpp
 * Author: Carlos
 *
 * Created on May 6, 2011, 11:41 PM
 */
