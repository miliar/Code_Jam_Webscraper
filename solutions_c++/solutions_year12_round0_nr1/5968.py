#include<iostream>
#include<string>
#include<conio.h>
using namespace std;
int main()
{
    char g[101],m[101];
    int i,t,j,p=0;
    cin>>t;
    for(j=0;j<=t;j++)
    {
     gets(g);
     if(j!=0)
     {
     for(i=0;i<100;i++)
     {
                      if(g[i]=='y')
                      m[i]='a';
             if(g[i]=='n')
                 m[i]='b';
             if(g[i]=='f')
                 m[i]='c';
                 if(g[i]=='i')
                      m[i]='d';
             if(g[i]=='c')
                 m[i]='e';
             if(g[i]=='w')
                 m[i]='f';
                 if(g[i]=='l')
                      m[i]='g';
             if(g[i]=='b')
                 m[i]='h';
             if(g[i]=='k')
                 m[i]='i';
                 if(g[i]=='u')
                      m[i]='j';
             if(g[i]=='o')
                 m[i]='k';
             if(g[i]=='m')
                 m[i]='l';
                 if(g[i]=='x')
                      m[i]='m';
             if(g[i]=='s')
                 m[i]='n';
             if(g[i]=='e')
                 m[i]='o';
                 if(g[i]=='v')
                      m[i]='p';
             if(g[i]=='z')
                 m[i]='q';
             if(g[i]=='p')
                 m[i]='r';
                 if(g[i]=='d')
                      m[i]='s';
             if(g[i]=='r')
                 m[i]='t';
             if(g[i]=='j')
                 m[i]='u';
                 if(g[i]=='g')
                      m[i]='v';
             if(g[i]=='t')
                 m[i]='w';
             if(g[i]=='h')
                 m[i]='x';
                 if(g[i]=='a')
                      m[i]='y';
             if(g[i]=='q')
                 m[i]='z';
                 if(g[i]==' ')
                 m[i]=' ';
                //if(i!=0)
             if(g[i]=='\0')
             {
                           m[i]='\0';
                           break;
             }
           }p++;cout<<"Case #"<<p<<": "; puts(m);}
      }
    return 0;
}
                        
