#include<iostream>
#include<cstdio>
#include<string.h>
#define M 120
using namespace std;
char s[M];
int main()
{
    //freopen("t.txt","r",stdin);
    //freopen("t1.txt","w",stdout);
    int cc,caseno;
    scanf("%d",&cc);
    getchar();
    for(caseno=1;caseno<=cc;caseno++)
    {
        for(int i=0;;i++)
        {
            s[i]=getchar();
            if(s[i]=='\n')
            {
                s[i]=0;
                break;
            }
            if(s[i]=='a') s[i]='y';
            else if(s[i]=='b') s[i]='h';
            else if(s[i]=='c') s[i]='e';
            else if(s[i]=='d') s[i]='s';
            else if(s[i]=='e') s[i]='o';
            else if(s[i]=='f') s[i]='c';
            else if(s[i]=='g') s[i]='v';
            else if(s[i]=='h') s[i]='x';
            else if(s[i]=='i') s[i]='d';
            else if(s[i]=='j') s[i]='u';
            else if(s[i]=='k') s[i]='i';
            else if(s[i]=='l') s[i]='g';
            else if(s[i]=='m') s[i]='l';
            else if(s[i]=='n') s[i]='b';
            else if(s[i]=='o') s[i]='k';
            else if(s[i]=='p') s[i]='r';
            else if(s[i]=='q') s[i]='z';
            else if(s[i]=='r') s[i]='t';
            else if(s[i]=='s') s[i]='n';
            else if(s[i]=='t') s[i]='w';
            else if(s[i]=='u') s[i]='j';
            else if(s[i]=='v') s[i]='p';
            else if(s[i]=='w') s[i]='f';
            else if(s[i]=='x') s[i]='m';
            else if(s[i]=='y') s[i]='a';
            else if(s[i]=='z') s[i]='q';
        }
        printf("Case #%d: %s\n",caseno,s);
    }
    return 0;
}
