#include <iostream>
#include <cstdio>

using namespace std;

int n;
int s;
int p;
int scores[100];
int group[100];

bool is_good_as_unsurprised(int x) {
  int u = x / 3;
  int r = x % 3;
  if (r > 0)
    ++u;
  return u >= p;
}


bool is_good_as_surprised(int x) {
  int u = x / 3;
  int r = x % 3;

  if (u > 0 && r == 0)
    u += 1;
  else if (r == 2)
    u += 2;
  else if (r == 1)
    u += 1;
  
  return u >= p;
}


int solve() {
  cin >> n >> s >> p;
  
  int class_a = 0;
  int class_b = 0;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    if (is_good_as_surprised(x))
      if (is_good_as_unsurprised(x))
        ++class_b;
      else
        ++class_a;
  }

  return class_b + std::min(s, class_a);
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << endl;
  return 0;
}
           
