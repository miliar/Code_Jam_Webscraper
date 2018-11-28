#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf


int n;
int last[45];
int t;

int corrupt()
{
 int i;
 for(i=0;i<n;i++)
  if ( last[i]>i ) return i;
 return -1;
}
int main() {
    
    int kase=1;
    sf("%d",&t);
    while ( t--)
    {
     sf("%d",&n);
     int i,j;
     char line[100];
     for(i=0;i<n;i++)
     {
      sf("%s",line);
      //pf("%s\n",line);
      for(j=n-1;j>=0 && line[j]!='1'; j--);
      //pf("j = %d\n",j);
      last[i]=j;
     }
     int cnt=0;
     while( 1 )
     {
       int ci = corrupt();
       if ( ci==-1 )   br;
       cnt++;
       //pf("hekko");
       for( ; ci<n-1;ci++)
       {
        int ni = ci+1;
        if ( last[ni] < last[ci] ) // meaningful swap
         if ( last[ni]<= ci ) // corruptionless swap
         {
          swap(last[ni],last[ci]);
          br;
         }
       }
     }
     pf("Case #%d: %d\n",kase++,cnt);
    }
	return 0;
}
