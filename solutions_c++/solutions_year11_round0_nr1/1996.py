#include <iostream>
#include <fstream>
using namespace std;
#define N_BUTTON 200
#define ORANGE 1
#define BLUE 2
ifstream fin("in.txt");
ofstream fout("out.txt");
int nTest;
int nButton;
int buttonPos[N_BUTTON], buttonBot[N_BUTTON];
char t_char;
void readInput() {
     fin >> nButton;
      int i;
      for (i=1;i<=nButton;++i) {
          fin >> t_char;
          if (t_char == 'O') {
             buttonBot[i] = ORANGE;      
          }
          else {
               buttonBot[i] = BLUE;
          }
          fin >> buttonPos[i];
      }
}

int oPos, bPos, oWait, bWait, c_dist;
int totalTime;
void init() {
     oPos = bPos = 1;
     oWait = bWait = 0;
     totalTime = 0;
}
int dist(int i, int j) {
    return i>=j ? i-j : j-i;
}
int main() {
    fin >> nTest;
    int i,j;
    for (j=1;j<=nTest;++j) {
          readInput();
          init();
          for (i=1;i<=nButton;++i) {
              if (buttonBot[i] == ORANGE) {
                 c_dist = dist(oPos,buttonPos[i]);
                 if (c_dist < oWait) {
                    oWait = 0;
                    oPos = buttonPos[i];
                    bWait = 1;//press the button
                    totalTime += 1;
                 }
                 else {
                      c_dist -= oWait;
                      oWait = 0;
                      oPos = buttonPos[i];
                      bWait += (1 + c_dist);//press the button + cover the remaining distance
                      totalTime += (1 + c_dist);
                 }
              }
              else {
                   c_dist = dist(bPos,buttonPos[i]);
                   if (c_dist < bWait) {
                      bWait = 0;
                      bPos = buttonPos[i];
                      oWait = 1; //press the button
                      totalTime += 1;
                   }
                   else {
                        c_dist -= bWait;
                        bWait = 0;
                        bPos = buttonPos[i];
                        oWait += (1 + c_dist);
                        totalTime += (1 + c_dist);
                   }
              }
          }
          fout <<"Case #"<<j<<": "<<totalTime<<"\n";
    }
    return 0;
}
