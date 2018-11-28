#include<iostream>
#include<map>
#include<string>
#include<cstdlib>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

    map<char, char> mapcc;
    string sin, sout;
    string si, so;
    int t;

    sin="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    sout="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

    for(int i=0;i<sin.length();i++)
    {
        if(mapcc.find(sin[i])==mapcc.end())mapcc[sin[i]]=sout[i];
    }
    mapcc['z']='q';
    mapcc['q']='z';

    cin>>t;
    getline(cin, si);
    for(int idx=0;idx<t;idx++)
    {
        getline(cin, si);
        so="";
        for(int i=0;i<si.length();i++)
        {
            if(si[i]!=' ')
            so.append(1, mapcc[si[i]]);
            else so.append(1, ' ');
        }
        cout<<"Case #"<<idx+1<<": "<<so<<endl;
    }

    return 0;
}
