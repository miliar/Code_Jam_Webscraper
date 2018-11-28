#include <map>
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

void solve (int a_case) {
  int N, S, p;
  cin >> N >> S >> p;

  int able = 0;
  int surprising = 0;
  for (int i = 0; i < N; ++i) {
    int score;
    cin >> score;

    if (score >= p && score >= p*3 - 4) {
      ++able;

      if (score < p*3 - 2) {
        ++surprising;
      }
    }
  }

  fprintf(stderr, "%d able, of which %d surprising. maximum %d\n", able, surprising, S);

  able -= surprising;
  able += std::min(surprising, S);

  printf("Case #%d: %d\n", a_case, able);
}

int main ()
{
  int n;

  cin >> n;
  for (int i = 0; i < n; ++i) solve(i+1);

  return 0;
}

