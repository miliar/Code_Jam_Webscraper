// By mirosuaf and rogrog v.3.1
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=200;
int n,x;

int zrob(){
  int mini = INF, modsum=0,sum=0;
  scanf("%d", &n);
  REP(i,n){
    scanf("%d", &x);
    mini=min(x,mini);
    modsum ^= x;
    sum += x;
  }
  if(n<2||modsum!=0) return -1;
  return sum-mini;
}

int main() {
	int T; scanf("%d", &T); FOR(i,1,T) {
	  int res = zrob();
	  printf("Case #%d: ", i);
	  if(res==-1) printf("NO\n");
	  else printf("%d\n", res);
	}
	return 0;
}

