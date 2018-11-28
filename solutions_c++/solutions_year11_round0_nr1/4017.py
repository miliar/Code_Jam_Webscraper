#include <cstdio>
#include <vector>

using namespace std;

#define ABS(x) (((x) > 0) ? (x) : (-(x)))

int main() {
  int t;
  vector<pair<char, int> > input;

  scanf("%d\n", &t);
  for (int T = 0; T < t; ++T) {
    int n;
    scanf("%d", &n);
    input.clear();
    for (int i = 0; i < n; ++i) {
      char x;
      int y;
      scanf(" %c %d", &x, &y);
      input.push_back(make_pair(x ,y));
    }
    int pozo = -1, pozb = -1;
    int timeo = 0, timeb = 0;
    for (int i = 0; i < input.size(); ++i) {
      if (input[i].first == 'O') {
        if (pozo == -1) {
          timeo += input[i].second - 1;
        } else {
          timeo += ABS(input[i].second - input[pozo].second);
        }
        if (pozb > pozo && timeb > timeo) {
          timeo = timeb;
        }
        timeo++;
        pozo = i;
      } else {
        if (pozb == -1) {
          timeb += input[i].second - 1;
        } else {
          timeb += ABS(input[i].second - input[pozb].second);
        }
        if (pozo > pozb && timeo > timeb) {
          timeb = timeo;
        }
        timeb++;
        pozb = i;
      }
      fprintf(stderr, "%d %c %d %d %d\n", i, input[i].first, input[i].second, timeo, timeb);
    }
    if (timeo < timeb) timeo = timeb;
    printf("Case #%d: %d\n", T + 1, timeo);
  }
  return 0;
}
