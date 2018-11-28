#include <iostream>

using namespace std;

#define MAX_T 10000
#define MAX_N 30
#define MAX_K 10000000

unsigned T, N, K;


pair<bool,bool> snappers[MAX_N];

int main () 
{
  cin >> T;
  for(unsigned t = 1; t <= T; ++t) {
    cin >> N >> K;
    unsigned long int aux = (0x01 << N);
    
    cout << "Case #" << t << ": ";
    if ((K % aux) == aux - 1) 
      cout << "ON" << endl;
    else
      cout << "OFF" << endl;  
  }
}
