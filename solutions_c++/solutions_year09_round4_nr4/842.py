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

struct circtype
{
  double x,y,r;
};

int main() {
    int c;
    sf("%d",&c);
    int n;
    circtype myc[3];
    int kase=1;
    while ( c--)
    {
      pf("Case #%d: ",kase++);
      sf("%d",&n);
      int i;
      for(i=0;i<n;i++)
       sf("%lf %lf %lf",&myc[i].x,&myc[i].y,&myc[i].r);
      double ans=1e15;
      if( n== 1 )
      {
       pf("%.9lf\n",myc[0].r);
      }
      else if ( n==2 )
      {
           ans = max(myc[0].r,myc[1].r);
           pf("%.9lf\n",ans);
      }
      else {
        int j;
        for(i=0;i<3;i++)
         
          {
             j = (i+1)%3;
             double dia = sqrt( (myc[i].x-myc[j].x)*(myc[i].x-myc[j].x) + (myc[i].y-myc[j].y)*(myc[i].y-myc[j].y) );
                    dia =  dia + myc[i].r + myc[j].r;
             dia = dia/2;
          
             double minrad = max(dia, myc[ (j+1)%3 ].r);
             ans = min(ans,minrad);
          }
          pf("%.9lf\n",ans);
      }
    }
	return 0;
}
