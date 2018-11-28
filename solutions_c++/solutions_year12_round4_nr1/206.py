
//Written by Alex H Ahmadi (alex@hamedahmadi.com)

#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl
#define pb push_back

#define zer(x) memset(x,0,sizeof(x));
#define isin(x,s) (s.find(x)!=s.end())

typedef long long ll;
typedef vector <int> vi;
typedef set <int> si;
typedef pair <int, int> pii;

const int maxn=10010;

//unsigned char mark[maxn][maxn];
int best[maxn];
int n;
int d[maxn];
int l[maxn];
int D;
bool dfound;

void dfs(int i, int j) {
  //cerr<<"dfs "<<i<<" "<<j<<endl;
  int dis=min(d[j]-d[i], l[j]);
  if (dis<=best[j]) return;
  best[j]=dis;
  if (D-d[j]<=dis) {
	dfound=1; return;
  }
  for (int k=j+1;k<=n;k++) {
	int e=d[k]-d[j];
	if (e>dis) break;
	dfs(j,k);
	if (dfound) return;	  
  }
}

void clear() {
  zer(best);
}

void solve(int cnum) {
  cin>>n;
  d[0]=0;
  l[0]=0;
  for (int i=1;i<=n;i++) {
	cin>>d[i]>>l[i];
  }
  cin>>D;

  dfound=0;

  dfs(0, 1);

  cout<<"Case #"<<cnum<<": ";

  if (dfound) cout<<"YES"<<endl;
  else cout<<"NO"<<endl;
}

int main() {
  int nt;
  cin>>nt;
  for (int cnum=1; cnum<=nt; cnum++) {
	clear();
	solve(cnum);
  }
  return 0;
}
