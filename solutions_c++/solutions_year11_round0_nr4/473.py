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

int const MAXN=1003;
int n,x[MAXN];
//LL nieporzadki[MAXN];
//LL silnia[MAXN];
//double p[MAXN];

double zrob(){
  int sum=0;
  scanf("%d", &n);
  FOR(i,1,n) scanf("%d", &x[i]);
  FOR(i,1,n) {
      int p = i,l=0;
      while(x[p]!=0){
        int next = x[p];
        x[p] = 0;
        p = next;
        l++;
      }
      if(l>1) sum+=l;
  }
  return sum;
}

int main() {
  /*
  nieporzadki[0]=1;
  nieporzadki[1]=0;
  silnia[0]=1;
  silnia[1]=1;
  FOR(i,2,MAXN){
    nieporzadki[i] = (nieporzadki[i-1]+nieporzadki[i-2])*(i-1);
    silnia[i]=i*silnia[i-1];
  }
  p[0]=0;
  p[1]=0;
  FOR(i,2,MAXN){
    double suma = 0;
    FOR(j,2,i-1){
      suma += p[j] * ((silnia[i]/silnia[j])/silnia[i-j])*nieporzadki[j];
    }
    suma += silnia[i];
    p[i] = suma / (silnia[i] - nieporzadki[i]);
    printf("%d: %lf\n", i, p[i]);
  }*/

	int T; scanf("%d", &T); FOR(i,1,T) {
	  printf("Case #%d: %lf\n", i, zrob());
	}
	return 0;
}

