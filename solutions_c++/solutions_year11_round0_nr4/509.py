#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main(){
  freopen("Dl.out","wt", stdout);
  freopen("Dl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");

  int n;
  FOR (test, tests){
    cin >> n;
    int a[n];
    FOR (i, n){
      cin >> a[i];
      a[i]--;
    }
    bool vis[n];
    SET(vis, 0);
    int ret = 0;
    FOR (i, n){
      if (vis[i])
        continue;
      int cnt = 0, idx = i;
      while (a[idx] != i){
        idx = a[idx];
        vis[idx] = true;
        cnt++;
      }
      if (cnt)
        ret += cnt + 1;
    }
    cout << "Case #" << (test + 1) << ": ";
    cout << ret << ".000000" << "\n";
  }
  return 0;
}
