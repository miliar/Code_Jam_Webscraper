#include <iostream>
#include <fstream>
#include<stdlib.h>
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    int t,i,j;
    char c,b[101];
    ifstream s;
    ofstream o("output2.txt");
    s.open("A-small-attempt1.in");
    s>>t;
    c=s.get();
    i=1;
    while(i<=t)
    {
              j=0;
              while((c=s.get())!='\n')
              {
                                       switch(c)
                                       {
                                                case ' ':b[j]=' ';break;
                                                case 'a':b[j]='y';break;
                                                case 'b':b[j]='h';break;
                                                case 'c':b[j]='e';break;
                                                case 'd':b[j]='s';break;
                                                case 'e':b[j]='o';break;
                                                case 'f':b[j]='c';break;
                                                case 'g':b[j]='v';break;
                                                case 'h':b[j]='x';break;
                                                case 'i':b[j]='d';break;
                                                case 'j':b[j]='u';break;
                                                case 'k':b[j]='i';break;
                                                case 'l':b[j]='g';break;
                                                case 'm':b[j]='l';break;
                                                case 'n':b[j]='b';break;
                                                case 'o':b[j]='k';break;
                                                case 'p':b[j]='r';break;
                                                case 'q':b[j]='z';break;
                                                case 'r':b[j]='t';break;
                                                case 's':b[j]='n';break;
                                                case 't':b[j]='w';break;
                                                case 'u':b[j]='j';break;
                                                case 'v':b[j]='p';break;
                                                case 'w':b[j]='f';break;
                                                case 'x':b[j]='m';break;
                                                case 'y':b[j]='a';break;
                                                case 'z':b[j]='q';break;
                                                }
                                                ++j;
                                       }
                                       b[j]='\0';
              o<<"Case #"<<i<<": "<<b<<endl;
              ++i;                               
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
