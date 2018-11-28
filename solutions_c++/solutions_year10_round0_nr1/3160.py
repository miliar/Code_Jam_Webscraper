#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main(){

  int n, ncasos = 0;
  long int k, encend;

  cin >> ncasos;
  for (int i=0; i<ncasos; i++){
    cin >> n >> k;
    k++;
    cout << "Case #" << i+1 << ": ";
    encend = pow(2,n);
    if (k%encend == 0)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }

  return 0;
}
