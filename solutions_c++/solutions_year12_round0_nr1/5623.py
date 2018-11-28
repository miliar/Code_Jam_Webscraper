#include<iostream>
//#include<conio.h>
#include<cstring>
#include<cstdlib>
#include<map>
using namespace std;
main()
{int t,te=0;
cin>>t;
map<char,char>m;
m['a']='y';m['b']='h';m['c']='e';m['d']='s';m['e']='o';m['f']='c';m['g']='v';m['h']='x';
m['i']='d';m['j']='u';m['k']='i';m['l']='g';m['m']='l';m['n']='b';m['o']='k';m['p']='r';
m['q']='z';m['r']='t';m['s']='n';m['t']='w';m['u']='j';m['v']='p';m['w']='f';m['x']='m';
m['y']='a';m['z']='q';m[' ']=' ';
while(++te<=t)
 {int i;cin.ignore();
  char str[250],outt[250];
  scanf("%[^\n]s",str);
 //cin>>str;
 
// cout<<str;
  int len=strlen(str);//cout<<" "<<len;
  for(i=0;i<len;i++)
       {//if(str[i]==' '){cout<<"str"<<str[i]<<" out"<<outt[i]<<"end";outt[i]==str[i];}else 
       outt[i]=m[str[i]];
       }
  outt[len]='\0';
  if(te!=t)
  cout<<"Case #"<<te<<": "<<outt<<"\n";
  else            
  cout<<"Case #"<<te<<": "<<outt;            
 }
      
      
}
