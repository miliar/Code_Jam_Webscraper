#include <iostream>
#include <utility>
#include <vector>
#include <list>
using namespace std;

typedef pair<char, int> Evt;

void solve(int, int);

int main(void){
  int T, N;
  cin >> T;
  for(int i=1; i<=T; ++i){
    cin >> N;
    solve(i, N); // solve this test case
  }
  return 0;
}

void solve(int caseNo, int N){
  list<Evt> events;
  list<int> orng, blue;
  char ch; int t;
  
  // get input
  for(int i=0; i<N; ++i){
    cin >> ch >> t;
    events.push_back(Evt(ch,t));
    if('O' == ch)
      orng.push_back(t);
    else
      blue.push_back(t);
  }
  
  // simulate
  int curr_o = 1, curr_b = 1;
  int next_o = -1, next_b = -1;
  Evt next = events.front();
  if(!orng.empty()){
    next_o = orng.front();
    orng.pop_front();
  }
  if(!blue.empty()){
    next_b = blue.front();
    blue.pop_front();
  }
  int steps = 0;  // main answer
  int dir;
  bool doesHappen;  // pushing of button
  while(!events.empty()){
    ++steps;
    doesHappen = false;
    // orange's move
    if('O' == next.first && curr_o == next.second){
      doesHappen = true;
      next_o = -1;
      if(!orng.empty()){
        next_o = orng.front();
        orng.pop_front();
      }
    }else{
      // calculate direction of movement
      if(-1 == next_o || next_o == curr_o)
        dir = 0;
      else if(next_o > curr_o)
        dir = 1;
      else
        dir = -1;
      // move
      curr_o += dir;
    }
    // blue's move
    if('B' == next.first && curr_b == next.second){
      doesHappen = true;
      next_b = -1;
      if(!blue.empty()){
        next_b = blue.front();
        blue.pop_front();
      }
    }else{
      // calculate direction of movement
      if(-1 == next_b || next_b == curr_b)
        dir = 0;
      else if(next_b > curr_b)
        dir = 1;
      else
        dir = -1;
      // move
      curr_b += dir;
    }
    
    // if event happen, get next event
    if(doesHappen){
      events.pop_front();
      if(!events.empty())
        next = events.front();
    }
  }
  // print output
  cout << "Case #" << caseNo << ": " << steps << endl;
}
