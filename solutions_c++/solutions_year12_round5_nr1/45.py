#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cmath>

using namespace std;
const int N_MAX = 4000;

int N;
int times[N_MAX];
int die_chance[N_MAX];
int perm[N_MAX];

bool comp(int x, int y) {
  if (times[x] * die_chance[y] == times[y] * die_chance[x])
    return x < y;
  return times[x] * die_chance[y] < times[y] * die_chance[x];
}

void solve_case(int case_num) {
  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> times[i];
  for (int i = 0; i < N; i++)
    cin >> die_chance[i];
  for (int i = 0; i < N; i++)
    perm[i] = i;
  sort(perm, perm + N, comp);
  cout << "Case #" << case_num << ":";
  for (int i = 0; i < N; i++)
    cout << " " << perm[i];
  cout << '\n';
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve_case(i);
}
