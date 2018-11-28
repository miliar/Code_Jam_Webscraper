#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("xyz.out","w",stdout);
int t;
cin>>t;
string x,g[32];
getline(cin,x);
for(int i=0;i<t;i++)
{
x="";
getline(cin,x);
g[i]="";
for(int j=0;j<x.size();j++)
{  
if(x[j]=='y'){g[i]+="a";}
else
if(x[j]=='n'){g[i]+="b";}
else
if(x[j]=='f'){g[i]+="c";}
else
if(x[j]=='i'){g[i]+="d";}
else
if(x[j]=='c'){g[i]+="e";}
else
if(x[j]=='w'){g[i]+="f";}
else
if(x[j]=='l'){g[i]+="g";}
else
if(x[j]=='b'){g[i]+="h";}
else
if(x[j]=='k'){g[i]+="i";}
else
if(x[j]=='u'){g[i]+="j";}
else
if(x[j]=='o'){g[i]+="k";}
else
if(x[j]=='m'){g[i]+="l";}
else
if(x[j]=='x'){g[i]+="m";}
else
if(x[j]=='s'){g[i]+="n";}
else
if(x[j]=='e'){g[i]+="o";}
else
if(x[j]=='v'){g[i]+="p";}
else
if(x[j]=='z'){g[i]+="q";}
else
if(x[j]=='p'){g[i]+="r";}
else
if(x[j]=='d'){g[i]+="s";}
else
if(x[j]=='r'){g[i]+="t";}
else
if(x[j]=='j'){g[i]+="u";}
else
if(x[j]=='g'){g[i]+="v";}
else
if(x[j]=='t'){g[i]+="w";}
else
if(x[j]=='h'){g[i]+="x";}
else
if(x[j]=='a'){g[i]+="y";}
else
if(x[j]=='q'){g[i]+="z";}
else
{g[i]+=" ";}
}        
}       
for(int i=0;i<t;i++)
{
cout<<"Case #"<<i+1<<": "<<g[i]<<endl;
} 
//system("pause");
return 0;
}
