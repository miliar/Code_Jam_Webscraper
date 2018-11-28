#include<iostream>
#include<map>
using namespace std;

main()
{
      map<char,char>m;
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
      m['q']='z';//geja
      m['p']='r';
      m['d']='s';
      m['r']='t';
      m['j']='u';
      m['g']='v';
      m['t']='w';
      m['h']='x';
      m['a']='y';
      m['z']='q';//geja
      
      int t,i; char c;
      cin>>t; getchar();
      for(i=1;i<t+1;i++)
      {
          cout<<"Case #"<<i<<": ";   
          while((c=getchar())!='\n') 
          {
                           if(c==' ') putchar(c);
                           else putchar(m[c]);}
            if(i!=t)cout<<endl;
            }//end of tstcase
            }//end          
