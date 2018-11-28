#include<cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>
 
using namespace std;
 
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define SZ(x) ((int) (x).size())
#define FE(i,x) for(typedef((x).begin() i=(x).begin();i!=(x).end();i++) 

typedef long long int  int64;
typedef unsigned long long int uint64;
typedef long double ldb;
typedef pair <int, int> pii;
typedef vector<int>vi;
typedef vector<string>vs;
 

 
template <class T> T sqr (T x) {return x * x;}
int main()
{
  int cases;
  FILE *p=fopen("input.in","r");
  FILE *p2=fopen("output.txt","w");

  fscanf(p,"%d",&cases);

 int cs=0;  
  while(cases--)
  {
   int r,c;
   fscanf(p,"%d%d",&r,&c);
   char a[r+1][c+1];

   for(int i=0;i<r;i++)
     fscanf(p,"%s",a[i]);

  
   //for(int i=0;i<1;i++)
     //printf("%s\n",a[i]);


   int flag=0;

   for(int i=0;i<r-1;i++)
   {
     for(int j=0;j<c-1;j++)
     {
       if(a[i][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j]=='#'&&a[i+1][j+1]=='#')
       {
         a[i][j]='/';a[i][j+1]='\\';a[i+1][j]='\\';a[i+1][j+1]='/';
         //printf("hi\n");
       }
     }
   }

  flag=1;
  for(int i=0;i<r;i++)  
  {
    for(int j=0;j<c;j++)
    {
      if(a[i][j]=='#')
      {
        flag=0;break;
      }
    }
  if(flag==0) break;
  }
  fprintf(p2,"Case #%d:\n",++cs);
  if(flag==0) fprintf(p2,"Impossible\n");
  else
  {
    
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<c;j++)
      {
        fprintf(p2,"%c",a[i][j]);
      }
        fprintf(p2,"\n");
    }
  }
 
 /*
  for(int i=0;i<r;i++)
    {
      for(int j=0;j<c;j++)
      {
        printf("%c",a[i][j]);
      }
        printf("\n");
    }
  */
 }

fclose(p);
fclose(p2);

return 0;
}
 
