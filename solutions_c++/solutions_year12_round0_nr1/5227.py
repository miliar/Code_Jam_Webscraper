#include<stdio.h>
#include<string.h>
#include<map>
#include<iostream>
using namespace std;



int t,cas,i,j,n;
map<char,char>mp;
char a[101];
int main()
{
 freopen("A-small-attempt2.in","r",stdin);
 freopen("in.txt","w",stdout);

 mp['a']='y';
 mp['b']='h';
 mp['c']='e';
 mp['d']='s';
 mp['e']='o';
 mp['f']='c';
 mp['g']='v';
 mp['h']='x';
 mp['i']='d';
 mp['j']='u';
 mp['k']='i';
 mp['l']='g';
 mp['m']='l';
 mp['n']='b';
 mp['o']='k';
 mp['p']='r';
 mp['q']='z';
 mp['r']='t';
 mp['s']='n';
 mp['t']='w';
 mp['u']='j';
 mp['v']='p';
 mp['w']='f';
 mp['x']='m';
 mp['y']='a';
 mp['z']='q';




 scanf("%d\n",&cas);

 for(t=1;t<=cas;t++)
 {
    gets(a);
    n=strlen(a);

    printf("Case #%d: ",t);
    for(i=0;i<n;i++)
    {
      if(a[i]==' ')
       cout<<" ";
      else
       cout<<mp[a[i]];
    }
    cout<<endl;
 }

return 0;

}
