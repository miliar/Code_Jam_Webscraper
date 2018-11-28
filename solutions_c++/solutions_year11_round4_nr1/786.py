///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-06-04

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

struct ww{
  ww(double l, double s):
    length(l), speed(s)
  {

  }

  bool operator<(ww& other){
    return speed < other.speed;
  }

  bool operator<(const ww& other) const{
    return speed < other.speed;
  }

  double length, speed;

};

int main(int argc, char ** argv){
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; test++){
    double result;
    double clen;
    cin >> clen;
    double walks;
    cin >> walks;
    double runs;
    cin >> runs;
    double runt;
    cin >> runt;
    int numww;
    cin >> numww;
    vector<ww> walkways;
    double totalww=0;
    for(int i = 0; i  < numww; i++){
      double b, e, s;
      cin >> b;
      cin >> e;
      cin >> s;
      walkways.push_back(ww(e-b, s));
      totalww+=e-b;
    }
    walkways.push_back(ww(clen-totalww, 0));//add a walkway to represent the
    //rest  of the corridor

    sort(walkways.begin(), walkways.end());
    result = 0;
    for(vector<ww>::iterator iter =  walkways.begin();
        iter != walkways.end(); iter++){
      if(runt != 0){
        double rtime = iter->length / (runs + iter->speed);
        if(rtime <= runt){
          runt -= rtime;
          result += rtime;
        }else{
          double rd = (runs + iter->speed)*runt;
          double drem = iter->length - rd;
          double wtime = drem / (walks + iter->speed);
          result += runt;
          result += wtime;
          runt = 0;
        }
      }else{
        double wtime = iter->length / (walks + iter->speed);
        result += wtime;
      }
    }
    cout.precision(10);
    cout << "Case #" << test << ": " << result << endl;
  }

}
