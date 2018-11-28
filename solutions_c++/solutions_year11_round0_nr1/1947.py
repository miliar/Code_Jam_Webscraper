/* 
 * File:   bt.cc
 * Author: lewy
 *
 * Created on 7 maj 2011, 09:36
 */

#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

#define MAX_N 10000

int tab[MAX_N];

int tr[MAX_N];

int main()
{
 
  tr['O'] = 0;
  tr['B'] = 1;
  int d;
  scanf("%d", &d);
  for(int k = 1; k <= d; ++k){
    int n;
    scanf("%d", &n);
    long long lastTime[2];
    long long lastPosition[2];
    for(int s = 0;  s < 2; ++s){
      lastTime[s] = 0;
      lastPosition[s] = 1;
    }
    long long t = 0;
    for(int i = 0; i < n; ++i){
      char c;
      int p;
      cin >> c >> p;
      //cout << "oto c: " << c << " oto p: " << p << endl;
      int bot = tr[c];
      long long path = abs(p - lastPosition[bot]);
      if(lastTime[bot] + path < t){
        ++t;
        lastTime[bot] = t;
      }
      else{
        ++path;
        lastTime[bot] += path;
        t = lastTime[bot];
      }
      lastPosition[bot] = p;
    }
    cout << "Case #" << k << ": " << t << endl;
  }
  return 0;
}

