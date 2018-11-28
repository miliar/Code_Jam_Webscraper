#include <iostream>
using namespace std;

const int MAXN = 110;
char diamond[MAXN][MAXN];
int T, k;
char ch;
bool hsym[MAXN];
bool vsym[MAXN];
int mink;

int iabs(int x) {
  if(x >= 0) {
    return x;
  } else {
    return -x;
  }
}

int main(int argc, char *argv[]) {

  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    cin >> k >> ws;

    for(int i=0; i<2*k-1; i++) {
      for(int j=0; j<2*k-1; j++) {
        diamond[i][j] = ' ';
      }
    }
    for(int i=0; i<k; i++) {
      for(int j=0; j<=i; j++) {
        cin >> ch;
        diamond[i][k-1-i+2*j] = ch;
      }
    }
    for(int i=k; i<2*k-1; i++) {
      for(int j=0; j<(2*k-i-1); j++) {
        cin >> ch;
        diamond[i][k-1-(2*k-2-i)+2*j] = ch;
      }
    }



    //for(int i=0; i<2*k-1; i++) {
    //  for(int j=0; j<2*k-1; j++) {
    //    cout << diamond[i][j];
    //  }
    //  cout << endl;
    //}
    
    for(int i=0; i<2*k-1; i++) {
      hsym[i] = true;
      for(int j=0; j<2*k-1; j++) {
        for(int a=1; a<2*k-1; a++) {
          if(i+a < 2*k-1 && i-a >= 0 && diamond[i+a][j] != ' ' && diamond[i-a][j] != ' ' && diamond[i+a][j] != diamond[i-a][j]) {
            hsym[i] = false;
          }
        }
      }
    }
    for(int j=0; j<2*k-1; j++) {
      vsym[j] = true;
      for(int i=0; i<2*k-1; i++) {
        for(int a=1; a<2*k-1; a++) {
          if(j+a < 2*k-1 && j-a >= 0 && diamond[i][j+a] != ' ' && diamond[i][j-a] != ' ' && diamond[i][j+a] != diamond[i][j-a]) {
            vsym[j] = false;
          }
        }
      }
    }
    


    mink = -1;
    for(int i=0; i<2*k-1; i++) {
      for(int j=0; j<2*k-1; j++) {
        if(hsym[i] && vsym[j] && (mink == -1 || k + iabs(k-1-i) + iabs(k-1-j) < mink)) {
          mink = k + iabs(k-1-i) + iabs(k-1-j);
        }
      }
    }
      
    cout << "Case #" << t << ": " << (mink*mink - k*k) << endl;

  }
  
  return 0;
}
