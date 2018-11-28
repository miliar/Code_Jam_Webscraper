///////////////////////////////////////////////////////////
// Francisco J. Sanchez                                  //
///////////////////////////////////////////////////////////

#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
  int T, N, K;
  cin >> T;

  for (int i = 0; i < T; ++i){
    cin >> N;
    cin >> K;

    if(fmod(K, pow(2, N)) ==  pow(2, N)-1)
      cout << "Case #" << i+1 << ": " << "ON" << endl;
    else
      cout << "Case #" << i+1 << ": " << "OFF" << endl;
  }
  return 0;
}
