#include <iostream>
#include <stdio.h>
using namespace std;

int T, N, S, p;
string str;

int main(){

freopen("B-large.in", "r", stdin);
freopen("output.txt", "w", stdout);

cin >> T;

for(int j=0;j<T;j++){
cin >> N >> S >> p;

int maxG = 0;
int tScore;
int bestResultU;
int bestResultS;

for(int i=0;i<N;i++){
  cin >> tScore;
  if(tScore % 3 == 0){
    bestResultU = tScore/3;
    if(tScore > 0)
      bestResultS = bestResultU + 1;
    else
      bestResultS = 0;
  }
  else if(tScore % 3 == 1){
    bestResultU = bestResultS = tScore/3 + 1;
  }
  else {
    bestResultU = tScore/3 + 1;
    bestResultS = bestResultU + 1;
  }

  if(bestResultU >= p)
    maxG++;
  else if(bestResultS >= p && S > 0){
    maxG++;
    S--;
  }
}

cout << "Case #" << j+1 << ": " << maxG << endl;
}

return 0;
}
