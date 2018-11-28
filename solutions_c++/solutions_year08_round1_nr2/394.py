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
struct node {
       int n,type;
};
vector<node> demand[2500];

int mini;
int mustmalt[2500];
int toprint[2500];
int n,m;
bool satisfy() {
     //pf("mine %d\n",mini);
     int j,i;
     for(j=0;j<m;j++) {
      bool satisfy = false;
      for(i=0;i<demand[j].size();i++)
       if ( mustmalt[ demand[j][i].n ] == demand[j][i].type )
        satisfy = true;
       if ( !satisfy)
       re false;
     }
  return true;
}
void call(int u ) {
     if ( u > n ) {
        int sum = 0;
        int i;
        for(i=1;i<=n;i++) if ( mustmalt[i] ) sum++;
        if ( satisfy() )
          if ( sum < mini ) {
            mini = sum;
            for(i=1;i<=n;i++) toprint[i] = mustmalt[i];
           }
          re ;
     }
     mustmalt[u] = 1;
     call(u+1);
     mustmalt[u] = 0;
     call(u+1);      
}
int main() {
    int t;
    sf("%d",&t);
    int kase=1;
    
    while ( t--) {
          sf("%d %d",&n,&m);
          int i;
          for(i=0;i<2500;i++)
           demand[i].clear();
          int dnum;
          node temp;
          int j;
          for(j=0;j<m;j++) {
           sf("%d",&dnum);
           for(i=0;i<dnum;i++)
            sf("%d %d",&temp.n,&temp.type), demand[j].pb(temp);
           }
           mini = 5000; 
           call(1);
           pf("Case #%d:",kase++);
           if ( mini > n )
            pf(" IMPOSSIBLE\n");
           else {
                for (i=1;i<=n;i++)
                 pf(" %d",toprint[i]?1:0);
                pf("\n");     
           }  
    }
	return 0;
}
