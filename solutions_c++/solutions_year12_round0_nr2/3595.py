#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
 int t,n,s,a,r,p,x;
 fstream fs,gs;
 fs.open("B-large.in",ios::in);
 gs.open("output.txt",ios::out);
 fs>>t;
 for(int i=1;i<=t;i++)
 {
  fs>>n>>s>>p; 
  r=0;       
  while(n--)
  {
    fs>>a;
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
 }
 gs<<"Case #"<<i<<": "<<r<<endl;
}
 return 0;
} 
