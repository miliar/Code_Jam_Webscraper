#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

int main()
{

    freopen("A-small-attempt5.in", "r", stdin);
    freopen("A-small-attempt5.out", "w", stdout);
    char g[210],s[210];
    int t,i,j,l;
    scanf("%d",&t);
    gets(g);
    for(i=1;i<=t;i++)
    {
        memset(s,0,sizeof(s));
        memset(g,0,sizeof(g));
        gets(g);
        l=strlen(g);
        for(j=0;j<l;j++)
        {
            if(g[j]=='a')s[j]='y';
            if(g[j]=='b')s[j]='h';
            if(g[j]=='c')s[j]='e';
            if(g[j]=='d')s[j]='s';
            if(g[j]=='e')s[j]='o';
            if(g[j]=='f')s[j]='c';
            if(g[j]=='g')s[j]='v';
            if(g[j]=='h')s[j]='x';
            if(g[j]=='i')s[j]='d';
            if(g[j]=='j')s[j]='u';
            if(g[j]=='k')s[j]='i';
            if(g[j]=='l')s[j]='g';
            if(g[j]=='m')s[j]='l';
            if(g[j]=='n')s[j]='b';
            if(g[j]=='o')s[j]='k';
            if(g[j]=='p')s[j]='r';
            if(g[j]=='q')s[j]='z';
            if(g[j]=='r')s[j]='t';
            if(g[j]=='s')s[j]='n';
            if(g[j]=='t')s[j]='w';
            if(g[j]=='u')s[j]='j';
            if(g[j]=='v')s[j]='p';
            if(g[j]=='w')s[j]='f';
            if(g[j]=='x')s[j]='m';
            if(g[j]=='y')s[j]='a';
            if(g[j]=='z')s[j]='q';
            if(g[j]==' ')s[j]=' ';
        }
        printf("Case #%d: %s\n",i,s);

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
