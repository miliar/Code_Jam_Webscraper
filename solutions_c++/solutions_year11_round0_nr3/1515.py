#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

int power[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
	       4096, 8192, 16384, 32768, 65536, 131072, 262144, 
	       524288, 1048576};

long summing(vector<int>& vec) {
  long sum = 0;
  for (unsigned i = 0; i < vec.size(); i++)
    sum += vec[i];
  return sum;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> num(N, 0);
    for (int i = 0; i < N; i++)
      cin >> num[i];
    sort(num.begin(), num.end());
    int maxx = num[N - 1];
    int digit = 0;
    while(maxx > 0) {
      digit++;
      maxx /= 2;
    }
    int pos;
    for (pos = 0; pos < digit; pos++) {
      int total = 0;
      for (int i = 0; i < N; i++) 
	total += num[i] / power[pos] % 2;
      if (total % 2 == 1)
	break;
    }
    cout << "Case #" << t << ": ";
    if (pos < digit)
      cout << "NO";
    else {
      cout << summing(num) - num[0];
    }
    cout << endl;
  }
  return 0;
}
