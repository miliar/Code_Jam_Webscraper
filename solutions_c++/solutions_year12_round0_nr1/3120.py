#include<iostream>
#include<map>
using namespace std;

int main()
{
  map<char,char> mp1,mp2;
  map<char,char>::iterator itr;
  int t;
    
  mp1['a']='y';
  mp1['b']='n';
  mp1['c']='f';
  mp1['d']='i';
  mp1['e']='c';
  mp1['f']='w';
  mp1['h']='b';
  mp1['i']='k';
  mp1['j']='u';
  mp1['k']='o';
  mp1['l']='m';
  mp1['m']='x';
  mp1['n']='s';
  mp1['o']='e';
  mp1['p']='v';
  mp1['q']='z';
  mp1['r']='p';
  mp1['s']='d';
  mp1['t']='r';
  mp1['u']='j';
  mp1['v']='g';
  mp1['w']='t';
  mp1['x']='h';
  mp1['y']='a';
  mp1['z']='q';
  mp1['g']='l';
  mp1[' ']=' ';
  
  for(itr=mp1.begin();itr!=mp1.end();itr++)
    mp2[itr->second]=itr->first;
  
  cin>>t;
  string s;
  cin.ignore();
  for(int n=0;n<t;n++)
  {
    getline(cin,s,'\n');
    cout<<"Case #"<<n+1<<": ";
    for(int i=0;i<s.length();i++)
     cout<<mp2[s[i]];
    cout<<endl;
  }    
  
  return 0;
}
