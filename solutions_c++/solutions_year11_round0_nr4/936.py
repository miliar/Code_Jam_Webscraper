#include <cstdio>
#include <vector>

using namespace std;

//int vec[1005], pos[1005];
int N;

double probability (int count) {
  return 1.0*count;
  /*int count = 0;
  for (int i = 1; i < N; i++) {
    for (int j = i+1; j <= N; j++) {
      //printf ("%d %d\n", vec[i], vec[j]);
      if (vec[i] > vec[j])
        count++;
    }
  }
  for (int i = 1; i <= N; i++) {
    if (vec[i] != i) {
      printf ("a %d %d\n", vec[i], vec[pos[i]]);
      int ant = pos[i];
      vec[i] ^= vec[pos[i]];
      vec[pos[i]] ^= vec[i];
      vec[i] ^= vec[pos[i]];
      pos[i] = i;
      pos[vec[ant]] = ant;
      printf ("d %d %d\n", vec[i], vec[ant]);
      count++;
    }
  }
  return 2.0*count;*/
}

int main () {
  int T;
  scanf("%d", &T);
  
  for (int t = 1; t <= T; t++) {
    scanf ("%d", &N);
    int count = 0;
    for (int i = 1; i <= N; i++) {
      int n;
      scanf ("%d", &n);
      if (n != i)
        count++;
    }
    
    printf ("Case #%d: %lf\n", t, probability(count));
  }
  return 0;
}
