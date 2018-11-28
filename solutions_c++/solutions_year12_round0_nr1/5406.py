#include <cstdlib>
#include<fstream>
#include<iostream>
using namespace std;
#include<stdio.h>
#include<conio.h>
#include<string.h>

int main()
{
   ofstream out;
   out.open("Asmallout.txt");
   
   ifstream in;
   in.open("Asmall.txt");
   
   int cnum=1000,i,j=0;
   string s[cnum];
   
   out.clear();
   in.seekg(0);
   
   if(out) cout<<"ha ha ha";
   getch();
   out.clear();
   in.clear();
   
   
   while(in)
   {  
      in>>cnum;
      cnum=cnum+1;
      cout<<cnum;
      
      for(i=0;i<cnum;i++)
      {getline(in,s[i]);
      cout<<s[i]<<endl;}
      
   }
   
   for(i=0;i<cnum;i++)
   for(j=0;j<s[i].length();j++)
      switch(s[i][j])
      {     case 'a':s[i][j]='y';break;
            case 'b':s[i][j]='h';break;
            case 'c':s[i][j]='e';break;
            case 'd':s[i][j]='s';break;
            case 'e':s[i][j]='o';break;
            case 'f':s[i][j]='c';break;
            case 'g':s[i][j]='v';break;
            case 'h':s[i][j]='x';break;
            case 'i':s[i][j]='d';break;
            case 'j':s[i][j]='u';break;
            case 'k':s[i][j]='i';break;
            case 'l':s[i][j]='g';break;
            case 'm':s[i][j]='l';break;
            case 'n':s[i][j]='b';break;
            case 'o':s[i][j]='k';break;
            case 'p':s[i][j]='r';break;
            case 'q':s[i][j]='z';break;
            case 'r':s[i][j]='t';break;
            case 's':s[i][j]='n';break; 
            case 't': s[i][j]='w';break;
            case 'u': s[i][j]='j';break;
            case 'v':s[i][j]='p';break;
            case 'w':s[i][j]='f';break;
            case 'x': s[i][j]='m';break;
            case 'y': s[i][j]='a';break;
            case 'z':s[i][j]='q';break;
      }
   
i=1;
while(i<cnum-1)
{ out<<"Case #"<<i<<": "<<s[i]<<endl; i++;}
in.close();
out.close();
getch();
return 0;
}
