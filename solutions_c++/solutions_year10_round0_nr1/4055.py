/*
 * Author: Landon LaSmith
 * Email: Landon.LaSmith@gmail.com
 */

#include <iostream>

using namespace std;


int main(int argc, char ** argv){
  int x, N;
  unsigned long int K, bitMask; 
  int totalCases;

  cin >> totalCases;

  for(x=1; x<=totalCases; x++){    
    cin >> N;
    cin >> K;

    bitMask = ~0;
    bitMask = ~(bitMask << N);

    cout << "Case #" << x << ": ";

    if((K & bitMask) == bitMask){
      cout << "ON\n"; 
    }else cout << "OFF\n";
  }

  return 0;
}
