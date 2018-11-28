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

int area(int x0,int y0,int x1,int y1,int x2,int y2) {
   int val = x0*(y1-y2)+ x1*(y2-y0)+x2*(y0-y1);
   re abs(val);
} 

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t,kase=1;
    sf("%d",&t);
    while ( t-- ) {
          int ans = -1;
          int n,m,a;
          int x1,x2;
          int y1,y2;
          sf("%d %d %d",&n,&m,&a);
          for(x1=0;x1<=n;x1++)
           for(x2=0;x2<=n;x2++)
            for(y1=0;y1<=m;y1++)
             for(y2=0;y2<=m;y2++) {
                int mya = area(0,0,x1,y1,x2,y2);
                if ( mya == a) 
                { ans = 1; goto done; }
             }
            done: 
                  if ( ans == -1 ) {
                     pf("Case #%d: IMPOSSIBLE\n",kase++);
                  }
                  else {
                     pf("Case #%d: 0 0 %d %d %d %d\n",kase++,x1,y1,x2,y2);  
                  }
    }
	return 0;
}
