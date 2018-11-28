#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int t,i=0;
    int flag=0;
    int l=0;
    int x=0;
    char c[123];
    char d[101];
    
    c['a']='y';
    c['b']='h';
    c['c']='e';
    c['d']='s';
    c['e']='o';
    c['f']='c';
    c['g']='v';
    c['h']='x';
    c['i']='d';
    c['j']='u';
    c['k']='i';
    c['l']='g';
    c['m']='l';
    c['n']='b';
    c['o']='k';
    c['p']='r';
    c['q']='z';
    c['r']='t';
    c['s']='n';
    c['t']='w';
    c['u']='j';
    c['v']='p';
    c['w']='f';
    c['x']='m';
    c['y']='a';
    c['z']='q';
    cin>>t;
    x=t;
    //gets(d);
  //  fflush(stdin);
  cin.getline(d,101);
    while(t--)
    { 
              //for(i=0;i<101;i++)//initialise d.
              //d[i]='\0';
             // fflush(stdin);
              cin.getline(d,101);
              cout<<"Case #"<<x-t<<": ";
              for(i=0;d[i]!='\0';i++)
              {
              if(/*(d[i]>='A'&&d[i]<='Z')||*/(d[i]>='a'&&d[i]<='z'))
              {
               /*   if(d[i]>='A'&&d[i]<='Z')
                  {
                                          flag=1;
                                          d[i]=d[i]+32;
                  }
                  if(flag==1)
                  {
                  cout<<char(c[d[i]]-32);
                  }
                  else
                  {*/
                  cout<<c[d[i]];
              //    cout<<" in loop\n";
                  //}
                  //flag=0;
              }
              else
                  cout<<d[i];            
              }
    cout<<"\n";
    }  
    return 0;
}
              
              
