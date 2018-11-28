#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())



int main()
{
  int i,j,k=0; char buf[10000];

  int n;
  scanf("%d",&n);
  for(k=1;k<=n;k++) {
     int B=0,C=0,D=0,E=0,S,N,p;
     scanf("%d %d %d",&N,&S,&p);
     for(j=0;j<N;j++) {
       int q;
       scanf("%d",&q);
       bool welsup = q>=2&& ((q+2>=3*p && (q+2)%3==0)||(q+4>=3*p && (q+4)%3==0)||(q+3>=3*p && (q+3)%3==0));
       bool nietsup = q+2>=3*p;
       if(!welsup && nietsup) B++;
       if(welsup && !nietsup) C++;
       if(welsup && nietsup) D++;
       if(!welsup && !nietsup && q>1) E++;
//printf("%d %d %d\n",q,welsup,nietsup);
     }

     printf("Case #%d: %d\n",k,B+D+min(S,C));
  }



  return 0;
}
