#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back

using namespace std;

bool issqr (long long a)
{
  int j;
  long long i;
  long double x=(long double)a;
  for (i=((long long)sqrt(x))-5ll, j=0; j<10; j++, i++)
    if (i>=1ll && i*i==a)
      return 1;
  return 0;
}

int A[30], l;
char s[100];

int main()
{
  int t, cnt, i, j, e;
  long long n, m;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d ", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    cerr<<"test #"<<cnt<<endl;
    e=0, n=0ll;
    gets(s);
    l=strlen(s);
    for (i=0; i<l; i++)
    {
      if (s[i]=='?')
        A[e]=l-i-1, e++; //cerr<<A[e-1]<<endl;
      if (s[i]=='1')
        n+=(1ll<<(l-i-1));
    }
    for (i=0; i<(1<<e); i++)
    {
      m=n;
      for (j=0; j<e; j++)
        if ((i&(1<<j))!=0)
          m+=(1ll<<A[j]);
      //if (i==143)
      //cerr<<m<<" "<<n<<" "<<i<<endl;
      if (issqr(m))
      {
        printf("Case #%d: ", cnt);
        for (i=l-1; i>=0; i--)
          printf("%d", (int)((m&(1ll<<i))!=0ll));
        printf("\n");
        break;
      }
    } 
  }
  return 0;
}
