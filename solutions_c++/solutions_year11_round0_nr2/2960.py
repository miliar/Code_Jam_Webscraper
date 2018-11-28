#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<map>
#define pr pair<char,char>
using namespace std;
map<string,char>ok;
map<pr,int>opp;
string change(string,char);
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int c,d,n;
        scanf("%d",&c);
        string s;
        for(int i=0;i<c;i++)
        {
            cin>>s;
            string h;
            h+=s[0];
            h+=s[1];
            ok[h]=s[2];
            h="";
            h+=s[1];
            h+=s[0];
            ok[h]=s[2];
        }
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            cin>>s;
            opp[pr(s[0],s[1])]=1;
            opp[pr(s[1],s[0])]=1;
        }
        scanf("%d",&n);
        cin>>s;
        string temp;
        string temp1;
        temp=s[0];
        for(int i=1;i<s.length();i++)
        {
                temp=change(temp,s[i]);
        }
        cout<<"Case #"<<k<<": "<<"[";
        for(int i=0;i<temp.length();i++)
        {
            if(i!=temp.length()-1)
            cout<<temp[i]<<", ";
            else
            cout<<temp[i];
        }
        cout<<"]\n";
        ok.clear();
        opp.clear();
    }
    return 0;
}
string change(string s,char g)
{
int l=s.length();
if(l==0)
{
    string ret;
    ret=g;
    return ret;
    //return s;
}
string h1;
h1+=s[l-1];
h1+=g;
if(ok[h1])
{
    string ret;
    for(int i=0;i<=l-2;i++)
    {
        ret+=s[i];
    }
    ret+=ok[h1];
    return ret;
}
for(int i=0;i<l;i++)
{
pr q;
q.first=g;
q.second=s[i];
if(opp[q]==1)
{
    string ret;
    return ret;
}
}
return s+g;
}






