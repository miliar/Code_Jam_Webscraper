#include <cstdio>
#include <cstdlib>
#include <stack>
#include <list>
#include <map>
using namespace std;

int main(int argc, const char *argv[])
{
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int T; //Number of cases

  scanf("%d\n", &T);
  for (int i = 0; i < T; i++) {
    long result = 0; //result
    int R = 0; //The roller coaster will run R times in a day.
    int k = 0; //The roller coaster can hold k people at once
    int N = 0; //Number of group
    int* g = NULL;
    int* numOfppl = NULL;
    int* nextG = NULL;

    scanf("%d %d %d\n", &R, &k, &N);
    //printf("%d %d %d\n", R, k, N);
    g = new int[N];
    numOfppl = new int[N];
    nextG = new int[N];
    for (int j = 0; j < N; j++) {
      scanf("%d", &g[j]);
      //printf("%d ", g[j]);
    }
    scanf("\n");
    //printf("\n");

    for (int j = 0; j < N; j++) {
      int index = j;
      int thisRoundPpl = g[index];

      //printf("%d::", index);
      if (N == 1) {
      } else {
        for (int z = 0; z < N; z++) {
          int nextIndex = (index+1)%N;

          if (thisRoundPpl > k) {
            thisRoundPpl -= g[index];
            //printf("(break@%d) ", index);
            break;
          } else if (thisRoundPpl == k) {
            //printf("(=%d:%d) ", index, g[index]);
            index = nextIndex;
            break;
          }
          //printf("(%d:%d) ", index, g[index]);
          if (z < (N-1)) {
            thisRoundPpl += g[nextIndex];
          }
          index = nextIndex;
        }
      }
      numOfppl[j] = thisRoundPpl;
      nextG[j] = index;
      //printf("Total: %d NextG:%d\n", thisRoundPpl, index);
    }

    int index = 0;
    for (int j = 0; j < R; j++) {
      //printf("%d:(%d) -> ", index, numOfppl[index]);
      result += numOfppl[index];
      index = nextG[index];
    }

    printf("Case #%d: %ld\n", i+1, result);
    delete[] g;
    delete[] numOfppl;
    delete[] nextG;
  }

  return 0;
}
