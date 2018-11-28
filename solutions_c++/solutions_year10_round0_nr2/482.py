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

#define SIZE 64

void converti(int *x, int n)
{
   int i;
   for(i=0; n; i++)
   {
      x[i]=n%10;
      n/=10;
   }
   for(; i<SIZE; x[i++]=0);
}

void converts(int *x, char *s)
{
   int i, j;
   for(j=strlen(s), i=0; i<j; x[i]=s[j-1-i]-'0', i++);
   for(; i<SIZE; x[i++]=0);
}

void copy(int *x, int *y)
{
   int i;
   for(i=0; i<SIZE; x[i]=y[i], i++);
}

int le(int *x, int *y, int len=SIZE)
{
   int i;
   for(i=len-1; i>=0 && x[i]==y[i]; i--);
   return i<0 || x[i]<y[i];
}

void sub(int *x, int *y, int len=SIZE)
{
   int i;
   for(i=0; i<len; i++)
      if((x[i]-=y[i])<0)
      {
         x[i+1]--;
         x[i]+=10;
      }
}

void division(int *q, int *r, int *x, int *y)
{
   int i;
   converti(q, 0);
   copy(r, x);
   for(i=SIZE-1; !y[i]; i--);
   for(i=SIZE-1-i; i>=0; i--)
      for(; le(y, r+i, SIZE-i); sub(r+i, y, SIZE-i), q[i]++);
}

void gcd(int *g, int *x, int *y)
{
   int q[64], r[64], i;
   for(i=0; i<64 && x[i]==0; i++);
   for(; i<64; )
   {
      division(q, r, y, x);
      copy(y, x);
      copy(x, r);
      for(i=0; i<64 && x[i]==0; i++);
   }
   copy(g, y);
}

void print(int *x)
{
   int i;
   for(i=SIZE-1; i>0 && !x[i]; i--);
   for(; i>=0; printf("%c", x[i--]+'0'));
}

int main()
{
   int T, t, n, i, j, x[64], y[64], z[64], g[64], q[64], r[64];
   char s[64][64];
   
   for(scanf("%d", &T), t=1; t<=T; t++)
   {
      scanf("%d", &n);
      fr(i,n) scanf("%s", s[i]);
      
      fr(i,64) g[i]=0;
      fr(i,n) fr(j,i)
      {
         converts(x, s[i]);
         converts(y, s[j]);
         if(le(x, y))
         {
            sub(y, x);
            copy(z, y);
         }
         else
         {
            sub(x, y);
            copy(z, x);
         }
         gcd(x, z, g);
         copy(g, x);
      }
      
      converts(x, s[0]);
      division(q, r, x, g);
      for(i=0; i<64 && r[i]==0; i++);
      if(i==64)
         printf("Case #%d: 0\n", t);
      else
      {
         sub(g, r);
         printf("Case #%d: ", t);
         print(g);
         printf("\n");
      }
   }
   
   return 0;
}
