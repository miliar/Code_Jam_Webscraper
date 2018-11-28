#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <climits>

using namespace std;
typedef long long int64;

#define maxn 25
int P[maxn],V[maxn];
int n,m;

bool gd(double t){
  double last = -1e9;
  for(int i=0;i<n;++i){
     for(int j=0;j<V[i];++j){
       double sx = P[i]-t;
       double ex = P[i]+t;
       if(sx-last+1e-6>m) {
          last = sx;
       }
       else if(ex-last+1e-6>m){
          last = last+m;
       }
       else return false;
     }
  }
  return true;
}

double search(){
  double s = 0; double e = 1e9;
  while(fabs(e-s)>1e-7){
     double t = (s+e)*0.5;
     if(gd(t)) e = t; 
     else s = t;
  }
  return (s+e)*0.5;
}

int main(){
  int tcase; scanf("%d",&tcase);
  for(int tc=1;tc<=tcase;++tc){
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;++i) scanf("%d%d",&P[i],&V[i]);
    printf("Case #%d: %.6lf\n",tc,search()); 
  } 
  return 0;
}
