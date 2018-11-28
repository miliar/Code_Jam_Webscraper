#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef long long i64_t;

int main()
{
  int N; cin >> N; cin.ignore();

  for (int n = 1; n <= N; ++n)
  {
	  unsigned N, K;
	  cin >> N >> K;
	  cout << "Case #" << n << ": ";
	  if ((K + 1) % (1 << N))
	  {
	  	  cout << "OFF";
	  } else {
		  cout << "ON";
	  }
	  cout << endl;
  }
  return 0;
}
