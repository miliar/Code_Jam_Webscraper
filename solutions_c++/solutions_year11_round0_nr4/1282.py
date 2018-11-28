#include <iostream>
#include <stdio.h>

#define MAX 1000

using namespace std;

int N, T;
int mat[MAX];
int unmarked[MAX];
int sum;

/** indexOf
    Returns the index of element x.
**/
int indexOf(int x) {
  for (int i = 1; i <= N; i++)
    if (mat[i] == x)
      return i;
}

/** Solve
 *  Parameter : x
 *
 *  Counts how large the cycle for x is.
 *  Marks all nodes visited as it finds this cycle.
 **/
void solve(int x) {
  int length = 1;
  for (int i = indexOf(x); i != x; i = indexOf(i)) {
    unmarked[i] = 0;
    length++;
  }
  if (length == 1) // already in order
    return;
  else  // Expect length many iterations to sort
    sum += length;
}

int main() {
  cin >> T;
  // For each test case
  for (int i = 0; i < T; i++) {
    cin >> N;
    // Reset expected value
    sum = 0;
    // Fill in array and mark all as unvisited
    for (int j = 1; j <= N; j++) {
      cin >> mat[j];
      unmarked[j] = 1;
    }
    for (int j = 1; j <= N; j++) {
      if (unmarked[j])
	solve(j);
    }
    printf("Case #%d: %d\n", i+1, sum);
  }
  return 0;
}

    
