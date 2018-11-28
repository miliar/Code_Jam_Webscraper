#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
 int t,n,s,a,r,p,x;
 fstream f,g;
 f.open("B-large.in",ios::in);
 g.open("output.out",ios::out);
 f>>t;
 for(int i=1;i<=t;i++)
 {
  f>>n>>s>>p; 
  r=0;       
  while(n--)
  {
    f>>a;
    switch(a%3)
    {
      case 0:x=a/3;
             if(x>=p)
               r++;
             
             else if((x+1)==p&&s&&x>0)
               {r++;s--;}
             break;
      case 1:x=(a/3)+1;
             if(x>=p)                      
              {r++;}
             break;
     case 2:x=(a/3)+1;
            if(x>=p)
             r++;
             else if((x+1)==p&&s)
               {r++;s--;}
             
             break;            
  }
  //cout<<a<<" "<<r<<endl;
 }
 g<<"Case #"<<i<<": "<<r<<endl;
}
 //system("pause");
 return 0;
} 
