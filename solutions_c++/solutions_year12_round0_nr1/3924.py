#include<stdio.h>
#include<string.h>
#include <iostream>
#include <map>
using namespace std;

map<char,char> C;

void initCipher()
{
    C[' ']=' ';

    C['a']='y';
    C['b']='h';
    C['c']='e';
    C['d']='s';
    C['e']='o';
    C['f']='c';
    C['g']='v';
    C['h']='x';
    C['i']='d';
    C['j']='u';
    C['k']='i';
    C['l']='g';
    C['m']='l';

    C['n']='b';
    C['o']='k';
    C['p']='r';
    C['q']='z';
    C['r']='t';
    C['s']='n';
    C['t']='w';
    C['u']='j';
    C['v']='p';
    C['w']='f';
    C['x']='m';
    C['y']='a';
    C['z']='q';
}

int main()
{
    int t,len,caseNum=1,i;
    string res;
    initCipher();
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    cin>>t;
    char s[201];
    gets(s);//get rid of 1 newline ('\n')
    while(t>0)
    {
        gets(s);
        len=strlen(s);
        res="";
        for(i=0;i<len;i++)
            res.push_back(C[s[i]]);
        cout<<"Case #"<<caseNum<<": "<<res<<endl;
        t--;
        caseNum++;
    }
    return 0;
}
