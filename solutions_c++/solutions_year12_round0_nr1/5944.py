#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
map<char,char>M;
string s;
void mapping(){

     M[' ']=' ';
     M['a']='y';
     M['b']='h';     
     M['c']='e';
     M['d']='s';               
     M['e']='o';
     M['f']='c';
     M['g']='v';                    
     M['h']='x';               
     M['i']='d';          
     M['j']='u';          
     M['k']='i';          
     M['l']='g';     
     M['m']='l';
     M['n']='b';          
     M['o']='k';                    
     M['p']='r';
     M['q']='z';                    
     M['r']='t';               
     M['s']='n';
     M['t']='w';     
     M['u']='j';               
     M['v']='p';                    
     M['w']='f';     
     M['x']='m';          
     M['y']='a';
     M['z']='q';

}

void f(){
     for(int i=0;i<s.size();++i)s[i]=M[s[i]];     
}

int main(){


     int t,it=1;     
     mapping();     

     
     cin>>t;          
     getline(cin,s);
          
          for(int i=1;i<=t;++i){

               getline(cin,s);
               f();                                   
               cout<<"Case #"<<i<<": "<<s<<"\n";
               
          }
     
     
     
}
