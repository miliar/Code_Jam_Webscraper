#include <cstdio>
#include <cstdlib>
#include <stack>
#include <map>
using namespace std;

int main(int argc, const char *argv[])
{
  int T; //Number of cases

  scanf("%d\n", &T);

  for (int i = 0; i < T; i++) {
    bool result = false;
    int N = 0;  //Number of Snapper devices
    int K = 0;  //Number of snap of finger

    scanf("%d %d\n", &N, &K);

    long mask = (1 << N) - 1;

    result = ((K & mask) == mask);
    //printf("N:%d K:%d, mask = %ld, result = %s(%d, %d)\n",
    //      N, K, mask, result?"true":"false", (K & mask), (K & 1));

    printf("Case #%d: %s\n", i+1, result?"ON":"OFF");

  }

  return 0;
}
