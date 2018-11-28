#include <iostream>
#include <map>
#include <string>
#include<cstdio>
#include<vector>
using namespace std;

int main ()
{
  map<char,char> mymap;
  map<char,char>::iterator it;
  int t;
  char c;
  c='a';
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
  //cout<<mymap.find('s')->second;
  
  cin>>t;
  vector<string> ss;
  getchar();
  
  for(int i=1;i<=t;i++)
  {
                  string str,res;
                  getline (cin,str);
                  ss.push_back(str);
                  
  }
  for(int i=0;i<ss.size();i++)
  {
        string str,res;
        str=ss[i];
        for(int j=0;j<str.size();j++)
                  {
                          c = str[j];
                            
                          if(c == ' ')
                               {res+= ' ';continue;}
                          res += mymap[c];
                          
                  }
                  cout<<"Case #"<<i+1<<": "<<res<<endl;
}

 //getchar();getchar();getchar();getchar();getchar();getchar();
 
 
}
