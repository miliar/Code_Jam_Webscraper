#include <iostream>

using namespace std;

int main()
{
  int T = 0;
  cin >> T;
  
  for(int i = 0; i < T; ++i)
  {
    short N = 0;
    cin >> N;
    unsigned long K = 0;
    cin >> K;

    unsigned long t = (1<<N) - 1;

    bool res = ((K & t) == t);

    cout << "Case #" << (i + 1) << ": " << (res ? "ON" : "OFF") << endl;
  }
  
  return 0;
}

