#include<iostream>

using namespace std;

long long abso(long long a,long long b)
    {
          if(a>=b)
                  return a-b;
          else
                  return b-a;
    }
    
int main()
    {
        long long t,n,prevo,prevb,i,k,m;
        long long curr,val;  
        cin>>t;
        for(k=1;k<=t;k++)
        {
                         cin>>n;
                         prevb=1;
                         prevo=1;
                         val=0;
                         curr=0;
                         char c[n];
                         long long v[n];
                         for(i=0;i<n;i++)
                         {
                                         cin>>c[i]>>v[i];
                                         if(c[i]=='O')
                                         {
                                                   m=abso(v[i],prevo);   
                                                   if(c[i-1]=='O' || i==0)
                                                   {
                                                                  val+=m+1;
                                                                  prevo=v[i];
                                                                  curr+=m+1;
                                                   }
                                                   else
                                                   {
                                                                  if(m<=curr)
                                                                  {
                                                                             val+=1;
                                                                             curr=1;
                                                                             prevo=v[i];
                                                                  }
                                                                  else
                                                                  {
                                                                             val+=(m+1-curr);
                                                                             curr=(m+1-curr);
                                                                             prevo=v[i];
                                                                  }
                                                   }
                                         }
                                         else
                                         {
                                                   m=abso(v[i],prevb);   
                                                   if(c[i-1]=='B' || i==0)
                                                   {
                                                                  val+=m+1;
                                                                  prevb=v[i];
                                                                  curr+=m+1;
                                                   }
                                                   else
                                                   {
                                                                  if(m<=curr)
                                                                  {
                                                                             val+=1;
                                                                             curr=1;
                                                                             prevb=v[i];
                                                                  }
                                                                  else
                                                                  {
                                                                             val+=(m+1-curr);
                                                                             curr=(m+1-curr);
                                                                             prevb=v[i];
                                                                  }
                                                   }
                                         }
                         }
                         cout<<"Case #"<<k<<": "<<val<<endl;
        }  
        return 0;
    }
