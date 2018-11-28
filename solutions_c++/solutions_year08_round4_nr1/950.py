#include<iostream>
#include<vector>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#define inf 10000000
using namespace std;

struct node
{
  int val,g,c;
};
int m;
node a[10005];
int b[10005];

int changeand(int i)
{
  if(i>m/2)
    return inf;
    if(b[i]!=-1)
      return b[i];
    
    if(a[i].val==1)
      return 0;
  int k,ans,lc=2*i,rc=2*i+1,x,y;
  if(a[i].c==1)
  {
    if(a[i].g==1 && (a[rc].val==1 || a[lc].val==1))
      {b[i]=1;
      return 1;
      }
   else
   {
       if(a[i].g==1)
       {
         x=changeand(lc);
         y=changeand(rc);
         b[i]=min(x,y)+1;
         return min(x,y)+1;
         
       }
       else if(a[i].g==0)
       {
         x=changeand(lc);
         y=changeand(rc);
         b[i]=min(x,y);
         return min(x,y);
       
       }
   
   }
  
  }
  else
  {
     if(a[i].g==1)
       {
        if(a[lc].val==0)
         x=changeand(lc);
        else
         x=0;
         
       if(a[rc].val==0)
         y=changeand(rc);
       else
         y=0;
         b[i]=x+y;
         return x+y;
         
       }
       else if(a[i].g==0)
       {
         x=changeand(lc);
         y=changeand(rc);
         b[i]=min(x,y);
         return min(x,y);
       
       }
  
  
  }
}

int cor(int i)
{
  
   if(i>m/2)
    return inf;
    if(b[i]!=-1)
      return b[i];
    
    if(a[i].val==0)
     {//cout<<i<<"slj";
      return 0;
      }
  int k,ans,lc=2*i,rc=2*i+1,x,y;
  if(a[i].c==1)
  {
    if(a[i].g==0 && (a[rc].val==0 || a[lc].val==0))
      {
    //  cout<<i<<"slj";
    b[i]=1;
      return 1;
      }
   else
   {
       if(a[i].g==0)
       {
         x=cor(lc);
         y=cor(rc);
          b[i]=min(x,y)+1;
       //  cout<<endl<<"i ="<<i<<" "<<x<<" "<<y<<endl;
         return min(x,y)+1;
         
       }
       else if(a[i].g==1)
       {
         x=cor(lc);
         y=cor(rc);
          b[i]=min(x,y);
        // cout<<endl<<"i ="<<i<<" "<<x<<" hi "<<y<<endl;
         return min(x,y);
       
       }
   
   }
  
  }
  else
  {
     if(a[i].g==0)
       {
       
         x=cor(lc);
         y=cor(rc);
          b[i]=x+y;;
     // cout<<endl<<"i ="<<i<<" "<<x<<" hi "<<y<<endl;
         return x+y;
         
       }
       else if(a[i].g==1)
       {
         x=cor(lc);
         y=cor(rc);
          b[i]=min(x,y);
        // cout<<endl<<"i ="<<i<<" "<<x<<" hi "<<y<<endl;
         return min(x,y);
       
       }
  
  
  }



}

int main()
{
int t,z=0;
  cin>>t;
  while(t--)
  {
    z++;
    int n,i,j,k,des,val,temp,ans;
    cin>>m>>des;
    
    for(i=1;i<=m/2;i++)
    {
      cin>>a[i].g>>a[i].c;
      b[i]=-1;
    }
    for(;i<=m;i++)
    {
       cin>>a[i].val;
       b[i]=-1;
    }
    i=m;
    while(i>1)
    {
      if(a[i/2].g==1)
      {
         temp=a[i].val&a[i-1].val;
      }
      else
        temp=a[i].val|a[i-1].val;
      a[i/2].val=temp;
      i-=2;
    }
    val=a[1].val;
   // cout<<"val="<<val<<endl;
    if(val==des)
     {
       printf("Case #%d: %d\n",z,0);
       continue;
     }
     
     if(val==0 && des==1)
     {
     // cout<<"hi11"<<endl;
        ans=changeand(1);
        if(ans>=inf)
         printf("Case #%d: %s\n",z,"IMPOSSIBLE");
         else
         printf("Case #%d: %d\n",z,ans);
         
         continue;
     }
     else
     { //cout<<"hi2"<<endl;
     
       ans=cor(1);
        if(ans>=inf)
         printf("Case #%d: %s\n",z,"IMPOSSIBLE");
         else
         printf("Case #%d: %d\n",z,ans);
         
          continue;
     
     
     }
    
  
  
  
  
  
  printf("Case #%d: %d\n",z,k);
  }
}
