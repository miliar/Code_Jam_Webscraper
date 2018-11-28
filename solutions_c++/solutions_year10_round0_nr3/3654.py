// GoogleJam3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>

using namespace std;

int T;

int g[1001];

void coaster(int id) {
  int R, k, N;
  cin >> R >> k >> N;
  
  for (int i = 0; i < N; ++i) {
	  cin >> g[i];
  }
  
  int money = 0;
  int rounds;
  int curGroup = 0;

  for (rounds = 0; rounds < R; ++rounds) {
	  int space = k;
	  int startGroup = curGroup;
	  while (g[curGroup] <= space) {
		  space -= g[curGroup];
		  money += g[curGroup];
		  ++curGroup;
		  if (curGroup == N) {
			  curGroup = 0;
		  }
		  if (curGroup == startGroup) {
			  space = 0;
		  }
	  }
  }

  cout << "Case #" << (id + 1) << ": " << money << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	cin >> T;

	for (int i = 0; i < T; ++i) {
		coaster(i);
	}
	return 0;
}

