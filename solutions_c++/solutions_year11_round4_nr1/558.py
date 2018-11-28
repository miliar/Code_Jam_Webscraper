#include<iostream>
#include<set>
#include<stack>
#include<string>
#include<sstream>
#include<numeric>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long ll;
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
pair<int, pair<int, int> > gap[2001];
int x, s, r, n;
double t;
int sz;
pair<double, double> v[2000];

bool cmp(const pair<double, double>& A, const pair<double, double>& B){
  return A.second * (r + B.first) > B.second * (r + A.first);
}
double halla(){
    double res = 0;
    double tt = t;
    for(int i = 0; i < sz; i++){
      double corre = min(t, v[i].second / (v[i].first + r));
      double avanza = corre * (v[i].first + r);
      double falta = v[i].second - avanza;
      t -= corre;
      res += corre;
      double camina = falta / (v[i].first + s);
      res += camina;
    }
    t = tt;
    return res;
}
int main(){
  int tt; scanf("%d", &tt);
  for(int caso = 1; caso <= tt; caso++){
    cin >> x >> s >> r >> t >> n;

    for(int i = 0; i < n; i++) cin >> gap[i].second.first >> gap[i].second.second >> gap[i].first;
    sort(gap, gap + n);

    int suma = x;
   sz = 0;
    for(int i = 0; i < n; i++)
        suma -= gap[i].second.second - gap[i].second.first,
        v[sz++] = mp(gap[i].first, gap[i].second.second - gap[i].second.first);
    
    v[sz++] = mp(0, suma);
    sort(v, v + sz, cmp);
    double res = halla();
    sort(v, v + sz);
    res = halla();
    cout << "Case #" << caso << ": ";
    printf("%.08f\n", res);

  }
}

