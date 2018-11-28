#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

int main () {
  int T;
  int N;
  int S;
  int p;
  int points; 
  int winners;

  cin >> T;
  for(int t=0;t<T;t++){

    cin >> N;
    cin >> S;
    cin >> p;
    winners = 0;

    for ( int i=0;i<N;i++){
      //cin >> googlers[i];
      cin >> points;

      if( (points+min(2,points) )/3 >= p) { 
        winners++;
      } else if( ( S > 0) && ( (points+min(4,points)) /3 >= p) ){
        --S;    
        winners++;
      }       

    }
    
 
    cout << "Case #" << (t+1)  << ": " << winners << endl;

  }
  return 0;
}
