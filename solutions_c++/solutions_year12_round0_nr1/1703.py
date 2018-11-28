#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstring>
using namespace std;
string str;
int t,i,j,k,l;
int main()
{
    ofstream fout ("testout.txt");
    ifstream fin ("testin.txt");
    fin>>t;
    for (j=0; j<=t; j++)
    {
        getline(fin,str);
        if (j!=0)
            {
                fout<<"Case #"<<j<<": ";
                for (i=0; i<str.size(); i++)
            {
                if (str[i]=='y') fout<<"a";
                if (str[i]=='n') fout<<"b";
                if (str[i]=='f') fout<<"c";
                if (str[i]=='i') fout<<"d";
                if (str[i]=='c') fout<<"e";
                if (str[i]=='w') fout<<"f";
                if (str[i]=='l') fout<<"g";
                if (str[i]=='b') fout<<"h";
                if (str[i]=='k') fout<<"i";
                if (str[i]=='u') fout<<"j";
                if (str[i]=='o') fout<<"k";
                if (str[i]=='m') fout<<"l";
                if (str[i]=='x') fout<<"m";
                if (str[i]=='s') fout<<"n";
                if (str[i]=='e') fout<<"o";
                if (str[i]=='v') fout<<"p";
                if (str[i]=='z') fout<<"q";
                if (str[i]=='p') fout<<"r";
                if (str[i]=='d') fout<<"s";
                if (str[i]=='r') fout<<"t";
                if (str[i]=='j') fout<<"u";
                if (str[i]=='g') fout<<"v";
                if (str[i]=='t') fout<<"w";
                if (str[i]=='h') fout<<"x";
                if (str[i]=='a') fout<<"y";
                if (str[i]=='q') fout<<"z";
                if (str[i]<'a' || str[i]>'z') fout<<str[i];
        }
            fout<<endl;
            }
    }
    return 0;

}
