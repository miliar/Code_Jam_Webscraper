/*
 * =====================================================================================
 *
 *       Filename:  c.cc
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  14.04.2012 18:53:48
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;


const int MAX_B = 2000020;

long long tab[MAX_B];

int count_digits(int s) {
  int ret = 1;
  while(s != 0) {
    s /= 10;
    ret *= 10;
  }
  return ret / 10;
}

int main() {
  
  int d;

  cin >> d;
  for(int k = 1; k <= d; ++k) {
    int a, b;
    cin >> a >> b;
    memset(tab, 0, sizeof(long long) * MAX_B);

    for(int i = a; i <= b; ++i) {
      int ccopy = i;
      int mmin = i;
      for(int s = 1; s <= 9; ++s) {
        int digit = ccopy % 10;
        ccopy = (ccopy / 10) + digit * count_digits(i);
        if(digit != 0) {
          mmin = min(mmin, ccopy);
        }
      }
      ++tab[mmin];
    }
    long long ret = 0;
    for(int i = 1; i < MAX_B; ++i)
      ret += (tab[i] * (tab[i] - 1ll)) / 2ll;
    cout << "Case #" << k << ": " << ret << endl;
  }

  return 0;
}
