#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cstring>
#include<sstream>
#include<fstream>

using namespace std;

char map[26];

int translate()
{
    char st='a';
    map['y'-st]='a';
    map['z'-st]='q';
    map['q'-st]='z';
    map['e'-st]='o';
    string s[3];
    string l[3];
    s[0]="ejpmysljylckdkxveddknmcrejsicpdrysi";
    s[1]="rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd";
    s[2]="dekrkdeoyakwaejtysrreujdrlkgcjv";
    l[0]="ourlanguageisimpossibletounderstand";
    l[1]="therearetwentysixfactorialpossibilities";
    l[2]="soitisokayifyouwanttojustgiveup";
    char c;
    int size;
    for(int k=0;k<3;k++)
    {
        size=s[k].size();
        for(int j=0;j<size;j++)
        {
            c=s[k][j];
            map[c-st]=l[k][j];
        }
    }

}

int main()
{
    ofstream of;
    of.open("ggle.txt");
    translate();
    int t;
    cin>>t;
    string st;
    st="";
    getline(cin,st);
    for(int i=0;i<t;i++)
    {
        getline(cin,st);
        string ans;
        char c;
        int sz=st.size();
        for(int k=0;k<sz;k++)
        {
            c=st[k];
            if(c==' ')
            {
                ans+=c;
            }
            else
            {
                ans+=map[c-'a'];
            }
        }
        of<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    of.close();
    return 0;
}
