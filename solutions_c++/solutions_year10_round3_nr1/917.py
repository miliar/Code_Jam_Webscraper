#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pi;


int A[1010];
int B[1010];
int N;
int solve()
{
  int total_int = 0;
  for (int i = 0; i < N-1; i++) {
    for (int j = i+1; j < N; j++) {
      if (A[i] < A[j] && B[i] > B[j]) ++total_int;
      if (A[i] > A[j] && B[i] < B[j]) ++total_int;
    }
  }
  return total_int;
}

int main(int argc, char **argv)
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    memset(A, 0, sizeof(A));
    memset(B, 0, sizeof(B));
    cin >> N;
    for (int j = 0; j < N; j++) {
      cin >> A[j] >> B[j];
    }
    int res = solve();
    cout << "Case #" << i+1 << ": " << res << endl;
  }
  return 0;
}
