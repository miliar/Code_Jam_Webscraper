/*
 * =====================================================================================
 *
 *       Filename:  b.cc
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  14.04.2012 12:57:03
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <iostream>
#include <algorithm>


using namespace std;




int main() {


  int d;
  cin >> d;
  for(int a = 1; a <= d; ++a) {
    int n, luck, mmin;

    int ret = 0;

    cin >> n >> luck >> mmin;
    for(int i = 1; i <= n; ++i){
      int k;
      cin >> k;
      if(k >= 3 * mmin - 2 && k >= mmin)
        ++ret;
      else if(k >= 3 * mmin - 4 && luck > 0 && k >= mmin) {
        --luck;
        ++ret;
      }
    }

    if(mmin > 10)
      ret = 0;
    
    cout << "Case #" << a << ": " << ret << endl;
  }
  return 0;
}
