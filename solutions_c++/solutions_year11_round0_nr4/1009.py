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
  int tc;cin>>tc;
  for(int t=1;t<=tc;t++){
    int n,ans=0;cin>>n;
    REP(i,n){
      int x;cin>>x;
      if (x != i + 1) ans++;
    }
    printf("Case #%d: %d.000000\n",t,ans);
  }
  return 0;
}

