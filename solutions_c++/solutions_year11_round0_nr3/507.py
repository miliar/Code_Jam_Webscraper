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
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");

  int n;
  FOR (test, tests){
    cin >> n;
    int a[n];
    FOR (i, n)
      cin >> a[i];
    sort(a, a + n);
    bool poss = true;
    FOR (bit, 30){
      int cnt = 0;
      FOR (i, n)
        cnt ^= (a[i] & (1 << bit)) != 0;
      poss &= (cnt ^ 1);
    }
    int s = 0;
    ffor (i, 1, n)
      s += a[i];
    cout << "Case #" << (test + 1) << ": ";
    if (poss)
      cout << s << "\n";
    else
      cout << "NO" << "\n";
  }
  return 0;
}
