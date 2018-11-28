#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>

using namespace std;
char mapping[26];

int translate(string stg,int no)
{
    char st='a';
    mapping['y'-st]='a';
    mapping['q'-st]='z';
    mapping['e'-st]='o';
    mapping['z'-st]='q';
    string s[3];
    s[0]="ejpmysljylckdkxveddknmcrejsicpdrysi";
    s[1]="rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd";
    s[2]="dekrkdeoyakwaejtysrreujdrlkgcjv";
    string l[3];
    l[0]="ourlanguageisimpossibletounderstand";
    l[1]="therearetwentysixfactorialpossibilities";
    l[2]="soitisokayifyouwanttojustgiveup";
    int sz;
    for(int i=0;i<3;i++)
    {
            sz=s[i].size();
            for(int j=0;j<sz;j++)
            {
                    mapping[s[i][j]-st]=l[i][j];
            }
    }
    int size=stg.size();
    string ans;
    for(int k=0;k<size;k++)
    {
            char c=stg[k];
            if(c==' ')
            {
                    ans+=c;
            }
            else
            {
                ans+=mapping[c-st];
            }
    }
    char t;
    /*for(int l=0;l<26;l++)
    {
            
            t=l+'a';
            cout<<t<<": "<<mapping[l]<<endl;
    }*/
    ofstream my;
    
    
    cout<<"Case #"<<no + 1<<": "<<ans<<endl;
   // my<<"Case #"<<no+1<<": "<<ans<<endl;
   // my.close();
}

int main()
{
    freopen("C:\\Users\\Deval Agrahari\\Downloads\\A-small-attempt1.in", "r", stdin);
        freopen("C:\\Users\\Deval Agrahari\\Downloads\\A-small-attempt1.out", "w", stdout);
    int t;
    cin>>t;
    string str;
    str="";
    getline(cin,str);
    for(int i=0;i<t;i++)
    {
           getline(cin,str);
           translate(str,i);
    }
    getchar();
    getchar();
    return 0;
} 
