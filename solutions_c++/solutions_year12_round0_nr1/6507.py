#include <iostream>
#include <stdio.h>
#include <fstream>
#include <map>
using namespace std;

int main(int argc, char *argv[])
{
    int len,i,tst,j=0;
    char c;
  map<char,char> mp;
  mp['y']='a';
  mp['n']='b';
  mp['f']='c';
  mp['i']='d';
  mp['c']='e';
  mp['w']='f';
  mp['l']='g';
  mp['b']='h';
  mp['k']='i';
  mp['u']='j';
  mp['o']='k';
  mp['m']='l'; mp['x']='m'; mp['s']='n'; mp['e']='o'; mp['v']='p'; mp['z']='q';
  mp['p']='r'; mp['d']='s'; mp['r']='t'; mp['j']='u'; mp['g']='v'; mp['t']='w';
  mp['h']='x'; mp['a']='y'; mp['q']='z';

  ifstream infil;
  ofstream ofil;
  infil.open("tst.txt");
  ofil.open("result.txt");
  string s;
 infil>>tst;
  while(infil.good()){
      if(j==tst+1)
      break;
    getline(infil,s);
    if(j==0){j++;continue;}
    ofil<<"Case #"<<j<<": ";

    len=s.length();
    for(i=0;i<len;i++)
    {
        c=char(s[i]);
        if(c==' ')
        ofil<<c;
        else
        ofil<<mp[c];

    }
  ofil<<"\n";

  j++;
   }
   infil.close();
   ofil.close();

    return 0;
}
