// Marek Rogala; Code Jam 2012
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
#include <cstring>

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
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=2000000;
int repr[MAXN+100];
int cnt[MAXN+100];

// Funkcja wyznacza minimalną leksykograficzną równoważność cykliczną słowa
// za: Piotr Stanczyk, Algorytmika praktyczna
int minLexCyc(const char *x, int l) {
  int i = 0, j = 1, k = 1, p = 1, a, b;
  while (j + k <= (l << 1)) {
    if ((a = x[(i + k - 1) % l]) > (b = x[(j + k - 1) % l])) {
      i = j++;
      k = p = 1;
    } else if (a < b) {
      j += k;
      k = 1;
      p = j - i;
    } else if (a == b && k != p) k++;
    else {
      j += p;
      k = 1;
    }
  }
  return i;
}


void zrob(int testcase){
  int a,b;
  int min_r=INF,max_r=-1;

  cin >> a >> b;

  FOR(i,a,b){
    int r = repr[i];
    min_r = min(min_r,r);
    max_r = max(max_r,r);
    cnt[r]++;
  }
  long long result = 0;
  FOR(i,min_r,max_r){
    if(cnt[i]){
      result += cnt[i]*(cnt[i]-1)/2;
    }
    cnt[i]=0;
  }
	cout << "Case #"<<testcase<<": "<<result<<endl;
}


char buff[20],buff2[20];

int main() {

  FOR(i,1,MAXN){
    int x=i;
    sprintf(buff, "%d", i);
    int len = strlen(buff);
    int start = minLexCyc(buff,len);
    FOR(i,start,len-1){
      buff2[i-start]=buff[i];
    }
    FOR(i,0,start-1){
      buff2[i+len-start]=buff[i];
    }
    buff2[len]=0;
    sscanf(buff2,"%d", &x);
    repr[i]=x;
  }


  ios_base::sync_with_stdio(0);
	int T; cin >> T;
	for(int i=1;i<=T;i++) zrob(i);
	return 0;
}

