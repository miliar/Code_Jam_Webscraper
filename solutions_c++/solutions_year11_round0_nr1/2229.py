#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

#define ba "O"
#define bb "B"

struct seq{
  string h;
  int b;
};

void set_location(const seq& s, int *location){
  if (s.h.compare(ba) == 0)
    location[0] = s.b;
  else
    location[1] = s.b;
}

int calculate_moves(const seq& s, const seq& p, int* location, int& moves){
  int steps = 0;
  if (p.h.compare(s.h) == 0){
    steps = abs(s.b - p.b) + 1;
    moves += steps;
  } else {
    if (p.h.compare(ba) == 0){
      if (abs(s.b - location[1]) < moves)
        steps = 1;
      else 
        steps = abs(s.b - location[1]) - moves + 1;
    } else {
      if (abs(s.b - location[0]) < moves)
        steps = 1;
      else
        steps = abs(s.b - location[0]) - moves + 1;
    }
    moves = steps;
  }
  set_location(s, location);
  //cout<<steps<<endl;
  return steps;
}

int execute(vector<seq> sequence){
  if (sequence.size() == 0)
    return 0;

  int location[2] = {1, 1}, steps = 0, moves = 0;
  steps += sequence[0].b;
  moves = sequence[0].b;
  set_location(sequence[0], location);

  for (int i = 1; i < sequence.size(); ++i)
    steps += calculate_moves(sequence[i], sequence[i-1], location, moves);

  return steps;
}

int main(){
  int t; cin>>t;
  for (int count = 1; count <= t; ++count){
    int n; cin>>n;
    vector<seq> sequence;
    for (int i = 0; i < n; ++i){
      seq s; cin>>s.h; cin>>s.b;
      sequence.push_back(s);
    }
    cout<<"Case #"<<count<<": "<<execute(sequence)<<endl;
  }
}
