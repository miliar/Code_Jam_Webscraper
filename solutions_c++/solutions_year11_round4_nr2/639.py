///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-06-04

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

double grid[501][501];

bool trycm(int bx, int by, int ex, int ey, double cx, double cy){
  double x = 0;
  double y = 0;
  for(int i = bx; i <= ex; i++){
    for(int j = by; j <= ey; j++){
      if(j == by || j == ey)
        if(i == bx || i == ex)
          continue;
      x += (((double)i) - cx) * grid[i][j];
      y += (((double)j) - cy) * grid[i][j];
    }
  }
  return ((x == 0) && (y == 0));
  
}

int main(int argc, char ** argv){
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; test++){
    int r,c;
    cin >> r;
    cin >> c;
    double d;
    cin >> d;
    for(int i = 0; i < r; i++)
      for(int j = 0; j < c; j++){
        char c = 0;
        while( ( c< '0' || c >  '9'))
          cin.get(c);
        grid[i][j] = c - '0';
      }
    int k = r;
    if(c < k)
      k = c;
    bool done = false;
    while(k > 2){
      //evens;
      if(k % 2 == 0){
        double kmod = k/2;
        kmod -= 0.5;
        for(int i = 0; i <= r-k; i++)
          for(int j = 0; j <= c-k; j++){
            if(trycm(i, j, i+k-1, j+k-1, i+kmod, j+kmod))
              done = true;
          }

      }else{
      //odds
        int start = k/2;
        int end   = r-start;
        for(int i = start; i < end; i++){
          int cend = c-start;
          for(int j = start; j < cend; j++){
            if(trycm(i-start, j-start, i+start, j+start, i, j))
              done = true;
          }
        }
      
      }
      if(done) break;
      k--;
    }
    if(k > 2){
      cout << "Case #" << test << ": " << k << endl;
    }else{
      cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    }
  }

}
