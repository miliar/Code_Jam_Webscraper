/* 
 * File:   c.cc
 * Author: lewy
 *
 * Created on 7 maj 2011, 14:12
 */

#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  int d;
  scanf("%d", &d);
  for(int k = 1; k <= d; ++k){
    int n;
    scanf("%d", &n);
    int xorr = 0;
    long long mini = 99999999;
    long long  suma = 0;
    for(int i = 0; i < n; ++i){
      int a;
      scanf("%d", &a);
      suma += a;
      xorr ^= a;
      mini = min<long long>(mini, a);
    }
    cout << "Case #" << k << ": ";
    if(xorr){
      cout << "NO" << endl;
    }
    else
      cout << (suma - mini) << endl;
  }

  return 0;
}

