#include <iostream>
using namespace std;

int alt[100][100];
int dir[100][100];
int neighbors[5];
int sinki[100][100];
int sinkj[100][100];
int sinklisti[26];
int sinklistj[26];

int T,H,W;

int main(int argc, char *argv[]) {
  int s, S, ii, jj;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> H >> W;
    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        cin >> alt[i][j];
      }
    }

    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        neighbors[0] = alt[i][j];
        if(i>0) neighbors[1] = alt[i-1][j]; else neighbors[1] = alt[i][j];
        if(j>0) neighbors[2] = alt[i][j-1]; else neighbors[2] = alt[i][j];
        if(j<W-1) neighbors[3] = alt[i][j+1]; else neighbors[3] = alt[i][j];
        if(i<H-1) neighbors[4] = alt[i+1][j]; else neighbors[4] = alt[i][j];
        dir[i][j] = 0;
        for(int k=1; k<=4; k++) {
          if(neighbors[k] < neighbors[dir[i][j]]) dir[i][j] = k;
        }
      }
    }

    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        ii = i;
        jj = j;
        while(dir[ii][jj] != 0) {
          switch(dir[ii][jj]) {
            case 1:
              ii--;
              break;
            case 2:
              jj--;
              break;
            case 3:
              jj++;
              break;
            case 4:
              ii++;
              break;
          }
        }
        sinki[i][j] = ii;
        sinkj[i][j] = jj;
      }
    }

    cout << "Case #" << t << ":" << endl;
    S = 0;
    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        for(s=0; s<S; s++) {
          if(sinki[i][j] == sinklisti[s] && sinkj[i][j] == sinklistj[s]) {
            cout << ((char) ('a'+s)) << ' ';
            break;
          }
        }
        if (s==S) {
          sinklisti[S] = sinki[i][j];
          sinklistj[S] = sinkj[i][j];
          cout << ((char) ('a'+S)) << ' ';
          S++;
        }
      }
      cout << endl;
    }
  }
  
  return 0;
}
