#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
  ifstream f("in", ios::in);
  if(!f.is_open()) {
    cout << "SCREAM: Invalid input file 'in'\n";
    return 0;
  }
  long int N;
  f >> N;
  for(long long i = 1; i <= N; ++i) {
    long int ans = 0;
    long int pb = 1;
    long int po = 1;
    long int timeElapsed = 0;
    long int tm = 0;
    long int M;
    bool prevBlue = false;
    bool prevOrange = false;
    f >> M;
    for(long int j = 0; j < M; ++j) {
      char color = 'x';
      long int num = 0;
      f >> color;
      f >> num;
      long long toTravel = num - po;
      if(color == 'o' || color == 'O') {
        toTravel = num - po;
        if(toTravel < 0)
          toTravel = toTravel * (-1);
        po = num;
        if(prevOrange) {
          tm = toTravel + 1;
        }
        else {
          if(toTravel > timeElapsed) {
            tm = (toTravel-timeElapsed)+1; // +1 for pressing button
          }
          else {
            tm = 1; // already there, just press button
          }
        }
        if(prevOrange) 
          timeElapsed += tm; 
        else
          timeElapsed = tm; 
        prevOrange = true;
        prevBlue = false;
      }
      if(color == 'b' || color == 'B') {
        toTravel = num - pb;
        if(toTravel < 0)
          toTravel = toTravel * (-1);
        pb = num;
        if(prevBlue) {
          tm = toTravel + 1;
        }
        else {
          if(toTravel > timeElapsed) {
            tm = (toTravel-timeElapsed)+1; // +1 for pressing button
          }
          else {
            tm = 1; // already there, just press button
          }
        }
        if(prevBlue) 
          timeElapsed += tm; 
        else
          timeElapsed = tm; 
        prevBlue = true;
        prevOrange = false;
      }
      ans += tm;
    }
    cout << "Case #" << i << ": " << ans << endl;
  }
  f.close();
}
