#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ostream>
#include <vector>

using namespace std;

char B = 'B';
char O = 'O';

// i is globTarget
int getTarget(char col, int i, vector<int> &p, vector<char> &r, int N, int curPos) {
  while(i < N) {
    if(r[i] == col)
      return p[i];
    i++;
  }
  
  return curPos;
}

bool metTarget(int globTarget, int bPos, int oPos, int bTarget, int oTarget, char color) {
  if(color == B) {
    if(bPos == bTarget)
      return true;
  } else if(color == O) {
    if(oPos == oTarget)
      return true;
  }
  
  return false;
}

int main() {
  int T, N;
  cin >> T;
  
  for(int i = 1; i <= T; i++) {
    vector<int> p;
    vector<char> r;
    cin >> N;
    char c;
    int button;
    for(int j = 0; j < N; j++) {
      cin >> c;
      cin >> button;
	  p.push_back(button);
      r.push_back(c);
    }

    // p is the button required
    // r is the robot required
    // p and r have lengths of N
    
    int bTarget, oTarget;
    int bPos = 1, oPos = 1;
    int globTarget = 0;
    int time = 0;
    
    while(globTarget < N) {
      bTarget = getTarget(B,globTarget,p,r,N,bPos);
      oTarget = getTarget(O,globTarget,p,r,N,oPos);
      char rTarget = r[globTarget];
      
      if(metTarget(globTarget, bPos, oPos, bTarget, oTarget, rTarget))
        globTarget++;
      
      if(bPos > bTarget) {
        bPos--;
      } else if(bPos < bTarget) {
        bPos++;
      }
    
      if(oPos > oTarget) {
        oPos--;
      } else if(oPos < oTarget) {
        oPos++;
      }
    
	  time++;    
    }
    
    cout << "Case #" << i << ": " << time << endl;
  }

  
  return 0;
}