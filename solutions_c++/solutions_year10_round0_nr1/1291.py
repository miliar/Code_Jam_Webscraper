#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <string.h>
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
#define FORN(i,n) FOR(i,0,(n))
#define FOR(i,a,n) for(int i=(a);i<(n);i++)
#define sz size()
#define PB push_back
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define PRESENT(container, element) (container.find(element) != container.end())
#define ALL(x) x.begin(), x.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define DIST(x1,y1,x2,y2) sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define ON 1
#define OFF 0

typedef  long long ull;


using namespace std;
int main(){
  ull T,n,k;

  cin >> T;
  int cases=1;
  
  while (T--){
    cin>>n>>k;
    ull t=0;
    ull m=0;
    while (k){
      if (k&1)t++;
      else break;
      k>>=1;
    }
    string ans="OFF";
    if (t>=n)ans="ON";
    printf("Case #%d: %s\n",cases++,ans.c_str());
  }
}












