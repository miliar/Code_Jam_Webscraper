//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
int T,n,s,p,a;
vector<int> v;

int nmax[40],smax[40];

int main() {
  for(int i = 7; i <= 30; i++)
    smax[i] = (i+4)/3;
  
  smax[0] = 0;
  smax[1] = 1;
  smax[2] = 2;
  smax[3] = 2;
  smax[4] = 2;
  smax[5] = 3;
  smax[6] = 3;
  
  for(int i = 0; i <= 30; i++)
    nmax[i] = (i+2)/3;
  
  // for(int i = 0; i <= 30; i++)
  //   printf("%d %d %d\n",i,nmax[i],smax[i]);
  

  cin >> T;
  for(int t = 1; t <= T; t++) {
    v.clear();
    scanf("%d %d %d",&n,&s,&p);
    for(int i = 0; i < n; i++) {
      scanf("%d",&a);
      v.PB(-a);
    }
    sort(v.begin(),v.end());
    for(int i = 0; i < SZ(v); i++) v[i]*=-1;
    int cnt=0;
    for(int i = 0; i < SZ(v); i++) {
      if(nmax[v[i]] >= p) cnt++;
      else if(smax[v[i]] >= p && s > 0) {
	s--;
	cnt++;
      }
    }
    printf("Case #%d: %d\n",t,cnt);
	  
  }
  
  return 0;
 
}
