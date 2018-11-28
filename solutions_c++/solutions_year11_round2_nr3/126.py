#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>
 
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<climits>
 
#define oo            (int)13e7
#define s(n)          scanf("%d",&n)
#define sl(n)         scanf("%lld",&n)
#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define ull           unsigned long long
#define ll            long long
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb( z )       push_back( z )
#define gcd           __gcd
using namespace std;

int n, m;
int u[2048];
int v[2048];
vector< int > groups;
vector<int> adj[2048];
bool used[2048];
bool edge[2048][2048];

int dp[256];
int solve(int mask) {
  if (mask == (1<<n) - 1) {
    return 0;
  }
  int &ret = dp[mask];
  if (~ret)
    return ret;
  ret = -(int)1e9;
  for (int sub=0; sub < (1<<n); sub++) 
  if ( (sub&mask) == 0 ) {
    bool ok = 1;
    for (int j=0; j < groups.size(); j++) {
      if ( (groups[j] & sub) == 0 ) {
        ok = 0;
        break;
      }
    }
    if (ok) {
      ret = max(ret, 1 + solve(mask | sub));
    }
  }
  return ret;
}

void recon(int mask, vector<int> &sol, int id) {
  if (mask == (1<<n)-1) {
    for (int j=0; j < sol.size(); j++) {
      cout << sol[j];
      if (j + 1 == sol.size())
        cout <<endl;
      else
        cout << " ";
    }
    return;
  }
  int val = solve(mask);
  for (int sub=0; sub < (1<<n); sub++)
  if ( (mask & sub) == 0 ) {
    bool ok = 1;
    for (int j=0; j < (int)groups.size(); j++) {
      if ( (groups[j] & sub) == 0 ) {
        ok = 0;
        break;
      }
    }
    if (!ok) continue;
    int nval = 1 + solve( mask | sub );
    if (nval == val) {
      for (int x=0; x < n; x++)
      if (sub & 1 << x) {
        sol[x] = id;
      }
      return recon( mask | sub, sol, id + 1 );
    }
  }
}

inline void solveBF() {
  groups.clear();
  s(n); s(m);
  for (int i=1; i <= n; i++) {
    adj[i].clear();
    used[i] = 0;
    for (int j=1; j <= n; j++)
      edge[i][j] = 0;
  }
  for (int i=0; i < m; i++) s(u[i]);
  for (int i=0; i < m; i++) {
    s(v[i]);
    adj[ u[i] ].pb( v[i] );
  }
  
  for (int i=1; i <= n; i++) {
    if (i < n)
      adj[i].pb( i+1 );
    else
      adj[i].pb( 1 );
    sort(all(adj[i]));
    for (int j=0; j < adj[i].size(); j++) {
      //cout << i << " to " << adj[i][j] << endl;
      edge[ i ][ adj[i][j] ] = edge[ adj[i][j] ][ i ] = 1;
    }
  }
  
  
  //brute force begins
  for (int mask=1; mask < (1<<n); mask++) 
  if (bitcount(mask) > 2) {
    vector<int> vertices;
    for (int j=0; j < n; j++)
    if (mask & 1 << j) {
      vertices.pb( j+1 );
    }
    bool ok = 1;
    int N =vertices.size();
    for (int j=0; j < N; j++) {
        int nj = (j+1)%N;
        if (!edge[ vertices[j] ][ vertices[nj] ]) {
          ok = 0;
          if (mask == 11) {
              //cout << vertices[j] << " x-> " << vertices[nj] << endl;
          }
          break;
        }
        for (int k=0; k < N; k++) {
          if (k == (j-1+N)%N) continue;
          if (k == (j+1)%N) continue;
          if (k == j) continue;
          if (edge[vertices[j]][vertices[k]]) {
            if (mask == 11) {
              //cout << vertices[j] << " -> " << vertices[k] << endl;
            }
            ok = 0;
            break;
          }
        }
    }
    if (ok) {
      groups.pb( mask );
      //for (int i=0; i < vertices.size(); i++)cout << vertices[i] << " "; cout<<endl;
    }
  }
  fill(dp, -1);
  printf("%d\n", solve(0));
  vector<int> sol(n);
  return recon(0, sol, 1);
}

int main(int argc, char** argv) {
  freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
  //freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
  //freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
  
  //freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
  
  int runs;
  s(runs);
  for (int T=1; T <= runs; T++) {
    printf("Case #%d: ", T);
    solveBF();
  }
  
	return 0;
}
