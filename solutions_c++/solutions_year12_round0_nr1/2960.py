#include<iostream>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cstdlib>
#include<fstream>


char cipher[]={'y',  'h',  'e',  's',  'o',  'c',  'v',  'x',  'd',  'u',  'i',  'g',  'l',  'b',  'k',  'r',  'z',  't',  'n',  'w',  'j',  'p',  'f',  'm',  'a',  'q' };
char str[120];

using namespace std;
int main()
{
    int a,b,c,d,i,j,k,l,t;char ch[1];
    ifstream fin ("A-small.in");
    ofstream fout ("A-small.out");
    fin>>t;cout<<t;
    FILE * fp;
    fp= fopen ("A-small.in","r");
    fgets(str,120,fp);
    //fin.ignore(1,'\n');
    for(i=1;i<=t;i++)
    {
        fgets(str,120,fp);
        a=strlen(str);
        fout<<"Case #"<<i<<": ";
        for(j=0;j<a-1;j++)
        {
            if(str[j]!=' ')
            fout<<cipher[str[j]-'a'];
            else if(str[j]==' ')
            fout<<" ";
        }
        fout<<"\n";
    }
    return 0;
}
