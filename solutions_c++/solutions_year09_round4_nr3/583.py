
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com
//Compiler used: g++ (GCC) 3.4.5 (mingw-vista special r3)

#include <algorithm>
#include <iostream>
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

using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl;
#define pb push_back

const int maxn=110;
const int maxk=30;

int n;
int k;

int p[maxn][maxk];
int a[maxn][maxn];

bool con(int i, int j) {
  for (int u=0;u<k;u++) if (p[i][u]==p[j][u]) return 1;
  if (p[i][0]>p[j][0]) swap(i,j);
  for (int u=1;u<k;u++)
    if (p[i][u]>p[j][u]) return 1;
  return 0;
}

int best=0;
int b[maxn];
void bt(int s, int cnt) {
  if (cnt>best) best=cnt;
  if (s>=n) return;
  if (n-s + cnt <= best ) return;
  for (int i=s;i<n;i++) {
    for (int j=0;j<cnt;j++) if (!a[i][b[j]]) goto fail;
    b[cnt]=i;
    bt(i+1, cnt+1);
  fail:;
  }
}

int solve( ){
  FOR (i,n)
    FOR (j,n) {
    if (con(i,j)) a[i][j]=1;
    else a[i][j]=0;
  }

  best=0;
  bt(0, 0);
  return best;
}

int main() {

  int nt;
  cin>>nt;
  for (int T=1;T<=nt;T++) {
    cin>>n>>k;
    FOR (i,n) FOR (j,k) cin>>p[i][j];
    int e=solve();
    cout<<"Case #"<<T<<": "<<e<<endl;
  }

  return 0;
}
