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

int gcd(int a,int b)
{
  if(a==0) return b;
  else if(b==0) return a;
  else return gcd(b,a%b);
}

int main()
{
  
 
  int cases;
  FILE *p=fopen("input.in","r");
  FILE *p2=fopen("output.txt","w");

   fscanf(p,"%d",&cases);

   int cs=0;  
  while(cases--)
  {
   int n,l,h;
   fscanf(p,"%d%d%d",&n,&l,&h);
   int a[n+1];
   for(int i=0;i<n;i++)
      fscanf(p,"%d",&a[i]);

   int g=a[0];
   int m=a[0];   
   for(int i=0;i<n;i++)
   {
     //g=min(g,gcd(g,a[i]));
     m=m*(a[i])/gcd(m,a[i]);
     //printf("%d %d\n",g,m);
   }
    
  int count,flag=0;
   int ans=0;
   for(int i=l;i<=h;i++)
   {
      count=0;
      for(int j=0;j<n;j++)
      if(a[j]%i==0||i%a[j]==0) ++count;
      if(count==n) 
     {ans=i;flag=1;break;}
   }

  
   
   if(flag==0)
   fprintf(p2,"Case #%d: NO\n",++cs);
   else
   fprintf(p2,"Case #%d: %d\n",++cs,ans);
 }

 fclose(p);
 fclose(p2);
return 0;
}
 
