#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
map<char,char>M;
int main()
{
freopen("A-small-attempt6.in.txt","r",stdin);
freopen("A-small-attempt0.out-1.txt","w",stdout);
int ks,i,j;
char ar[109],hu[10];
M['a']='y'; M['b']='h'; M['c']='e'; M['d']='s'; M['e']='o';
M['f']='c'; M['g']='v'; M['h']='x'; M['i']='d'; M['j']='u';
M['k']='i'; M['l']='g'; M['m']='l'; M['n']='b'; M['o']='k';
M['p']='r'; M['q']='z'; M['r']='t'; M['s']='n'; M['t']='w';
M['u']='j'; M['v']='p'; M['w']='f'; M['x']='m'; M['y']='a';
M['z']='q';
M[' ']=' ';
cin>>ks;

gets(hu);

for(i=1;i<=ks;i++)
{
  gets(ar);
  int len=strlen(ar);
  printf("Case #%d: ",i);
  for(j=0;j<len;j++)
    {   cout<<M[ar[j]];}
	
	
	
	printf("\n");

}

return 0;
}

