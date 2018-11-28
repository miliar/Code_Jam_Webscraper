#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

void decode(string a,int asd);
ifstream in("A-small-attempt0.in");
ofstream out("out.txt");

int main()
{
    int t;
    in>>t;
    string a;
    getline(in,a);
    for(int i=1;i<=t;i++)
    {
        getline(in,a);
        decode(a,i);
    }
    return 0;
}

void decode(string a,int asd)
{
    int l=a.length();
    for(int i=0;i<l;i++)
    {
        if(a[i]=='a')
        {
            a[i]='y';
        }else
        if(a[i]=='b')
        {
            a[i]='h';
        }else
        if(a[i]=='c')
        {
            a[i]='e';
        }else
        if(a[i]=='d')
        {
            a[i]='s';
        }else
        if(a[i]=='e')
        {
            a[i]='o';
        }else
        if(a[i]=='f')
        {
            a[i]='c';
        }else
        if(a[i]=='g')
        {
            a[i]='v';
        }else
        if(a[i]=='h')
        {
            a[i]='x';
        }else
        if(a[i]=='i')
        {
            a[i]='d';
        }else
        if(a[i]=='j')
        {
            a[i]='u';
        }else
        if(a[i]=='k')
        {
            a[i]='i';
        }else
        if(a[i]=='l')
        {
            a[i]='g';
        }else
        if(a[i]=='m')
        {
            a[i]='l';
        }else
        if(a[i]=='n')
        {
            a[i]='b';
        }else
        if(a[i]=='o')
        {
            a[i]='k';
        }else
        if(a[i]=='p')
        {
            a[i]='r';
        }else
        if(a[i]=='q')
        {
            a[i]='z';
        }else
        if(a[i]=='r')
        {
            a[i]='t';
        }else
        if(a[i]=='s')
        {
            a[i]='n';
        }else
        if(a[i]=='t')
        {
            a[i]='w';
        }else
        if(a[i]=='u')
        {
            a[i]='j';
        }else
        if(a[i]=='v')
        {
            a[i]='p';
        }else
        if(a[i]=='w')
        {
            a[i]='f';
        }else
        if(a[i]=='x')
        {
            a[i]='m';
        }else
        if(a[i]=='y')
        {
            a[i]='a';
        }else
        if(a[i]=='z')
        {
            a[i]='q';
        }
    }
    out<<"Case #"<<asd<<": "<<a<<endl;
}
