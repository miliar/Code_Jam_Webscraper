#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char map[300];

void deal(char *a)
{
    int len=strlen(a);
    for(int i=0;i<len;i++)
    {
        a[i]=map[a[i]];
    }
}

int main()
{
    int t;
    char a[120];
    map['a']='y';
    map['b']='h';
    map['c']='e';
    map['d']='s';
    map['e']='o';
    map['f']='c';
    map['g']='v';
    map['h']='x';
    map['i']='d';
    map['j']='u';
    map['k']='i';
    map['l']='g';
    map['m']='l';
    map['n']='b';
    map['o']='k';
    map['p']='r';
    map['q']='z';
    map['r']='t';
    map['s']='n';
    map['t']='w';
    map['u']='j';
    map['v']='p';
    map['w']='f';
    map['x']='m';
    map['y']='a';
    map['z']='q';
    map[' ']=' ';

    cin>>t;
    cin.getline(a,101);
    for(int iii=1;iii<=t;iii++)
    {
        cin.getline(a,101);
        deal(a);
        cout<<"Case #"<<iii<<": "<<a<<endl;
    }
    //system("pause");
    return 0;
}
