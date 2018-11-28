#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <cstring>
using namespace std;

#define all(v) (v).begin(), (v).end()
typedef unsigned long long ll;


ll getMaxNum(int p, vector<int> &q)
{
  ll maxsum = 1000000000;
  do {
    vector<bool> f(p, true);
    ll sum = 0;
    for (int i = 0; i < q.size(); i++) {
      f[q[i]-1 ] = false;
      for (int j = q[i]-2; j >= 0; j--) {
        if (f[j] == false) break;
        ++sum;
      }
      for (int j = q[i]; j < p; j++) {
        if (f[j] == false) break;
        ++sum;
      }
    }
    if (maxsum > sum) maxsum = sum;
  } while(next_permutation(all(q)));

  return maxsum;
}

int main(int argc, char **argv)
{
  if (argc < 2) {
    cerr  << "Usage: " << argv[0] << " <input file>\n";
    return 1;
  }
  ifstream fin(argv[1]);
  if (!fin) {
    cerr << "Could not open file " << argv[1] << endl;
    return 1;
  }
  int test;
  fin >> test;
  for (int i = 0; i < test; i++) {
    int p, q;
    fin >> p >> q;
    vector<int> v;
    for (int j = 0; j < q; j++) {
      int cell;
      fin >> cell;
      v.push_back(cell);
    }
    cout << "Case #" << i+1 << ": " << getMaxNum(p, v) << endl;
  }
  fin.close();
  return 0;
}
