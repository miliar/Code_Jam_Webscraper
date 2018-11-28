#include<cstdio>
#include <iostream>
#include<math.h>
using namespace std;

int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int i,j;
    long long int A[50],B[50],count,m,n,a,b,c,d,e,f;
    long long int calculate(long long int number,int length,int x);
    cin>>j;
    for(i=0;i<j;i++)
    {
           cin>>A[i]>>B[i];                            
    }
    for(i=0;i<j;i++)
    {    
         count=0;
         n=A[i];
         m=B[i];
         while(m>n)
         {                
                          if(n<=9 && m>=1)
                          {
                                  n=10;
                                  }
         if(n<=99 && m>=10)
         {
                  a=calculate(n,2,1);
             
                  if(a>n && a<=m)
                  {
                        
                  count++;
                  }
                  n++;
                  }
                 
                  if(n<=999 && m>=100)
                  {
                 
                  a=calculate(n,3,1);
                  if(a>n && a<=m)
                  {
                  count++;
               
                  }
                  b=calculate(n,3,2);
                 
                  if(b>n && b<=m)
                  {
                   if(a!=b)
                         {      
                  count++;
                  
                  }}
                  n++;
                  }
                  
                  if(n<=9999 && m>=1000)
                  {
                  a=calculate(n,4,1);
                  if(a>n && a<=m)
                  {
                  
                  count++;
                  }
                  b=calculate(n,4,2);
                  if(b>n && b<=m)
                  {
                         if(a!=b)
                         {
               
                  count++;
                  }}
                  c=calculate(n,4,3);
                  
                  if(c>n && c<=m)
                  {
                         if(c!=b &&c!=a)
                         {
          
                  count++;
                  }}
                  n++;
                  }
                  if(n<=99999 && m>=10000)
                  {
                  a=calculate(n,5,1);
                  if(a>n && a<=m)
                  count++;
                  b=calculate(n,5,2);
                  if(b>n && b<=m)
                  {
                         if(a!=b)
                         {
                  count++;
                  }}
                  c=calculate(n,5,3);
                  if(c>n && c<=m)
                  {if(c!=b &&c!=a)
                         {
                  count++;
                  }}
                  d=calculate(n,5,4);
                  if(d>n && d<=m)
                  {
                         if(d!=a && d!=b && d!=c)
                  count++;
                  }
                  n++;
                  }
                  if(n<=999999 && m>=100000)
                  {
                  a=calculate(n,6,1);
                  if(a>n && a<=m)
                  count++;
                  b=calculate(n,6,2);
                  if(b>n && b<=m){
                  if(a!=b)
                  count++;}
                  c=calculate(n,6,3);
                  if(c>n && c<=m){
                  if(c!=b &&c!=a)
                  count++;}
                  d=calculate(n,6,4);
                  if(d>n && d<=m){
                  if(d!=a && d!=b && d!=c)
                  count++;}
                  e=calculate(n,6,5);
                  if(e>n && e<=m){
                  if(e!=a && e!=b && e!=c &&e!=d)
                  count++;}
                  n++;
                  }
                  if(n<=9999999 && m>=1000000)
                  {
                  a=calculate(n,7,1);
                  if(a>n && a<=m)
                  count++;
                  b=calculate(n,7,2);
                  if(b>n && b<=m){
                         if(a!=b)
                  count++;}
                  c=calculate(n,7,3);
                  if(c>n && c<=m){
                          if(c!=b &&c!=a)
                  count++;}
                  d=calculate(n,7,4);
                  if(d>n && d<=m){
                    if(d!=a && d!=b && d!=c)     
                  count++;}
                  e=calculate(n,7,5);
                  if(e>n && e<=m){
                  if(e!=a && e!=b && e!=c &&e!=d)
                  count++;}
                  f=calculate(n,7,6);
                  if(f>n && f<=m){
                  if(f!=a && f!=b && f!=c &&f!=d &&f!=e)
                  count++;}
                  n++;
                  }
                 
         }
          
                     cout<<"Case #"<<i+1<<": "<<count<<"\n";
                      
                     }
         
                     return 0;
                     }
                     long long int calculate(long long int number,int length,int x)
                     {
                          long long int temp1,temp2,temp3;
                          
                         
                          temp3=ceil(pow(10,(double)x));
                      
                          temp1=number%temp3;
                 
                          temp2=number/temp3;
                      
                          temp3=ceil(pow(10,(double)(length-x)));
                        
                         
                          return ((temp1*temp3)+temp2);
                      }
                     
