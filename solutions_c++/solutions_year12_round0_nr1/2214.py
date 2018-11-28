#include <iostream>
#include <map>
using namespace std;
int main()
{
map<char,char> mymap;
map<char,char> inv_mymap;

mymap[' ']=' ';

mymap['a']='y';
mymap['b']='n';
mymap['c']='f';
mymap['d']='i';
mymap['e']='c';
mymap['f']='w';
mymap['g']='l';

mymap['h']='b';
mymap['i']='k';
mymap['j']='u';
mymap['k']='o';
mymap['l']='m';
mymap['m']='x';
mymap['n']='s';

mymap['o']='e';
mymap['p']='v';
mymap['q']='z'; 

mymap['r']='p';
mymap['s']='d';
mymap['t']='r';
mymap['u']='j';
mymap['v']='g';
mymap['w']='t';
mymap['x']='h';
mymap['y']='a';
mymap['z']='q';

inv_mymap[' ']=' ';
for(int i=0;i<26;i++)
	inv_mymap[mymap['a'+i]]='a'+i;

int T;
cin>>T;
string s;
getline(cin,s);
for(int i=0;i<T;i++)
{
string s;
getline(cin,s);
for(int j=0;j<s.length();j++)
	s[j]=inv_mymap[s[j]];
cout<<"Case #"<<i+1<<": "<<s<<endl;
}

}
