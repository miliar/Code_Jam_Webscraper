#include <cstdio>
#include <cstdlib>
#include <stack>
#include <map>
using namespace std;

int getTimeNeeded(int currPos, int tarPos) { return abs(tarPos - currPos); }

int main(int argc, const char *argv[])
{
  int T; //Number of cases

  scanf("%d\n", &T);

  for (int i = 0; i < T; i++) {
    int result = 0;
    int N = 0;        //Number of of buttons that need to be pressed
    int* R = NULL;    //Robot color is 'O'
    int* P = NULL;    //Button position

    scanf("%d\n", &N);

    R = new int[N];
    P = new int[N];

    for (int j = 0; j < N; j++) {
      char r_char;
      scanf("%c %d ", &r_char, &P[j]);
      R[j] = r_char == 'O'?1:0;
    }
    scanf("\n");

    int stopTime[] = {0, 0};
    int pos[] = {1, 1};
    for (int j = 0; j < N; j++) {
      int timeNeeded = getTimeNeeded(pos[R[j]], P[j]) + 1;
      int currBot = R[j];
      int anotherBot = R[j] ^ 1;
//printf("CurrBot: %d; AnotherBot: %d\n", currBot, anotherBot);
      pos[currBot] = P[j];
//printf("if timeNeeded(%d) >= stopTime(%d)\n", timeNeeded, stopTime[currBot]);
      if (timeNeeded <= stopTime[currBot]) {
        timeNeeded = 1;
      } else {
        timeNeeded -= stopTime[currBot];
      }
      stopTime[anotherBot] += timeNeeded;
      result += timeNeeded;
//printf("result=%d\n", result);
      stopTime[R[j]] = 0;
//printf("timeNeeded:%d,stopTime[%d:%d]\n\n", timeNeeded, stopTime[0], stopTime[1]);
    }

    printf("Case #%d: %d\n", i+1, result);

    //delete[] R;
    //delete[] P;
  }

  return 0;
}
