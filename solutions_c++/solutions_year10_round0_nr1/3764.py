//Snappers
#include <iostream>
#include <math.h>
using namespace std;
int main(){
int cases,N,K;
cin >> cases;
for (int i = 1; i <= cases; i++){
  cin >> ws >> N >> ws >> K;
  if ((K+1) % (int)pow(2,N) == 0){
    cout << "Case #" << i << ": ON" << endl;
  }
  else {
    cout << "Case #" << i << ": OFF" << endl;
  }
  }
}
