#include<iostream>
#include<map>
#include<stdio.h>
using namespace std;
int main()
{
    map<char,char> arr;
    arr['a']='y';
    arr['b']='h';
    arr['c']='e';
    arr['d']='s';
    arr['e']='o';
    arr['f']='c';
    arr['g']='v';
    arr['h']='x';
    arr['i']='d';
    arr['j']='u';
    arr['k']='i';
    arr['l']='g';
    arr['m']='l';
    arr['n']='b';
    arr['o']='k';
    arr['p']='r';
    arr['q']='z';
    arr['r']='t';
    arr['s']='n';
    arr['t']='w';
    arr['u']='j';
    arr['v']='p';
    arr['w']='f';
    arr['x']='m';
    arr['y']='a';
    arr['z']='q';
    int test;
    scanf("%d",&test);
    int ctr=1;
    test++;
    while(test--)
    {
                 cout<<"Case #"<<ctr-1<<": ";
    char st[101];
    gets(st);
    for(int i=0;i<strlen(st);i++)
    {
            if(st[i]==' ')
                    cout<<" ";
            else
                cout<<arr[st[i]];
    }
    cout<<endl;
    ctr++;
    }
}
