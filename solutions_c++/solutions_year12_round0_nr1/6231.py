#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int t,j=0;
    string s,s1;
    scanf("%d",&t);
    getchar();
    while(j<t)
    {
        getline(cin,s);
        int size=s.size();
        char ch;
        for(int i=0; i<size; i++)
        {
            ch=s[i];
            switch(ch)
            {
                case 'a':s1+='y';
                         break;
                case 'b':s1+='h';
                         break;
                case 'c':s1+='e';
                         break;
                case 'd':s1+='s';
                         break;
                case 'e':s1+='o';
                         break;
                case 'f':s1+='c';
                         break;
                case 'g':s1+='v';
                         break;
                case 'h':s1+='x';
                         break;
                case 'i':s1+='d';
                         break;
                case 'j':s1+='u';
                         break;
                case 'k':s1+='i';
                         break;
                case 'l':s1+='g';
                         break;
                case 'm':s1+='l';
                         break;
                case 'n':s1+='b';
                         break;
                case 'o':s1+='k';
                         break;
                case 'p':s1+='r';
                         break;
                case 'q':s1+='z';
                         break;
                case 'r':s1+='t';
                         break;
                case 's':s1+='n';
                         break;
                case 't':s1+='w';
                         break;
                case 'u':s1+='j';
                         break;
                case 'v':s1+='p';
                         break;
                case 'w':s1+='f';
                         break;
                case 'x':s1+='m';
                         break;
                case 'y':s1+='a';
                         break;
                case 'z':s1+='q';
                         break;
                case ' ':s1+=' ';
                         break;
            }
        }
        cout<<"Case #"<<j+1<<": "<<s1<<"\n";
        s1.clear();
        j++;
    }
    return 0;
}

