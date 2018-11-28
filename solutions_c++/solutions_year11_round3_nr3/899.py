#include <vector>
#include <iostream>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <iterator>
#include <set>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <string>
#include <stack>
#include <queue>

using namespace std;
using namespace std::tr1;

int main()
{
  int T;
  cin >> T;
  int L, H, N;
  
  for (int caseNumber = 1;caseNumber <= T;++caseNumber) {
    cin >> N >> L >> H;
    vector<int> others(N);
    for (int i =0;i< N;++i) {
      cin >> others[i];
    }
    int harmonies;
    int note;
    for (note = L;note <= H;++note) {
      harmonies = 0;
      for (int i = 0;i < N;++i) {
	if (note % others[i] == 0 || others[i] % note == 0) {
	  harmonies++;
	}
      }
      if (harmonies == N) {
	break;
      }
    }
    cout << "Case #" << caseNumber
	 << ": ";
    if (harmonies == N) {
      cout << note;
    } else {
      cout << "NO";
    }
    cout << endl;
  }
  return 0;
}
