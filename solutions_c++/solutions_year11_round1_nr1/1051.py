#include<iostream>

using namespace std;

long long gcd(long long a, long long b)
     {
          long long temp;
          if(a==0)
                  return 0;
          while(a!=0)
          {
                     b=(b%a);
                     temp=a;
                     a=b;
                     b=temp;
          }
          return b;
     }
     
int main()
    {
          long long t,n,pd,pg,a,b,y,z,k,i;
          cin>>t;
          for(i=0;i<t;i++)
          {
               k=0;
               cin>>n>>pd>>pg;
               a=gcd(pd,100);
               if(a==0)
                       k=1;
               else
               {
                       y=(100/a);
                       if(y>n)
                              k=1;
                       else
                       {
                              b=gcd(pg,100);
                              if(b==0)
                                      k=1;
                              else
                              {       
                                      if(pg==100 && pd<100)
                                                 k=1;
                              }       
                       }
               }
               if(pg==0 && pd==0)
                        k=0;
               if(k==0)
                       cout<<"Case #"<<i+1<<": Possible"<<endl;
               else
                       cout<<"Case #"<<i+1<<": Broken"<<endl;
          }
          return 0;
    }
