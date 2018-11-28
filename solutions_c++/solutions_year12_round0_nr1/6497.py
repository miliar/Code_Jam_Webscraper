#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{

ifstream in;
in.open ("in.txt");

ofstream out;
out.open ("out.txt");

int t,i,j;
char g[]="yhesocvxduiglbkrztnwjpfmaq";

in>>t;

char gg[102];
//gg=' ';
in.getline(gg,t*100);
for(i=0;i<t;i++)
{
in.getline(gg,t*100);
out<<"Case #"<<i+1<<": ";
for(j=0;j<102;j++)
{
                  if(gg[j]=='\0'||gg[j]=='\n')
                  break;
    if(gg[j]==' ')
    out<<" ";

    else
    {
        out<<g[gg[j]-97];
    }

}
out<<endl;
 memset(gg,0,101);
}
//out<<gg;
//cout<<gg;
}
