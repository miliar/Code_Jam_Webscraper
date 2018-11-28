#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
    char s[200];
    int data[300];
	data['a']='y';
    data['b']='h';
    data['c']='e';
    data['d']='s';
    data['e']='o';
    data['f']='c';
    data['g']='v';
    data['h']='x';
    data['i']='d';
    data['j']='u';
    data['k']='i';
    data['l']='g';
    data['m']='l';
    data['n']='b';
    data['o']='k';
    data['p']='r';
    data['q']='z';
    data['r']='t';
    data['s']='n';
    data['t']='w';
    data['u']='j';
    data['v']='p';
    data['w']='f';
    data['x']='m';
    data['y']='a';
    data['z']='q';
    data[' ']=' ';
    int n,i,cas;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>n;
    gets(s);
    for (cas=1; cas<=n; cas++)
    {
        gets(s);
        printf("Case #%d: ",cas);
        for (i=0; s[i]; i++)
        {
            printf("%c",data[s[i]]);
        }
        printf("\n");
    }
    return 0;
}
