#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{

  int test,len,i,j=0;
  string a;
  char arr[200];
  arr['a']='y';arr['b']='h';arr['c']='e';arr['d']='s';arr['e']='o';arr['f']='c';arr['g']='v';arr['h']='x';arr['i']='d';arr['j']='u';arr['k']='i';arr['l']='g';arr['m']='l';arr['n']='b';arr['o']='k';arr['p']='r';arr['q']='z';arr['r']='t';arr['s']='n';arr['t']='w';arr['u']='j';arr['v']='p';arr['w']='f';arr['x']='m';arr['y']='a';arr['z']='q';
  cin>>test;
  getchar();
  while(test--)
  {
  j++;
  getline(cin,a);
   len=a.length();
   for(i=0;i<len;i++)
   {
      if(a[i]!=' ')
      a[i]=arr[a[i]];
   }

   cout<<"Case #"<<j<<": "<<a<<endl;
   a[1010]='\0';
}
  return 0;
}
