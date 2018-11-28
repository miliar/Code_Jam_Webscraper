#include <vector>
#include <iostream>
#include <utility>
#include <string>

#include <stdlib.h>

using namespace std;

int solve(vector<pair<int,int> >);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    vector<pair<int,int> > seq;
    int num_buttons;
    cin >> num_buttons;
    for(int j = 0; j < num_buttons; j++){
      string rb;
      int rbi, pos;
      cin >> rb >> pos;
      if(rb == string("B")) rbi = 0; else rbi = 1;
      seq.push_back(pair<int,int>(rbi,pos));
    }
    int r = solve(seq);
    cout << "Case #" << i+1 << ": " << r << endl;;
  }
}

int solve(vector<pair<int, int> > seq){
  int time = 0;
  vector<int> pos(2);
  pos[0] = 1;
  pos[1] = 1;
  pair<int, int> overlap(0, 0);
  for(size_t i = 0; i < seq.size(); i++){
    int rb = seq[i].first;
    int npos = seq[i].second;
    int movetime = abs(npos - pos[rb]);
    pos[rb] = npos;
    if(overlap.first == rb){
      time += (movetime + 1);
      overlap.second += (movetime + 1);
    } else {
      movetime -= overlap.second;
      if(movetime < 0) movetime = 0;
      time += (movetime + 1);
      overlap.first = rb;
      overlap.second = movetime + 1;
    }
  }
  return time;
}
