#include <iostream>
#include <cstring>
#include <map>
#include <stdio.h>

using namespace std;

int main()
{
  map<char,char> gMap;
  gMap['a']='y';
  gMap['b']='h';
  gMap['c']='e';
  gMap['d']='s';
  gMap['e']='o';
  gMap['f']='c';
  gMap['g']='v';
  gMap['h']='x';
  gMap['i']='d';
  gMap['j']='u';
  gMap['k']='i';
  gMap['l']='g';
  gMap['m']='l';
  gMap['n']='b';
  gMap['o']='k';
  gMap['p']='r';
  gMap['q']='z';
  gMap['r']='t';
  gMap['s']='n';
  gMap['t']='w';
  gMap['u']='j';
  gMap['v']='p';
  gMap['w']='f';
  gMap['x']='m';
  gMap['y']='a';
  gMap['z']='q';
  int t,count=1;
  cin>>t;
  getchar();
  char ca[101];
  while(t--)
    {
      cin.getline(ca,101);
      cout<<"Case #"<<count<<": ";
      for(int i=0;ca[i]!='\0';++i)
	{
	  char c=ca[i];
	  if(gMap.find(c)==gMap.end())cout<<c;
	  else cout<<gMap.find(c)->second;
	}
      cout<<endl;
      count++;
    }
  return 0;
}
