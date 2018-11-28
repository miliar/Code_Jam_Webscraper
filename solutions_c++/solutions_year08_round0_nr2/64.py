#include <iostream>
#include <queue>
using namespace std;
#define A 3
#define B 2
#define TRIPAB 1
#define TRIPBA 0
inline vector<int> mv(int x, int y, int z) {
  vector<int> ret = vector<int>(3);
  ret[0] = x, ret[1] = y, ret[2] = z;
  return ret;
}
inline int get_time(const string &s) {
  int hh, mm;
  sscanf(s.c_str(), "%d:%d", &hh, &mm);
  return 60*hh + mm;
}
int main() {
  int no_tests;
  cin >> no_tests;
  for (int rr = 1; rr <= no_tests; ++rr) {
    int na, nb, t, needa = 0, needb = 0, a = 0, b = 0;
    priority_queue< vector<int> > Q;
    cin >> t >> na >> nb;
    for (int i = 0; i < na; ++i) {
      string S, T;
      cin >> S >> T;
      int start = get_time(S), end = get_time(T);
      if (start == end)
	fprintf(stderr, "this shouldn't happen\n");
      Q.push(mv(-start, TRIPAB, -end));
    }
    for (int i = 0; i < nb; ++i) {
      string S, T;
      cin >> S >> T;
      int start = get_time(S), end = get_time(T);
      if (start == end)
	fprintf(stderr, "this shouldn't happen\n");
      Q.push(mv(-start, TRIPBA, -end));
    }
    while (Q.size()) {
      vector<int> next = Q.top();
      Q.pop();
      int t1 = -next[0], t2 = -next[2], mode = next[1];
      if (mode == A)
	a++;
      else if (mode == B)
	b++;
      else if (mode == TRIPAB) {
	if (a)
	  --a;
	else
	  needa++;
	Q.push(mv(-(t2 + t), B, -(t2 + t)));
      } else if (mode == TRIPBA) {
	if (b)
	  --b;
	else
	  needb++;
	Q.push(mv(-(t2 + t), A, -(t2 + t)));
      } else
	fprintf(stderr, "this shouldn't happen 2\n");
    }
    printf("Case #%d: %d %d\n", rr, needa, needb);
  }
  return 0;
}
