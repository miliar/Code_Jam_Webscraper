#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define inf (1 << 30)
int d[10000], l[10000], peso[10000];
int main(){
   int tt; cin >> tt;
   f(caso, 1, tt + 1){
      int n; cin >> n;
      f(i, 0, n) scanf("%d %d" ,d + i, l + i);
      int D; cin >> D;
      clr(peso, -1);
      priority_queue<pii> s; s.push(mp(d[0], 0)); peso[0] = d[0];
      bool can = false;
      while(!s.empty() && !can){
         int u = s.top().snd, w = s.top().fst; s.pop();
         if(peso[u] > w) continue;
         if(abs(d[u] - D) <= w) can = true;
         f(v, 0, n) if(abs(d[u] - d[v]) <= w){
            int npeso = min(l[v], abs(d[u] - d[v]));
            if(npeso > peso[v])
               peso[v] = npeso, s.push(mp(npeso, v));
         }
      }

      printf("Case #%d: %s\n", caso, can ? "YES" : "NO");
   }
}

