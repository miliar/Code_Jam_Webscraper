using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
int main()
{
int t;
cin>>t;
map<char,char> c;
c['a']='y';c['j']='u';c['p']='r';c['c']='e';c['m']='l';c['y']='a';c['s']='n';
c['l']='g';c['k']='i';c['x']='m';c['v']='p';c['n']='b';c['r']='t';c['e']='o';
c['i']='d';c['b']='h';c['f']='c';c['g']='v';c['h']='x';c['o']='k';c['t']='w';
c['u']='j';c['w']='f';c['z']='q';c['q']='z';c['d']='s';c[' ']=' ';
int j=1;
getchar();
while(j<=t)
{
   string s,s1="";
   getline( cin, s, '\n' );
   for(int i=0;i<s.length();i++)s1+=c[s[i]];
   cout<<"Case #"<<j<<": "<<s1<<'\n';
   j++;       
}
return 0;
}
