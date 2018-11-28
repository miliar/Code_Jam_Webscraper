#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
#define for(i,n) for(long i=0;i<n;i++)
int main()
{
    //freopen("aI.in","r",stdin);
    //freopen ("aO.txt","w",stdout);
    long t,cas=1,i,j,n;
    
    char s[1000];
    cin>>t;
    getchar();
    char m[200];
    i=97;
    m[i++]='y';
    m[i++]='h';
    m[i++]='e';
    m[i++]='s';
    m[i++]='o';
    m[i++]='c';
    m[i++]='v';
    m[i++]='x';
    m[i++]='d';
    m[i++]='u';
    m[i++]='i';
    m[i++]='g';
    m[i++]='l';
    m[i++]='b';
    m[i++]='k';
    m[i++]='r';
    m[i++]='z';
    m[i++]='t';
    m[i++]='n';
    m[i++]='w';
    m[i++]='j';
    m[i++]='p';
    m[i++]='f';
    m[i++]='m';
    m[i++]='a';
    m[i++]='q';
    m[32]=' ';
    while(t--)
    {
              gets(s);
              printf("Case #%ld: ",cas++);
              for(i,strlen(s)) cout<<m[s[i]];
              cout<<endl;
    }
    return 0;
}
