#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

using namespace std;
#define iss istringstream
#define pb push_back
#define cs c_str()
#define frr(i,a,b) for(i=(a); i<(b); i++)
#define fr(i,n) frr(i,0,(n))
#define rrf(i,b,a) for(i=(b)-1; i>=(a); i--)
#define rf(i,n) rrf(i,(n),0)
#define sq(x,y,z) sqrt((x)*(x)+(y)*(y)+(z)*(z))
#define in(x,s) (s.find(x)!=s.end())
#define sv(x) sort(x.begin(),x.end())

int main()
{
   int T, t, R, K, n, x[1024], p[1024], e[1024], v[1024], i, j, k, f;
   long long total, sum[1024];
   
   for(scanf("%d", &T), t=1; t<=T; t++)
   {
      scanf("%d %d %d", &R, &K, &n);
      fr(i,n) scanf("%d", x+i);
      
      fr(i,n)
      {
         for(k=j=0; j<n && k<=K; k+=x[(i+j)%n], j++);
         if(k>K)
         {
            j--;
            k-=x[(i+j)%n];
         }
         e[i]=k;
         p[i]=(i+j)%n;
      }
      
      fr(i,1024) v[i]=-1;
      fr(i,1024) sum[i]=0;
      for(total=f=i=j=0; R; i++)
      {
         if(v[j]==-1 || f)
         {
            v[j]=i;
            R--;
            total+=e[j];
            j=p[j];
            if(!f)
               sum[i]=(i>0?sum[i-1]:0)+e[j];
         }
         else
         {
            total+=R/(i-v[j])*(sum[i-1]-(v[j]>0?sum[v[j]-1]:0));
            R%=i-v[j];
            f=1;
         }
      }
      
      printf("Case #%d: %lld\n", t, total);
   }
   
   return 0;
}
