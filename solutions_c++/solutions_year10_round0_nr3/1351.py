#include <cassert>

#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <vector>


#include <boost/tuple/tuple.hpp>


using namespace std;
using namespace boost;


int main() {
  int T;
  cin >> T;
  
  for (int i = 0; i < T; ++i) {
    int R, K, N;
    cin >> R >> K >> N;
    vector<int> g(N);
    for (int j = 0; j < N; ++j) {
      cin >> g[j];
    }

    cout << "Case #" << i+1 << ": ";

    auto sum = accumulate(g.cbegin(), g.cend(), 0ULL);
    if (sum <= static_cast<unsigned long long>(K)) {
      cout << sum * R << endl;
      continue;
    }


    if (R < 4 * N) {
      auto pos = 0ULL;
      auto np = 0ULL;
      for (int j = 0; j < R; ++j) {
	int sum = 0;
	int k;
	for (k = 0; k < N && sum <= K; ++k) {
	  if (sum + g[(k+pos)%N] > K) {
	    break;
	  }
	  sum += g[(k+pos)%N];
	}
	pos = (pos+k) % N;
	np += sum;
      }
      cout << np << endl;
      continue;
    }

    auto pos = 0;
    int first_two = 0;
    bool flag = true;
    map<int, tuple<int, int, int> > m; // first, last, n_persons, ntimes
    for (int j = 0; j < 4 * N; ++j) {
      int sum = 0;
      int k = 0;
      for (k = 0; k < N && sum <= K; ++k) {
	if (sum + g[(k+pos)%N] > K) {
	  break;
	}
	sum += g[(k+pos)%N];
      }
      m[pos].get<0>() = (k+pos)%N;
      m[pos].get<1>() = sum;
      ++m[pos].get<2>();
      if (flag && m[pos].get<2>() == 2) {
	first_two = pos;
	flag = false;
      }
      pos = (k+pos)%N;
    }

    int cycle = 0;
    auto result = 0ULL;
    auto sumCycle = 0ULL;
    for (auto it = m.cbegin(), end = m.cend(); it != end; ++it) {
      if (it->second.get<2>() >= 2) {
	++cycle;
	sumCycle += it->second.get<1>();
      } else {
	result += it->second.get<1>();
      }
    }

    int newR = R - (m.size() - cycle);
    result += (newR/cycle) * sumCycle;
    newR %= cycle;
 
    pos = first_two;
    for (int j = 0; j < newR; ++j) {
      int sum = 0;
      int k = 0;
      for (k = 0; k < N && sum <= K; ++k) {
	if (sum + g[(k+pos)%N] > K) {
	  break;
	}
	sum += g[(k+pos)%N];
      }
      pos = (pos+k)%N;
      result += sum;
    }
    cout << result << endl;











  }

  return 0;
}
