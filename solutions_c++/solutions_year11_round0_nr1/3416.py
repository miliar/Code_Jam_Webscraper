#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <string>
#include <queue>
#include <map>
#include <bitset>
#include <climits>

#ifdef _DEBUG_MODE_
#define db(X) { cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl; }
#define db_arr(X) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrM(X, M) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrMN(X, M, N) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);++i)
#define ForL(i, m, n) for(i=(m);i<(n);++i)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

#define ArraySize(X) (sizeof(X)/sizeof(X[0]))

template <typename T> void xchg(T &a, T &b) { T c=a; a=b; b=c; }

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();

int main() {
  // COUNTER CODE STARTS HERE

  int T;
  cin >> T;

  for (int i=1; i<=T; ++i) {
    cout << "Case #" << i << ": ";
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW

void _main() {
  int N, i, j;
  char bot[101];
  int task[101];
  cin >> N;

  Clear(bot); Clear(task);
  
  For (i, N) {
    cin >> bot[i] >> task[i];
  }

  int currTask = 0, currTime = 0;
  int OBotPos = 1, OBotDest = -1, OBotTask = 0;
  int BBotPos = 1, BBotDest = -1, BBotTask = 0;
  bool pressed;

  while (currTask < N) {
    currTime++;
    pressed = false;
    // Get task
    while (OBotDest == -1 && OBotTask < N && bot[OBotTask] != 'O') {
      ++OBotTask;
    }
    if (OBotTask < N) {
      OBotDest = task[OBotTask];
    }

    while (BBotDest == -1 && BBotTask < N && bot[BBotTask] != 'B') {
      ++BBotTask;
    }
    if (BBotTask < N) {
      BBotDest = task[BBotTask];
    }

    // Press if possible
    if (OBotDest == OBotPos && currTask == OBotTask) {
      pressed = true;
      OBotDest = -1;
      ++OBotTask;
    }

    if (BBotDest == BBotPos && currTask == BBotTask) {
      pressed = true;
      BBotDest = -1;
      ++BBotTask;
    }

    // Move Bot
    if (OBotDest != -1) {
      if (OBotDest > OBotPos) {
	++OBotPos;
      } else if (OBotDest < OBotPos) {
	--OBotPos;
      }
    }

    if (BBotDest != -1) {
      if (BBotDest > BBotPos) {
	++BBotPos;
      } else if (BBotDest < BBotPos) {
	--BBotPos;
      }
    }
    
    if (pressed) {
      ++currTask;
    }
  }

  cout << currTime;
}
