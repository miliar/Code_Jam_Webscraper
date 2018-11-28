#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define x first
#define y second
#define rep(i,n) for(int i=0; i<int(n); i++)
#define INF 10000000

using namespace std;

typedef vector<int> vi;
typedef vector<vi>  vvi;
typedef pair<int,int> pii;
typedef long long ll;

vvi tree;
vi  gate;
vi  val;
vi  chan;
map<pii,int> memo;

int doit(int x, int v) {
   if (val[x] != -1) {
      if (val[x] == v) return 0;
      else             return -1;
   }
   if (memo.find(pii(x,v)) != memo.end()) return memo[pii(x,v)];
   int mini1 = INF;
   int mini2 = INF;
   int final = INF;
   // AND
   if (v == 1) {
      int res1 = doit(2*x, 1);
      int res2 = doit(2*x+1, 1);
      if (res1 != -1 and res2 != -1) {
         mini1 = min(mini1, res1 + res2);
      }                   
   }
   else {
      int res1 = doit(2*x, 0);
      int res2 = doit(2*x+1, 0);
      if (res1 != -1) mini1 = min(mini1, res1);
      if (res2 != -1) mini1 = min(mini1, res2);
   }
   // OR
   if (v == 1) {
      int res1 = doit(2*x, 1);
      int res2 = doit(2*x+1, 1);
      if (res1 != -1) mini2 = min(mini2, res1);
      if (res2 != -1) mini2 = min(mini2, res2);
   }
   else {
      int res1 = doit(2*x, 0);
      int res2 = doit(2*x+1, 0);
      if (res1 != -1 and res2 != -1) {
         mini2 = min(mini2, res1 + res2);
      }                   
   }
   if (chan[x] == 0) {
      if (gate[x] == 1) final = mini1;
      else              final = mini2;
   }
   else {
      if (gate[x] == 1) final = min(mini1,mini2+1);
      else              final = min(mini1+1,mini2);
   }
   if (final >= INF) final = -1;
   return (memo[pii(x,v)] = final);

}


int main() {
    int __N; cin >> __N;
    for (int Nc = 1; Nc <= __N; Nc++) {
        int M, V;
        cin >> M >> V;
        memo.clear();
        tree = vvi(M+1);
        gate = vi(M, -1);
        val = vi(M, -1);
        chan = vi(M,0);
        for (int i = 1; i <= M; i++) {
            if (i <= (M-1)/2) {
                tree[i].push_back(i*2);
                tree[i].push_back(i*2+1);
                cin >> gate[i];
                cin >> chan[i];
            }
            else {
                cin >> val[i];
            }
        }
        int res = doit(1,V);
        if (res == -1) cout << "Case #" << Nc << ": IMPOSSIBLE" << endl;
        else           cout << "Case #" << Nc << ": " << res << endl;
    }
}
