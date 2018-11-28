#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int C, D;
    scanf("%d%d", &C, &D);
    vector<pair<int, int> > data;
    for(int i = 0; i < C; i++) {
      int V, P;
      scanf("%d%d", &P, &V);
      data.push_back(make_pair(P, V));
    }
    sort(data.begin(), data.end());

    long long pos = -1000000;
    long long cost = 0;
    for(int i = 0; i < C; i++) {
      long long costCur;
      if(pos > data[i].first) {
        pos = max(pos, (long long)data[i].first);
        costCur = (long long)pos - data[i].first;
      } else {
        pos = data[i].first;
        costCur = 0;
      }
      pos += (long long)data[i].second * D;
      costCur += (long long)(data[i].second-1) * D;
      cost = max (cost, costCur);
    }

    printf("Case #%d: %lf\n", t, (double)cost/2);
  }

}
