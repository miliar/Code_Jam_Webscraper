#include<iostream>
#include<map>
#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
map<char,char> letra;
int marca[100];
int main(){
  int n;
  char bas;
  string pal;
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  letra['q']='z';
  letra['z']='q';
  letra['e']='o';
  letra['j']='u';
  letra['p']='r';
  letra['m']='l';
  letra['y']='a';
  letra['s']='n';
  letra['l']='g';
  letra['c']='e';
  letra['k']='i';
  letra['d']='s';
  letra['x']='m';
  letra['v']='p';
  letra['n']='b';
  letra['r']='t';
  letra['i']='d';
  letra['b']='h';
  letra['t']='w';
  letra['a']='y';
  letra['h']='x';
  letra['w']='f';
  letra['f']='c';
  letra['o']='k';
  letra['u']='j';
  letra['g']='v';
  cin>>n;

  for(int i=0;i<n+1;i++){
    getline(cin,pal);
    if(i==0)continue;
    cout<<"Case #"<<i<<": ";
    for(int j=0;j<pal.size();j++){
      if(pal[j]==' '){ cout<<" ";continue;      }
      cout<<letra[pal[j]];
    }
    cout<<endl;
  }
  return 0;
}
