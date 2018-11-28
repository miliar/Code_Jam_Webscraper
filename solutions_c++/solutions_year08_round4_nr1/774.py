#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <ext/hash_set>
#include <ext/hash_map>
using namespace std;

int points[10000];
int vals[10000];
int changeable[10000];
int M;




long long op(int node)
{
     
  //cout<<node<<endl;
  if(vals[node]!=-1)
   return vals[node];
  if(2*node+1>=M)
  {  vals[node]=points[node]; 
     return vals[node];
  } 
  if(points[node]==0)
    vals[node]=op(2*node+1)|op(2*node+2);
  else
    vals[node]=op(2*node+1)&op(2*node+2);
  return vals[node];
}


int hh(int a,int b)
{
    
    if(a==-1) return b;
    if(b==-1) return a;
    return min(a,b);
}
long long op2(int node)
{
     
 // cout<<node<<endl;
  if(vals[node]!=-1)
   return vals[node];
  if(2*node+1>=M)
  {  vals[node]=points[node]; 
     return vals[node];
  } 
  if(points[node]==0)
    vals[node]=op(2*node+1)&op(2*node+2);
  else
    vals[node]=op(2*node+1)|op(2*node+2);
  return vals[node];
}


long long res(int a,int b)
{
 if(2*a+1>=M)
   if(op(a)==b) return 0;
 else return -1;
   
   
 if(op(a)==b)
   return 0;
   
   
 if(changeable[a]&&op2(a)==b)
  return 1;

 int res1,res2;

 if(!changeable[a])
 {
   if(points[a]==1&&b==1)
   {
                        
     if(res(2*a+1,1)!=-1&&res(2*a+2,1)!=-1)          
       return res(2*a+1,1)+res(2*a+2,1);
     else
       return -1;
   }
   if(points[a]==1&&b==0)
   {
     if(res(2*a+1,0)!=-1||res(2*a+2,0)!=-1)          
       return hh(res(2*a+1,0),res(2*a+2,0));
     else
       return -1;
   }
   if(points[a]==0&&b==1)
   {
     if(res(2*a+1,1)!=-1||res(2*a+2,1)!=-1)          
       return hh(res(2*a+1,1),res(2*a+2,1));
     else
       return -1;
   }
   if(points[a]==0&&b==0)
   {
     if(res(2*a+1,0)!=-1&&res(2*a+2,0)!=-1)          
       return res(2*a+1,0)+res(2*a+2,0);
     else
       return -1;
   }   
 }   
 else
 {
   if(points[a]==1&&b==1)
   {
     if(res(2*a+1,1)!=-1&&res(2*a+2,1)!=-1)          
       res1= res(2*a+1,1)+res(2*a+2,1);
     else
       res1= -1;
   }
   if(points[a]==1&&b==0)
   {
     if(res(2*a+1,0)!=-1||res(2*a+2,0)!=-1)          
       res1= hh(res(2*a+1,0),res(2*a+2,0));
     else
       res1= -1;
   }
   if(points[a]==0&&b==1)
   {
     if(res(2*a+1,1)!=-1||res(2*a+2,1)!=-1)          
       res1= hh(res(2*a+1,1),res(2*a+2,1));
     else
       res1= -1;
   }
   if(points[a]==0&&b==0)
   {
     if(res(2*a+1,0)!=-1&&res(2*a+2,0)!=-1)          
       res1= res(2*a+1,0)+res(2*a+2,0);
     else
       res1= -1;
   }   
   if(points[a]==0&&b==1)
   {
     if(res(2*a+1,1)!=-1&&res(2*a+2,1)!=-1)          
       res2= res(2*a+1,1)+res(2*a+2,1);
     else
       res2= -1;
   }
   if(points[a]==0&&b==0)
   {
     if(res(2*a+1,0)!=-1||res(2*a+2,0)!=-1)          
       res2= hh(res(2*a+1,0),res(2*a+2,0));
     else
       res2= -1;
   }
   if(points[a]==1&&b==1)
   {
     if(res(2*a+1,1)!=-1||res(2*a+2,1)!=-1)          
       res2= hh(res(2*a+1,1),res(2*a+2,1));
     else
       res2= -1;
   }
   if(points[a]==1&&b==0)
   {
     if(res(2*a+1,0)!=-1&&res(2*a+2,0)!=-1)          
       res2= res(2*a+1,0)+res(2*a+2,0);
     else
       res2= -1;
   }
  // cout<<"node: "<<a<<" "<<res1<<" "<<res2<<endl;
   if(res2==-1)
     return res1;
   if(res1==-1)
     return res2+1; 
   return(min(res1,res2+1));
 }        
     
     
}


int main()
{
  int n;
  cin>>n;
  for(int i=0;i<n;i++)
  {
          
    long long V;
    cin>>M>>V;      
    cout<<"Case #"<<i+1<<": ";
    for(int j=0;j<M;j++)
      vals[j]=-1;
    for(int j=0;j<(M-1)/2;j++)
    {
      int a;
      cin>>a;
      points[j]=a;
      int b;
      cin>>b;
      changeable[j]=b;
    }
    for(int j=(M-1)/2;j<M;j++)
    {
      int a;
      cin>>a;
      points[j]=a;              
    }
    op(0);
   // for(int j=0;j<M;j++)
   //   cout<<"points[j]: "<<points[j]<<endl;
   // for(int j=0;j<M;j++)
   //   cout<<"vals[j]: "<<vals[j]<<endl;
    int c=res(0,V);
    if(c==-1)
      cout<<"IMPOSSIBLE"<<endl;
    else
      cout<<c<<endl;
  }


}
