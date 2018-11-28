#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <set>
#include <limits>

using namespace std;

int main()
{

  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    
    int N;
    cin >> N;

    int min = std::numeric_limits<int>::max();
    int sum = 0;
    int xor_sum = 0;

    for (int j = 0; j < N; ++j) {
      int num;
      cin >> num;
      
      min = std::min(min, num);
      sum += num;
      xor_sum ^= num;
    }
    
    if (xor_sum != 0)
      cout << "Case #" << i+1 << ": NO" << endl;
    else
      cout << "Case #" << i+1 << ": " << sum - min << endl;
  }
  
  return 0;
}
