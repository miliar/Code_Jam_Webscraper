#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int N, NA, NB, T, a, b, c, d;
  vector<pair<int, pair<int, bool> > > hora;
  int pai[1001];
  bool usado[1001];
  scanf("%d\n", &N); 
  for(int caso = 1; caso <= N; ++caso) {
    scanf("%d\n", &T);
    scanf("%d %d\n", &NA, &NB);
    hora.clear();
    memset(usado, false, sizeof(usado));
    for(int i = 0; i < NA; ++i) {
      scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
      hora.push_back(make_pair(a * 60 + b, make_pair(c * 60 + d + T, true)));
    }
    for(int i = 0; i < NB; ++i) {
      scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
      hora.push_back(make_pair(a * 60 + b, make_pair(c * 60 + d + T, false)));
    }
    sort(hora.begin(), hora.end());
    int tam = hora.size();
    for(int i = 0; i < tam; ++i) {
      pai[i] = -1;
      usado[i] = false;
      for(int j = 0; j < i; ++j) {
        if(!usado[j] && hora[i].second.second != hora[j].second.second && hora[i].first >= hora[j].second.first) {
          pai[i] = j;
          usado[j] = true;
          break;
        }
      }
    }
    NA = NB = 0;
    for(int i = 0; i < tam; ++i) {
      if(pai[i] == -1) {
        if(hora[i].second.second) ++NA;
        else ++NB;
      }
    }
    printf("Case #%d: %d %d\n", caso, NA, NB);
  }
  return 0;
}
