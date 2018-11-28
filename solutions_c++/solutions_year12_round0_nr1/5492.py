#include<stdio.h>
#include<map>
using namespace std;

int main()
{
  map<char,char> mymap;
  map<char,char>::iterator it;
  
  mymap['a']='y';
  mymap['b']='h';
  mymap['c']='e';
  mymap['d']='s';
  mymap['e']='o';
  mymap['f']='c';
  mymap['g']='v';
  mymap['h']='x';
  mymap['i']='d';
  mymap['j']='u';
  mymap['k']='i';
  mymap['l']='g';
  mymap['m']='l';
  mymap['n']='b';
  mymap['o']='k';
  mymap['p']='r';
  mymap['q']='z';
  mymap['r']='t';
  mymap['s']='n';
  mymap['t']='w';
  mymap['u']='j';
  mymap['v']='p';
  mymap['w']='f';
  mymap['x']='m';
  mymap['y']='a';
  mymap['z']='q';
  
  int t,i,j;
  char a;
  scanf("%d",&t);
  scanf("%c",&a);
  for(i=1;i<=t;i++)
  {
    printf("Case #%d: ",i);
    scanf("%c",&a);
    while(a!='\n')
    {
      if(a>=97 && a<=122)
	printf("%c",mymap.find(a)->second);
      else
	printf("%c",a);
      scanf("%c",&a);
    }
    printf("\n");
  }
}