#include<iostream>
#include<string.h>
#include<string>
#include<map>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("data.out","w",stdout);
    map<char,char> hash;
    hash[' ']=' ';
    hash['a']='y';hash['b']='h';hash['c']='e';
    hash['d']='s';hash['e']='o';hash['f']='c';
    hash['g']='v';hash['h']='x';hash['i']='d';
    hash['j']='u';hash['k']='i';hash['l']='g';
    hash['m']='l';hash['n']='b';hash['o']='k';
    hash['p']='r';hash['q']='z';hash['r']='t';
    hash['s']='n';hash['t']='w';hash['u']='j';
    hash['v']='p';hash['w']='f';hash['x']='m';
    hash['y']='a';hash['z']='q';
    char s[105];
    int t;
    scanf("%d",&t);
    getchar();
    int i;
    for(i=1;i<=t;i++){
       gets(s);
       int len=strlen(s);
       int j;
       for(j=0;j<len;j++)
          s[j]=hash[s[j]];
       printf("Case #%d: %s\n",i,s);
    }
}
