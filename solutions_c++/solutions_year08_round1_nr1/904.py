#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

// for size length iterator begin end push_back int char string vector stringstream

#define FOR(i,m,n) for(int i=(m);i<=(int)(n);i++)
#define rep(i,n) FOR(i,0,(n)-1)

using namespace std;

string readln()
{
    string s="";
    char buf[1000];
    cin.getline(buf,1000);
    s=buf;
    return s;
}

int readintln()
{
    stringstream ss(readln());
    int s;
    ss>>s;
    return s;
}

void pvi(vector<int> v,string eoln=" ")
{
    rep(i,v.size())
    {
        cerr << v[i]<<eoln;
    }
    cerr<<"\n";
}

void pvs(vector<string> v,string eoln=" ")
{
    rep(i,v.size())
    {
        cerr << v[i]<<eoln;
    }
    cerr<<"\n";
}

string main_fn(int a1,string s1,string s2)
{
    cerr << s1<<"\nnn " <<s2<<"\n";
    string retval="";
    stringstream ss1(s1);
    stringstream ss2(s2);
    vector<int> v1,v2;
    int a,b;
    while(a1>0)
    {
        a1--;
        ss1 >> a;
        ss2>>b;
        v1.push_back(a);
        v2.push_back(b);
    }
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    long long ans=0;
    rep(i,v1.size())
    {
        ans+=v1[i]*v2[v2.size()-1-i];
        cerr << v1[i] << "*"<<v2[v2.size()-1-i]<<"\n";
    }
    char buf[1000];
    sprintf(buf,"%d",ans);

    return buf;
}

int main()
{
    int N=readintln();
    rep(i,N)
    {
        int a=readintln();
        string s1=readln();
        string s2=readln();
        cout << "Case #"<<i+1<<": "<<main_fn(a,s1,s2)<<"\n";
    }
} 
