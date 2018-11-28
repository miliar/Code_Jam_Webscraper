#include<iostream>
#include<map>
#include<string>
using namespace std;
int main() {
     map<char, char> m;
     string s,t;
     int i,j,T;
     m['y']='a';
     m['n']='b';
     m['f']='c';
     m['i']='d';
     m['c']='e';
     m['w']='f';
     m['l']='g';
     m['b']='h';
     m['k']='i';
     m['u']='j';
     m['o']='k';
     m['m']='l';
     m['x']='m';
     m['s']='n';
     m['e']='o';
     m['v']='p';
     m['z']='q';
     m['p']='r';
     m['d']='s';
     m['r']='t';
     m['j']='u';
     m['g']='v';
     m['t']='w';
     m['h']='x';
     m['a']='y';
     m['q']='z';
     cin>>T;
     cin.ignore();
     for(i=0; i<T; i++) {
          getline(cin, s);
          for(j=0; j<s.size(); j++) {
               if(s[j]!=' ') {
                    t+=m[s[j]];
               } else {
                    t+=s[j];
               }
          }
          cout<<"Case #"<<i+1<<": "<<t<<endl;
          t.clear();
     }
     return 0;
}
