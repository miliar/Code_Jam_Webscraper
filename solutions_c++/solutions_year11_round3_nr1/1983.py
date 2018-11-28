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

char matrix[50][50];
int main()
{
 freopen("A-small-attempt0.in","r",stdin);
 freopen("a.out","w",stdout);
 long t;
 int r,c;
 bool err;
 cin>>t;
 for(long i = 0; i < t; i++)
 {
  cin>>r>>c;
  for(int j = 0; j < r; j++)
   for(int k = 0; k < c; k++)
    cin>>matrix[j][k];
  
  printf("Case #%d:\n",i+1);
  err = false;
  for(int j = 0; j < r; j++)
  {   
   for(int k = 0; k < c; k++)
   {
    if(matrix[j][k] == '#')
    {
     if(matrix[j][k+1] == '#' && matrix[j+1][k] == '#' && matrix[j+1][k+1] == '#')
     {
      matrix[j][k] = '/';
      matrix[j][k+1] = '\\'; 
      matrix[j+1][k] = '\\';
      matrix[j+1][k+1] = '/';
     }
     else
     {
      err = true;
      break;
     }
    } 
   }
   if(err == true)
   {
    printf("Impossible\n");
    break;       
   }
  }
  if(err == false)
  {
   for(int j = 0; j < r; j++)
   {
    for(int k = 0; k < c; k++)
     printf("%c",matrix[j][k]);
    printf("\n");      
   }
  }
 } 
 return 0;
}
