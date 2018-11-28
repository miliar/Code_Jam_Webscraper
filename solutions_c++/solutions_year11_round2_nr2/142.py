///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-05-07


#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;


int main(int argc, char ** argv){
  int trials;
  cin >> trials;
  for(int trial = 1; trial <= trials; trial++){
    int points;
    double D;
    cin >> points;
    cin >> D;
    double minDist, maxDist;
    vector< double > vstarts;
    for(int i = 0; i < points; i++){
      double point;
      cin >> point;
      int vendors;
      cin >> vendors;
      for(int j = 0; j < vendors; j++){
        vstarts.push_back(point);
      }
    }
    sort(vstarts.begin(), vstarts.end());

    double change = vstarts[0];
    double previous = 0;
    double tot = 0;
    for(int i = 1; i < vstarts.size(); i++){
      double dfromfirst = vstarts[i] - change;
      double dfromp = dfromfirst - previous;
      if(dfromp >= D){
        previous = dfromfirst;
      }else{
        double mov = D - dfromp;
        previous = mov + dfromfirst;
        if(mov > tot)
          tot = mov;
        //tot+=mov;
      }
    }

    double enddist = tot/(2.0f);
    cout << "Case #" << trial << ": " << setprecision(12) << enddist << endl;
  }
}
