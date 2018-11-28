#include <iostream>
#include <string.h>
#include <map>
#include <stdio.h>
using namespace std;

map <char, char> genClave ()
{
    map <char, char> res;
    res.clear();
    string cad1="ejpmysljylckdkxveddknmcrejsicpdrysi";
    string cad2="rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd";
    string cad3="dekrkdeoyakwaejtysrreujdrlkgcjv";
    string res1="ourlanguageisimpossibletounderstand";
    string res2="therearetwentysixfactorialpossibilities";
    string res3="soitisokayifyouwanttojustgiveup";
    for (int c=0; c<cad1.length(); c++)
    {
        res[cad1[c]]=res1[c];
    }
    for (int c=0; c<cad2.length(); c++)
    {
        res[cad2[c]]=res2[c];
    }
    for (int c=0; c<cad3.length(); c++)
    {
        res[cad3[c]]=res3[c];
    }
    res['q']='z';
    res['z']='q';
    res[' ']=' ';
    return res;
}

int main()
{
    int t;
    cin>>t;
    map <char, char> clave;
    clave.clear();
    clave=genClave();
    cin.ignore();
    for (int s=1; s<=t; s++)
    {
        char cad[1000];
        gets(cad);
        cout<<"Case #"<<s<<": ";
        for (int c=0; c<strlen(cad); c++)
        {
            cout<<clave[cad[c]];
        }
        if (s!=t) cout<<endl;
    }
    return 0;
}
