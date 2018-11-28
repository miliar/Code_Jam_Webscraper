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
#include <queue>

using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(a,v) memset((a),(v),sizeof(a)) 
vector<int> SplitInt(string &s)
{vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;}

int main ()
{
  freopen ("output.txt","w",stdout);
  int c,cas=1,n,q;
  scanf ("%d",&c);
  while (c--)
  {
    vector<int> a,b;
    scanf ("%d",&n);
    REP(i,n)
    {
      scanf ("%d",&q);
      a.PB(q);
      
    }
    REP(i,n)
    {
      scanf ("%d",&q);
      b.PB(q);
    }
    SORT(a);
    SORT (b);
    reverse(ALL(b));
    long long sum=0;
    REP(i,n)
      sum+=(long long)a[i]*(long long)b[i];
     cout<<"Case #"<<cas<<": "<<sum<<"\n";
     cas++;
  }
  fclose(stdout);
  //system("PAUSE");
  return 0;
}