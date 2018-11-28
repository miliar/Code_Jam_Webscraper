#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

// ./a.out < XXX.in.txt > XXX.out.txt

int main() {
  // read in the number of test cases
  int T;
  cin >> T;
  cin.get();

  // read in data for test cases
  for(int test=1; test<=T; test++) {
    char str[1000];
    stringstream ss;
    cin.getline(str, 1000);
    ss << str;
    
    int N;
    ss >> N;
    vector<int> orange;
    vector<int> blue;
    int total = 0, curpos[2]={1,1}, curmove=0;
    char currobot = '\0';
    for(int step=0; step<N; step++) {
      char robot;
      int pos;
      ss >> robot >> pos;
      if( currobot == '\0' ) currobot = robot;
      if( currobot == robot ) {
        curmove += (abs(pos - curpos[currobot=='B']) + 1); 
        curpos[currobot=='B'] = pos;
      } else {
        int move = abs(pos - curpos[robot=='B']);
        total += curmove;
        curmove = (curmove > move) ? 1 : (move-curmove+1);
        currobot = robot;
        curpos[currobot=='B'] = pos;
      }
    }
    total += curmove;

    cout << "Case #" << test << ": " << total << endl;
  }

  return 0;
}

