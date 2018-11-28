#include<iostream>
#include<string>
#include<map>
using namespace std;


int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t;
    map<char,char>m;
    m.clear();
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
    m[' ']=' ';
    scanf("%d",&t);
    getchar();
    for(int i = 1; i <= t; i++)
    {
        string str;
        char c;
        //int j = 0;
        while(1)
        {
            scanf("%c",&c);
            if(c=='\n')
                break;
            else
                str += m[c];
        }
        printf("Case #%d: ",i);
        cout<<str<<endl;
    }
    return 0;
}
