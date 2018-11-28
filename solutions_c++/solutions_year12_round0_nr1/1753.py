#include<iostream>
#include<algorithm>
#include<map>
#include<cstdio>
#include<conio.h>
using namespace std;

int main()
{
    int t,k=0,i;
    map<char, char> m;
    char str[101];
    
    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';
    
    fflush(stdin);
    cin>>t;
    t++;
    while(t--)
    {
           gets(str);
           if(k>0)
           cout<<"Case #"<<k++<<": ";
           else
           k++;
           for(i=0;str[i]!='\0';i++)
           {
                                    if(str[i]==' ')
                                    {
                                                 cout<<' ';
                                    }
                                    else
                                    cout<<m[str[i]];
           }
           if(k>1) cout<<'\n';
    }
    getch();
    return(0);
}
