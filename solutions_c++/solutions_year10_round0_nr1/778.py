#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <vector>
using namespace std;
 
typedef long long LL;
 
#define MP make_pair
#define ST first
#define ND second
#define ALL(k) k.begin(),k.end()
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOREACH(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define SZ(a) (int)((a).size())

int main()
{
  int tst;
  cin >> tst;
  REP(j,tst)
  {
    LL n,k;
    cout << "Case #" << j+1 << ": ";
    cin >> n >> k;
    if( k == 0)
    {
      cout << "OFF" << endl;
      continue;
    }
    
    LL t = 1;
    t <<= (n);
    if( (k % t) == (t-1) ) 
    {
      cout << "ON" << endl;
    }
    else
    {
       cout << "OFF" << endl;
    }
  }

  return 0;
}
