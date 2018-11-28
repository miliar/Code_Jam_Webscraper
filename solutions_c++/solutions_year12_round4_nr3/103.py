#include <iostream>

using namespace std;

const int N_MAX = 3000;

int N;
long long heights[N_MAX];
int view[N_MAX];
bool possible;

void solve(int left, int right, int slope) {
  //cout << left << ", " << right << ", " << slope << endl;
  
  if (left == right)
    return;
  if (left + 1 == right) {
    possible = (view[left] == right);
    heights[left] = heights[right] - slope;
    return;
  }

  int first_see = right - 1;
  for (int i = left; i < right; i++) {
    if (view[i] > right) {
      possible = false;
      return;
    }
    if (view[i] == right) {
      first_see = i;
      break;
    }
  }

  solve(first_see + 1, right, slope + 1);
  heights[first_see] = heights[right] - slope * (right - first_see);
  solve(left, first_see, slope);
}

void solve_case(int case_num) {
  possible = true;
  cin >> N;
  for (int i = 0; i < N - 1; i++) {
    int x; cin >> x;
    view[i] = x - 1;
  }
  view[N - 1] = N - 1;  
  heights[N - 1] = 0;

  solve(0, N - 1, 0);
  if (!possible) {
    cout << "Case #" << case_num << ": Impossible\n";
    return;
  }

  long long min_height = heights[0];
  for (int i = 1; i < N; i++)
    min_height = min(min_height, heights[i]);
  cout << "Case #" << case_num << ":";
  for (int i = 0; i < N; i++)
    cout << " " << heights[i] - min_height + 1;
  cout << '\n';
}


int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve_case(i);
}
