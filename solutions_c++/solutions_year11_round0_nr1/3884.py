#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int T;

int nO[1000];
int nB[1000];

int main()
{
  scanf("%d", &T);
  int N;
  for (int tt = 0; tt < T; tt++) {
    scanf("%d ", &N);
    memset(nO, -1, sizeof(nO));
    memset(nB, -1, sizeof(nB));
    for (int i = 0; i < N; i++)
    {
      char col;
      int pos;
      scanf("%c %d ", &col, &pos);
//      printf("%c %d ", col, pos);
      if (col == 'B')
      {
	nB[i] = pos;
      }
      else
      {
	nO[i] = pos;
      }
    }
//    printf("\n");
    int O = 1;
    int B = 1;
    int nextO = 1, nextB = 1;
    int ans = 0;
    for (int pos = 0; pos < N; pos++) {
      
      if (nO[pos] > -1)
      {
	nextO = nO[pos];
	for (int i = pos + 1; i < N; i++)
	{
	  if (nB[i] > -1) {
	    nextB = nB[i];
	    break;
	  }
	}

	//printf("nextsO: %d %d\n", nextO, nextB);
	
	int time = abs(nextO - O) + 1;
	ans += time;
	O = nextO;
	if (nextB < B) {
	  if (B - nextB < time) B = nextB;
	  else B -= time;
	}
	else {
	  if (nextB - B < time) B = nextB;
	  else B += time;
	}
	
	//printf("    takes %d: they're at %d %d\n", time, O, B);
      }
      
      else
	
      {
	nextB = nB[pos];
	for (int i = pos + 1; i < N; i++)
	{
	  if (nO[i] > -1) {
	    nextO = nO[i];
	    break;
	  }
	}

	//printf("nextsB: %d %d\n", nextO, nextB);
	
	int time = abs(nextB - B) + 1;
	ans += time;
	B = nextB;
	if (nextO < O) {
	  if (O - nextO < time) O = nextO;
	  else O -= time;
	}
	else {
	  if (nextO - O < time) O = nextO;
	  else O += time;
	}
	
	//printf("    takes %d: they're at %d %d\n", time, O, B);
	
      }
    }
    
    printf("Case #%d: %d\n", tt+1, ans);
  }
  return 0;
}