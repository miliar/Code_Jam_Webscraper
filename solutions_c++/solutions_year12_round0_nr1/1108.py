#include<iostream>
#include<fstream>
#include<map>
using namespace std;

map<char,char> code;

string translate(string s)
{
int c=s.length();
int i;
for(i=0;i<c;i++)
{
if(s[i]!=' ')
{s[i]=code[s[i]];}
}
return s;
}

int main()
{
code['a']='y'; code['b']='h'; code['c']='e'; code['d']='s'; code['e']='o'; code['f']='c'; code['g']='v';
code['h']='x'; code['i']='d'; code['j']='u'; code['k']='i'; code['l']='g'; code['m']='l'; code['n']='b';
code['o']='k'; code['p']='r'; code['q']='z'; code['r']='t'; code['s']='n'; code['t']='w'; code['u']='j';
code['v']='p'; code['w']='f'; code['x']='m'; code['y']='a'; code['z']='q';
ifstream in("crypto.in");
ofstream out("crypto.out");
int t;
in >> t;
string g;
getline(in,g);
int i;
for(i=1;i<=t;i++)
{
getline(in,g);
g=translate(g);
out << "Case #" << i << ": " << g << endl;
}
  
in.close(); out.close();    
return 0;    
}
