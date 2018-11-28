#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) for(int i=0;i<(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    
    int cases;
    scanf("%d",&cases);
    REP(k,cases)
    {
      
      int n;
      scanf("%d",&n);            
      vector<int> v(n,0),w(n,0);
      REP(i,n) scanf("%d",&v[i]);
      REP(i,n) scanf("%d",&w[i]);
      /*
      printf("w : "); REP(i,n) printf("%d ",w[i]);
      printf("\n");
      printf("v : "); REP(i,n) printf("%d ",v[i]);
      printf("\n");
      */
      sort(ALL(w));
      sort(rALL(v));
      int c = 0;
      REP(i,w.size()) c+=w[i]*v[i];
      printf("Case #%d: %d\n",k+1,c);
      
    }
    
    
    
     return 0;
}

