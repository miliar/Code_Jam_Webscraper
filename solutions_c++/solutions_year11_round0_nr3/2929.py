#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

#include <stdint.h>

using namespace std;

int main()
{
  uint16_t T;
  cin >> T;
  
  for(uint16_t ti = 0; ti < T; ti++)
  {
    uint16_t N;
    cin >> N;
    vector<uint32_t> C;
    C.resize(N);
    for(uint16_t ni = 0; ni < N; ni++)
    {
      cin >> C.at(ni);
    }

    sort(C.rbegin(), C.rend());

    uint32_t summed = 0, 
             xored = 0;
    for(uint16_t ni = 0; ni < N; ni++)
    {
      xored ^= C.at(ni);
      summed += C.at(ni);
    }
    summed -= C.at(N-1);

    if(xored != 0)
    {
      cout << "Case #" << (ti + 1) << ": NO" << endl;
    }
    else
    {
      cout << "Case #" << (ti + 1) << ": " << summed << endl;
    }
  }
  return 0;
}

