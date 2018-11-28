#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <set>
#include <queue>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i<(b);++i)
#define EACH(x,v) for(typeof(v.begin()) x=v.begin();x<v.end();x++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mkp make_pair
#define sz size()
#define bset(i,j) (i&(1<<j))
#define INF (int)1e8
#define MAX 402
typedef long long LL;
typedef double D;
typedef vector<int> VI;
using namespace std;
int main()
{
  int t=GI, kase=1;
  while(t--) {
     int n=GI, a[n], b[n];
     REP(i,n) a[i]=GI;
     REP(i,n) b[i]=GI;
     sort(a,a+n);
     sort(b,b+n);
     reverse(b,b+n);
     LL sum=0;
     REP(i,n) sum+=(LL)a[i]*(LL)b[i];
     printf("Case #%d: %Ld\n", kase++, sum);
  }
  
  
  
  
}
