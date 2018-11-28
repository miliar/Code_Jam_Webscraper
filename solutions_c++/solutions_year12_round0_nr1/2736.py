#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
#include<string.h>
#include<list>
#include<map>

using namespace std;
ifstream infile;
ofstream outfile;


int main(){
map<char, char> vals;
vals['a']='y';
vals['b']='h';
vals['c']='e';
vals['d']='s';
vals['e']='o';
vals['f']='c';
vals['g']='v';
vals['h']='x';
vals['i']='d';
vals['j']='u';
vals['k']='i';
vals['l']='g';
vals['m']='l';
vals['n']='b';
vals['o']='k';
vals['p']='r';
vals['q']='z';
vals['r']='t';
vals['s']='n';
vals['t']='w';
vals['u']='j';
vals['v']='p';
vals['w']='f';
vals['x']='m';
vals['y']='a';
vals['z']='q';

infile.open("A-small-attempt0.in");
outfile.open("out.out");
int tc;
infile>>tc;

for(int tcc=1; tcc<=tc; tcc++){
outfile<<"Case #"<<tcc<<": ";
char str[101];
if(tcc==1)infile.getline(str,100);
infile.getline(str,101);
int len=strlen(str);
for(int i=0; i<len; i++){
if(str[i]==' ')outfile<<str[i];
else outfile<<vals[str[i]];
}
outfile<<endl;
}

return 0;
}
