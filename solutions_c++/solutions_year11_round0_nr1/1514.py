#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

struct action {
  char robot;
  int position;
};

int N;
vector<action> move;

int seek(int pos, char robot) 
{
  while (pos < N && move[pos].robot != robot) pos++;
  return pos;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> N;
    action element;
    move.clear();
    for (int i = 0; i < N; i++) {
      cin >> element.robot >> element.position;
      move.push_back(element);
    }
    long total = 0;
    int pos = 0;
    int posO, posB, timeO, timeB;
    posO = posB = 1;
    while (pos < N) {
      timeO = seek(pos, 'O');
      timeB = seek(pos, 'B');
      if (timeO == N) {
	while (pos < N) {
	  total += abs(move[pos].position - posB) + 1;
	  posB = move[pos++].position;
	}
      } else if (timeB == N) {
	while (pos < N) {
	  total += abs(move[pos].position - posO) + 1;
	  posO = move[pos++].position;
	}
      } else {
	if (timeO < timeB) {
	  int timeNeed = abs(move[timeO].position - posO) + 1;
	  posO = move[pos++].position;
	  total += timeNeed;
	  if (move[timeB].position > posB &&
	      move[timeB].position - posB >= timeNeed) {
	    posB += timeNeed;
	  } else if (move[timeB].position < posB &&
		     posB - move[timeB].position >= timeNeed) {
	    posB -= timeNeed;
	  } else {
	    posB = move[timeB].position;
	  }
	} else {
	  int timeNeed = abs(move[timeB].position - posB) + 1;
	  posB = move[pos++].position;
	  total += timeNeed;
	  if (move[timeO].position > posO &&
	      move[timeO].position - posO >= timeNeed) {
	    posO += timeNeed;
	  } else if (move[timeO].position < posO &&
		     posO - move[timeO].position >= timeNeed) {
	    posO -= timeNeed;
	  } else {
	    posO = move[timeO].position;
	  }
	}
      }
    }
    cout << "Case #" << t << ": ";
    cout << total << endl;
  }
  return 0;
}
