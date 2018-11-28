#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

int C=1,T;
int s;
char line[1024];
map<char,char> m;

int main(){

  m['a']='y';
  m['b']='h';
  m['c']='e';
  m['d']='s';
  m['e']='o';
  m['f']='c';
  m['g']='v';
  m['h']='x';
  m['i']='d';
  m['j']='u';
  m['k']='i';
  m['l']='g';
  m['m']='l';
  m['n']='b';
  m['o']='k';
  m['p']='r';
  m['q']='z';
  m['r']='t';
  m['s']='n';
  m['t']='w';
  m['u']='j';
  m['v']='p';
  m['x']='m';
  m['y']='a';
  m['w']='f';
  m['z']='q';
  m[' ']=' ';
  m['\n']='\n';

  scanf("%d",&T);
  fgets(line,1024,stdin);
  while(T--){
    printf("Case #%d: ",C++);
    fgets(line,1024,stdin);
    s=strlen(line);
    for(int i=0;i<s;i++) printf("%c",m[line[i]]);
  }

  return 0;
}
