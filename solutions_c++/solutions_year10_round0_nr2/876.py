#include <iostream>
#include <fstream>

#include<algorithm>
using namespace std;
int gcd(int a,int b);

int gcd(int a,int b)
{
    if(b==0)return a;
    else return gcd(b,a%b);
    }

    
int main()
{
    long long  t,n,i,j,p,q,a[3],m,l,r,u,v,w,x;
    ifstream s;
    ofstream o("output1.txt");
    s.open("B-small-attempt4.in");
    s>>t;
    i=0;
    while(i<t)
    {
              s>>n;
              j=0;
              while(j<n)
              {
                        s>>a[j];
                        ++j;
                        }
                        sort(a,a+n);
                        if(n==3)
                        {
                                if(a[0]==a[1]||a[1]==a[2])
                                {
                                                          a[1]=a[2];
                                                          --n;
                                                          }
                                }
                                if(n==2)
                                {
                                        p=a[1]-a[0];
                                        if(p==1)
                                        {
                                                o<<"Case #"<<i+1<<": "<<0<<endl;
                                                ++i;
                                                continue;
                                                }
                                        m=1;
                                        x=p;
                                        while(x<a[0])
                                        {
                                                     ++m;
                                                     x=x+p;      
                                                     }
                                                     //cout<<m<<endl;
                                        o<<"Case #"<<i+1<<": "<<x-a[0]<<endl;
                                        ++i;
                                        continue;         
                                        }
                                  if(n==3)
                                  {
                                          p=a[1]-a[0];
                                          q=a[2]-a[1];
                                          r=a[2]-a[0];
                                          l=gcd(gcd(p,q),r);
                                          u=l;
                                          //o<<"Case #"<<i+1<<": "<<l<<endl;
                                          if(l==1)
                                          {
                                                o<<"Case #"<<i+1<<": "<<0<<endl;
                                                ++i;
                                                continue;  
                                                  }
                                                  m=1;
                                                  x=l;
                                                  while(x<a[0])
                                                  {
                                                               ++m;
                                                               x=x+l;
                                                               }
                                                               v=x-a[0];
                                                               //cout<<m<<endl;
                                                               //w=gcd(gcd(l/u,(a[1]+v)/u),(a[2]+v)/u);
                                                               o<<"Case #"<<i+1<<": "<<x-a[0]<<endl;
                                                               ++i;
                                                               continue;
                                          }                                                 
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
