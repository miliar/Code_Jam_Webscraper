#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <set>
#include <limits>

#define abs(x) ((x) > 0 ? (x) : -(x))

using namespace std;

int main()
{

  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {

    int N;
    cin >> N;

    int count = 0;
    for (int j = 0; j < N; ++j) {
      int n;
      cin >> n;
      
      if (n == j+1)
        ++count;
    }
    
    cout << "Case #" << i+1 << ": " << N - count << endl;
  }
  
  return 0;
}
