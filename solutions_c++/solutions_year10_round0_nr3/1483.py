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

const int MAXN = 5000;

long long sum[MAXN], a[MAXN];
int R, k, n;

int main(){
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cin >> R >> k >> n;
    FOR (i, n)
      cin >> a[i];
    int used[n];
    SET(used, 255);
    int idx = 0, next, cnt = 0;
    sum[0] = 0;
    long long ss;
    while (true){
      ss = 0;
      next = idx;
      while (true){
        if (ss + a[next] > k)
          break;
        ss += a[next];
        next++;
        next %= n;
        if (next == idx)
          break;
      }
      
      sum[++cnt] = sum[cnt - 1] + ss;
      if (used[next] != -1)
        break;
      used[idx] = cnt;
      idx = next;
    }
    int ccnt = used[next];
    cout << "Case #" << (test + 1) << ": ";
    cout << (sum[ccnt - 1] + (sum[cnt] - sum[ccnt - 1]) * (1LL * (R - ccnt + 1) / (cnt - ccnt + 1)) + 
              sum[ccnt - 1 + (R - ccnt + 1) % (cnt - ccnt + 1)] - sum[ccnt - 1]) << endl;
  }

  return 0;
}
