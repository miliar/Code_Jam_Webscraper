#include <iostream>
#include <map>
#include <cstdio>
using namespace std;
int main(){
  map <char,char> trans;
  trans['a']='y';
  trans['b']='h';
  trans['c']='e';
  trans['d']='s';
  trans['e']='o';
  trans['f']='c';
  trans['g']='v';
  trans['h']='x';
  trans['i']='d';
  trans['j']='u';
  trans['k']='i';
  trans['l']='g';
  trans['m']='l';
  trans['n']='b';
  trans['o']='k';
  trans['p']='r';
  trans['q']='z';
  trans['r']='t';
  trans['s']='n';
  trans['t']='w';
  trans['u']='j';
  trans['v']='p';
  trans['w']='f';
  trans['x']='m';
  trans['y']='a';
  trans['z']='q';
  trans[' ']=' ';
  int t;
  string str;
  string::iterator it;
  cin >> t;
  getline(cin,str);
  int i = 1;
  while(t--){
    getline(cin,str);
    cout << "Case #"<< i << ": ";
    for(it=str.begin();it!=str.end();it++){
      printf("%c",(trans[*it]));
    }
    i++;
    cout << endl;
  }
  return 0;
}
