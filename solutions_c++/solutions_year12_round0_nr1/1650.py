#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int a,b,c,d;
char s[200],s2[200];
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&b);
    getchar();
    for (c=1;c<=b;c++)
    {
        gets(s);
        d=strlen(s);
        for (a=0;a<d;a++)
        {
            if (s[a]=='a') s2[a]='y';
            else if (s[a]=='b') s2[a]='h';
            else if (s[a]=='c') s2[a]='e';
            else if (s[a]=='d') s2[a]='s';
            else if (s[a]=='e') s2[a]='o';
            else if (s[a]=='f') s2[a]='c';
            else if (s[a]=='g') s2[a]='v';
            else if (s[a]=='h') s2[a]='x';
            else if (s[a]=='i') s2[a]='d';
            else if (s[a]=='j') s2[a]='u';
            else if (s[a]=='k') s2[a]='i';
            else if (s[a]=='l') s2[a]='g';
            else if (s[a]=='m') s2[a]='l';
            else if (s[a]=='n') s2[a]='b';
            else if (s[a]=='o') s2[a]='k';
            else if (s[a]=='p') s2[a]='r';
            else if (s[a]=='q') s2[a]='z';
            else if (s[a]=='r') s2[a]='t';
            else if (s[a]=='s') s2[a]='n';
            else if (s[a]=='t') s2[a]='w';
            else if (s[a]=='u') s2[a]='j';
            else if (s[a]=='v') s2[a]='p';
            else if (s[a]=='w') s2[a]='f';
            else if (s[a]=='x') s2[a]='m';
            else if (s[a]=='y') s2[a]='a';
            else if (s[a]=='z') s2[a]='q';
            else s2[a]=s[a];
        }
        s2[a]=0;
        printf("Case #%d: %s\n",c,s2);
    }
}
