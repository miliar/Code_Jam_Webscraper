#include <iostream>
#include <fstream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <complex>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define EACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define FOR(i,k,n) for (int i=(k);i<(int)(n);i++)
#define FEQ(i,k,n) for(int i=(k);i<=(int)(n);i++)
typedef long long ll;
typedef complex<double> P;

int main()
{
  int tc; scanf("%d",&tc);
  for(int t=1;t<=tc;t++){
    int n,l,h;scanf("%d%d%d",&n,&l,&h);
    int f[10000]; REP(i,n) scanf("%d",f+i);

    bool ok;
    for(int j=l;j<=h;j++){
      ok = true;
      REP(i,n){
        if (f[i] % j != 0 && j % f[i] != 0){
          ok = false;
          break;
        }
      }
      if (ok) {
        printf("Case #%d: %d\n",t,j);
        break;
      }
    }
    if (!ok) printf("Case #%d: NO\n",t);
  }
  return 0;
}
