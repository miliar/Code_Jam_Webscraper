#include <iostream>
#include <vector>

using namespace std;

int A;
int B;

bool check(int i, int j) {
  int kr = 1;
  while (kr <= i) {
    kr *= 10;
  }
  kr /= 10;

  for ( int keta=10 ; i >= keta ; keta*=10, kr/=10 ) {
    int m = i % keta;
    if (m < (keta/10)) {
      continue;
    }
    int rot = (i/keta) + (m * kr);
    if ( rot == j ) {
      return true;
    }
  }
  return false;
}

int solve() {
  int res = 0;
  for (int i=A; i<B; ++i) {
    for (int j=i+1; j<=B; ++j) {
      if (i == j) {
	continue;
      }
      if (check(i,j)) {
	++res;
      }
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; ++tc) {
    cin >> A >> B;
    cout << "Case #" << tc << ": " << solve() << endl;
  }
}
