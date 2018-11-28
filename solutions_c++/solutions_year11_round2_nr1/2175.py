#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

using namespace std;

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 long t,m,c,co,count;
 char temp;
 char matrix[100][100];
 float wp[100];
 float owp[100];
 float oowp[100]; 
 cin>>t;
 for(long i = 0; i < t; i++)
 {
  for(int q = 0; q < 100; q++) wp[q] = 0;
  for(int q = 0; q < 100; q++) owp[q] = 0;
  for(int q = 0; q < 100; q++) oowp[q] = 0;
  printf("Case #%d:\n",i+1);
  cin>>m;
  for(int j = 0; j < m; j++)
  {
   c = 0;
   co = 0;
   for(int k = 0; k < m; k++)
   {
    cin>>matrix[j][k];
    if(matrix[j][k] != '.')
     c++;
    if(matrix[j][k] != '0' && matrix[j][k] != '.')
     co++; 
   }
   wp[j] = (float)co/c;
  }
  for(int j=0; j<m;j++)
  {   
   count = 0;
   for(int k=0; k<m;k++)
   {
    if(matrix[j][k] != '.')
    {
     count++;     
     c = 0;
     co = 0;
     for(int h=0; h<m;h++)
     {    
      if(matrix[k][h] != '.' && j!= h)
      {
       c++;
       if(matrix[k][h] != '0')
        co++;      
      }
     }
     owp[j]+= (float)co/c; 
    }     
   }
   owp[j]/=count;
  }
  for(int j=0; j<m;j++)
  {
   c = 0;
   for(int k=0; k<m;k++)
   {    
    if(matrix[j][k] != '.')
    {
     c++;
     oowp[j]+=owp[k];
    }
   }  
   oowp[j]/=c;    
  }
  for(int j=0; j<m;j++)
  {   
   printf("%.6f\n",(wp[j]*0.25+owp[j]*0.5+oowp[j]*0.25));  
  }
 }
 
 return 0;
}
