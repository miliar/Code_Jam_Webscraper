#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<functional>
using namespace std;
const int INF=(1<<31)-1;
const double EPS=1e-8;
char str[60][60];
int T,n,K,steven;

void rotate()
{
  int i,j,k;
  for( i=0;i<n;i++)
  {
     vector<char>v;
     for( j=n-1;j>=0;j--)
     {
        if(str[i][j]!='.')v.push_back(str[i][j]);    
     }             
     j=n-1;
     for(k=0;k<v.size();k++)
     {
        str[i][j]=v[k];
        j--;                        
     }
     while(j>=0)str[i][j--]='.';   
  }        
}

bool check(int i,int j)
{
  if(i>=0&&i<n&&j>=0&&j<n)return true;     
  return false;   
}


bool find_red_blue()
{

   int i,j,k;
   bool red=false;
   bool blue=false;
   bool flag;
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)                 
     {
         char temp=str[i][j];
         if(temp=='.')continue;
         if(check(i+K,j-K))//1
         {
           flag=true;
           for(k=1;k<=K;k++)
           {
             if(temp!=str[i+k][j-k])flag=false;                
           } 
           if(flag)
           {
            
            if(str[i][j]=='R')red=true;
            else blue=true;        
           }                      
         }                                 
           
         if(check(i+K,j+K))//2
         {
           flag=true;
           for(k=1;k<=K;k++)
           {
             if(temp!=str[i+k][j+k])flag=false;                
           } 
           if(flag)
           {
            if(str[i][j]=='R')red=true;
            else blue=true;        
           }                      
         }
         
         if(check(i,j+K))//3
         {
           flag=true;
           for(k=1;k<=K;k++)
           {
             if(temp!=str[i][j+k])flag=false;                
           } 
           if(flag)
           {
            if(str[i][j]=='R')red=true;
            else blue=true;        
           }                      
         }
         
         if(check(i+K,j))//4
         {
           flag=true;
           for(k=1;k<=K;k++)
           {
             if(temp!=str[i+k][j])flag=false;                
           } 
           if(flag)
           {
            if(str[i][j]=='R')red=true;
            else blue=true;        
           }                      
         }
                              
     }               
   }  
   if(red&&blue)printf("Both\n");
   else if(red)printf("Red\n");
   else if(blue)printf("Blue\n");
   else printf("Neither\n");
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    steven=1;
    for(scanf("%d",&T);steven<=T;steven++)
    {
       scanf("%d%d",&n,&K);
       K--;
       for(int i=0;i<n;i++)scanf("%s",str[i]);                                             
       rotate();
       //for(int i=0;i<n;i++)printf("%s\n",str[i]);
       printf("Case #%d: ",steven);
       find_red_blue();                                  
    }

    //system("pause");
    return 0;
}
