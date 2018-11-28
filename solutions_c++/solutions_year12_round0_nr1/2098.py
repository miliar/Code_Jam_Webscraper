#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
 
 
string ungooglerese(char* foo)
{
        char* bar=foo;
        int i,size=0;
	for(size=0;foo[size]!='\0';size++);
        for(i=0;i<size;i++)
        {
                switch(bar[i])
                {
                case 'a': bar[i]='y';break;
                case 'b':bar[i]='h';break;
                case 'c':bar[i]='e';break;
                case 'd':bar[i]='s';break;
                case 'e':bar[i]='o';break;
                case 'f':bar[i]='c';break;
                case 'g':bar[i]='v';break;
                case 'h':bar[i]='x';break;
                case 'i':bar[i]='d';break;
                case 'j':bar[i]='u';break;
                case 'k':bar[i]='i';break;
                case 'l':bar[i]='g';break;
                case 'm':bar[i]='l';break;
                case 'n':bar[i]='b';break;
                case 'o':bar[i]='k';break;
                case 'p':bar[i]='r';break;
                case 'q':bar[i]='z';break;
                case 'r':bar[i]='t';break;
                case 's':bar[i]='n';break;
                case 't':bar[i]='w';break;
                case 'u':bar[i]='j';break;
                case 'v':bar[i]='p';break;
                case 'w':bar[i]='f';break;
                case 'x':bar[i]='m';break;
                case 'y':bar[i]='a';break;
                case 'z':bar[i]='q';break;
                default: break;
                }
 
        }
        return bar;
 
}
 
 
int main(void)
{
        int T,i;
        char foo[1000];
        cin>>T;
 	getchar();
        for(i=1;i<=T;i++)
        {
                gets(foo);
                cout<<"Case #"<<i<<": "<<ungooglerese(foo)<<endl;
        
        }
return 0;
}