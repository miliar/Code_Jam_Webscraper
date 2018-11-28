
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <queue>
#include <stack>
#include <deque>
#include <complex>

using namespace std;

#define x1 fiwgiunb
#define x2 viosjosk
#define y1 fnwnfwgw
#define y2 jfowjgon
#define ws osgsogsg
#define free fnibfn


#define dbg(x) cerr << #x << " = " << x << endl
#define deb(x) cerr << #x << " = " << x << endl


#define all(c) (c).begin(),(c).end()
#define pb push_back
#define sz(c) (int)(c).size()          
#define mp make_pair
#define forn(i,n) for(int i=0;i<(int)n;++i)
#define ford(i,n) for(int i=(int)n;i>=0;--i)
#define X first
#define Y second
#define bits(x) __builtin_popcount(x)



typedef long long int64;
typedef long long ll;
typedef long double ld;



int a[29999];
int main()
{ 
  int t,n;
  cin >> t;
  forn(i,t)
  {
    printf("Case #%d: ",i+1);
    cin>>n;
    int rez=0;
    ll sum=0;
    int mn= 1<<30;
    forn(i,n)
      scanf("%d",&a[i]), rez^=a[i], sum += a[i], mn = min(mn,a[i]);
    if (rez!=0)
    {
      puts("NO");
    } else {
      printf("%I64d\n",sum-mn);
    }
    
  }
   
  return 0;
}
