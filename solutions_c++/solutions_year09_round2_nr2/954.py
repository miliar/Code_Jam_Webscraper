#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cstring>
using namespace std;

#define all(v) (v).begin(), (v).end()

void printNext(const string &num)
{
  vector<int> v(num.size());
  for (int i = 0; i < num.size(); i++) {
    v[i] = num[i] - '0';
  }

  bool res = next_permutation(all(v));
  if (res) {
    copy(all(v), ostream_iterator<int>(cout, "")); cout << endl;
  } else {
    //sort(all(v));
    int min_nzd = 0;
    for (int i = 0; i < v.size(); i++) {
      if (v[min_nzd] == 0) min_nzd = i;
      if (v[min_nzd] > v[i] && v[i] != 0) min_nzd = i;
    }
    int t = v[0];
    v[0] = v[min_nzd];
    v[min_nzd] = t;
    sort(v.begin()+1, v.end());
    v.insert(v.begin()+1, 0);
    //next_permutation(all(v));
    copy(all(v), ostream_iterator<int>(cout, "")); cout << endl;
  }
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

  int T;
  fin >> T >> ws;
  char buf[25];
  for (int i = 0; i < T; i++) {
    memset(buf, 0, 25);
    fin.getline(buf, 25);
    stringstream ss;
    ss << buf;
    string num;
    ss >> num;
    cout << "Case #" << i+1 << ": ";
    printNext(num);
    fin >> ws;
  }
  return 0;
}
