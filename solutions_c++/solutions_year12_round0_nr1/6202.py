#include<iostream>
#include<string.h>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
    int t,num[31];
    char b;
    char a[31][101];
    FILE *fpin,*fpout;
    fpin=freopen("A-small-attempt1.in","r",stdin);
    fpout=freopen("out.out","w",stdout);
    scanf("%d",&t);
    scanf("%c",&b);
    for(int i=1;i<=t;i++)
    {
        gets(a[i]);
        num[i]=strlen(a[i]);
        //cout<<num[i];
        for(int j=0;j<num[i];j++)
    {
        switch (a[i][j])
        {
            case 'a':a[i][j]='y';break;
            case 'b':a[i][j]='h';break;
            case 'c':a[i][j]='e';break;
            case 'd':a[i][j]='s';break;
            case 'e':a[i][j]='o';break;
            case 'f':a[i][j]='c';break;
            case 'g':a[i][j]='v';break;
            case 'h':a[i][j]='x';break;
            case 'i':a[i][j]='d';break;
            case 'j':a[i][j]='u';break;
            case 'k':a[i][j]='i';break;
            case 'l':a[i][j]='g';break;
            case 'm':a[i][j]='l';break;
            case 'n':a[i][j]='b';break;
            case 'o':a[i][j]='k';break;
            case 'p':a[i][j]='r';break;
            case 'q':a[i][j]='z';break;
            case 'r':a[i][j]='t';break;
            case 's':a[i][j]='n';break;
            case 't':a[i][j]='w';break;
            case 'u':a[i][j]='j';break;
            case 'v':a[i][j]='p';break;
            case 'w':a[i][j]='f';break;
            case 'x':a[i][j]='m';break;
            case 'y':a[i][j]='a';break;
            case 'z':a[i][j]='q';break;
            case ' ':a[i][j]=' ';break;
        }
    }
    }
    for(int i=1;i<=t;i++)
    {
    cout<<"Case #"<<i<<": "<<a[i]<<endl;
    }
    fclose(stdout);
    return 0;

}
